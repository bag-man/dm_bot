import urllib
import praw
import os
import requests
import time

from selenium import webdriver
from PIL import Image
from xvfbwrapper import Xvfb


def getScreenShot(url):
    # http://stackoverflow.com/a/6300672
    # http://stackoverflow.com/a/15870708

    fox.get(url)

    element = fox.find_element_by_id('js-article-text')
    comment = element.find_element_by_id('socialLinks')

    end = comment.location
    location = element.location
    size = element.size

    fox.save_screenshot('screenshot.jpg')

    im = Image.open('screenshot.jpg')

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + end['y'] - 500

    im = im.crop((left, top, right, bottom))
    im.save('screenshot.jpg', "JPEG")


vdisplay = Xvfb()
vdisplay.start()

fox = webdriver.Firefox()

comment = """
[Non-Daily Mail Mirror](%s)

^(Code on) ^[github](https://github.com/bag-man/dm_bot).
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
                        response = requests.post(
                            url="http://pomf.se/upload.php",
                            files={"files[]": open("screenshot.jpg", "rb")}
                        )
                        link = "http://a.pomf.se/" + response.text.split('"')[17]
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
        print "Reddit's down?!"
        print e
fox.quit()
vdisplay.stop()
