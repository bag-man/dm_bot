import praw
import pyimgur
import string
import re

from selenium import webdriver
from PIL import Image
from xvfbwrapper import Xvfb

def getScreenShot(url):
  # http://stackoverflow.com/a/6300672
  # http://stackoverflow.com/a/15870708

  vdisplay = Xvfb()
  vdisplay.start()

  fox = webdriver.Firefox()
  fox.get(url)

  element = fox.find_element_by_id('js-article-text')
  location = element.location
  size = element.size
  fox.save_screenshot('screenshot.png') 
  fox.quit()

  im = Image.open('screenshot.png') 

  left = location['x']
  top = location['y']
  right = location['x'] + size['width']
  bottom = location['y'] + size['height']

  im = im.crop((left, top, right, bottom))
  im.save('screenshot.png')

  vdisplay.stop()

comment =\
"""
Please don't post Daily Mail links!

The DM is a pretty evil organisation, these videos explain it better than me:

* [Why The Daily Mail is Evil](https://www.youtube.com/watch?v=r9dqNTTdYKY)
* [The Daily Mail song](https://www.youtube.com/watch?v=5eBT6OSr1TI)

You can view an image of the article [here](%s) instead of visiting their page.

Or you can find another news source [here](https://www.google.co.uk/#q=%s+-site:dailymail.co.uk).

"""

clientId = "2c85eab2ef18353"
postedOn = []
i = pyimgur.Imgur(clientId)
r = praw.Reddit(user_agent='DM_Bot')
r.login('DM_Bot', 'totallyNotMyPassword')

print "Logged in"
first = True

while True:
  submissions = r.get_domain_listing('dailymail.co.uk', sort='new',limit=100)
  for submission in submissions:
    if first == True:
      postedOn.append(submission.id)
    if submission.id not in postedOn:
      print "We got one!"
      getScreenShot(submission.url.rstrip())
      image = i.upload_image("screenshot.png")
      googleUrl = re.sub('[%s]' % re.escape(string.punctuation), '', submission.title)
      googleUrl = googleUrl.replace(" ","+")
      submission.add_comment(comment % (image.link, googleUrl)) 
      postedOn.append(submission.id)
  first = False

