import urllib
import praw
import os
import requests
import time
import json

from selenium import webdriver
from PIL import Image


def getScreenShot(url):
    # http://stackoverflow.com/a/15870708

    driver.get(url)

    element = driver.find_element_by_id('js-article-text')
    comment = element.find_element_by_id('socialLinks')

    end = comment.location
    location = element.location
    size = element.size

    driver.save_screenshot('screenshot.jpg')

    im = Image.open('screenshot.jpg')

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + end['y'] - 510

    im = im.crop((left, top, right, bottom))
    im.save('screenshot.jpg', "JPEG")


driver = webdriver.PhantomJS()

comment = """
[Non-Daily Mail Mirror](%s)

^^Code ^^on ^^[github](https://github.com/bag-man/dm_bot).
"""

postedOn = []
r = praw.Reddit(user_agent='DM_Mirror')

r.login('DailMail_Bot', 'asdf1234')

reddits = {'reddevils', 'politic', 'dailymail'}

print "Logged in"
first = True

while True:
    try:
        posts = r.get_domain_listing('dailymail.co.uk', sort='new', limit=10)
        for submission in posts:
            if str(submission.subreddit).lower() not in reddits:
                if first is True:
                    postedOn.append(submission.id)

                if submission.id not in postedOn:
                    print "We got one! " + submission.short_link
                    if submission.domain == "dailymail.co.uk":
                        try:
                            getScreenShot(submission.url.rstrip())
                        except Exception, e:
                            print "Failed to get image:"
                            print e
                    elif submission.domain == "i.dailymail.co.uk":
                        urllib.urlretrieve(submission.url, "screenshot.jpg")

                    try:
                        res = requests.post(
                            url="http://img.loveisover.me/upload.php",
                            files={"files[]": open("screenshot.jpg", "rb")}
                        )
                        # Returns a dictionary-like json object which has
                        # attributes like:
                        # success: true/false
                        # files:
                        # name:
                        # url:
                        json_object = json.loads(res.text)[u'files']
                        # link is an list that is of length 1 and contains a
                        # dictionary
                        link = "http://a.loveisover.me/" + json_object[0][u'url']
                        submission.add_comment(comment % (link))
                        print "Posted!"
                    except Exception, e:
                        print "Failed to submit:"
                        print e

                    if(os.path.isfile('screenshot.jpg')):
                        os.remove('screenshot.jpg')
                    postedOn.append(submission.id)
        time.sleep(5)
        first = False
    except Exception, e:
        print e

driver.quit()
