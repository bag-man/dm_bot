import urllib
import praw
import os
import requests
import time
import json

from selenium import webdriver
from PIL import Image
from googleapiclient.discovery import build
from config_dmbot import *

def findAnother(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def getScreenShot(url):
    # http://stackoverflow.com/a/15870708

    driver.get(url)

    term = driver.title[:-20].replace("'","")

    print term

    foundsources = findAnother(term, my_api_key, my_cse_id, num=2)

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

    return foundsources, term

# set livemode to False to disable comment posting

livemode = True

driver = webdriver.PhantomJS()

commentheader = """
Here are some potential alternative sources for this story:


"""

comment = """

The above links were automatically generated. If they don't work, [here is a screenshot of the original article.](%s)

^^I'm ^^trying ^^to ^^help ^^so ^^please ^^don't ^^ban ^^me, ^^just ^^downvote ^^me. ^^I ^^auto-delete ^^my ^^comments ^^with ^^a ^^score ^^of ^^-1 ^^or ^^less. ^^I ^^am ^^a ^^bot ^^based ^^on [^^this ^^code](https://github.com/bag-man/dm_bot).
"""

postedOn = []
r = praw.Reddit(user_agent='Non-DM Mirror Helper')

r.login(reddit_user_id, reddit_password)

reddits = {'politics', 'reddevils', 'dailymail', "the_donald", "conspiracy", "cordcutters"}

# comment out the above line and uncomment the next one for testing
# reddits = {'bot_sandbox'}

user = r.get_redditor(reddit_user_id)

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
                    print str(submission.subreddit).lower()
                    if submission.domain == "dailymail.co.uk":
                        try:
                            alternatives,title = getScreenShot(submission.url.rstrip())
                        except Exception, e:
                            print "Failed to get image at:" + submission.url.rstrip()
                            print e
                    elif submission.domain == "i.dailymail.co.uk":
                        urllib.urlretrieve(submission.url, "screenshot.jpg")

                    if livemode == True:

                        try:
                            res = requests.post(
                                url="https://filebunker.pw/upload.php",
                                files={"files[]": open("screenshot.jpg", "rb")}
                            )
                            altlink = ""
                            for source in alternatives:
                                altlink = altlink + "["+source['title']+"]("+source['link']+")\n\n"
                            data = json.loads(res._content)
                            link = data["files"][0]["url"]
                            submission.add_comment(commentheader + altlink + comment % (link))
                            print "Posted!"
                        except Exception, e:
                            print "Failed to submit:"
                            print e

                    else:
                        print "Live mode Off. Testing only."

                    if(os.path.isfile('screenshot.jpg')):
                        os.remove('screenshot.jpg')
                    postedOn.append(submission.id)
        
        for c in user.get_comments(limit=20):
            if c.score <= -1:
                print("We got an unpopular one, folks")
                c.delete()
                
        time.sleep(5)
        first = False
        
    except Exception, e:
        print e

driver.quit()
