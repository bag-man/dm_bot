dm_bot
======

This bot is more of a learning exercise than anything else, no harm intended.

It works by using phantom.js and selenium to grab a screenshot of the whole page and mark some points for reference. The next step is to crop just the article out of the page by using pillow, and then save it as a jpg to save bandwidth. Once it has done that it can post a comment on the reddit post with a link to the image.

Needs all this installed to work:

* praw        - get reddit posts and comment on them
* selenium    - get screenshot through phantom.js
* pillow      - crop screenshot to just the article
* libjpeg8    - allows pillow to save as jpeg
* phantom.js  - renders the screenshot 

![A picture of the output](http://i.imgur.com/gFrtGnb.png)

[Link to /u/DailMail_Bot. See him in action!](http://www.reddit.com/user/DailMail_Bot)

I was originally using imgur, however imgur would compress images over 1MB so [they were unreadable.](https://i.imgur.com/CQ5tLg1.jpg) I now use [teknik.io](https://u.teknik.io/QVaWQ4.jpg) as it allows for the full image to be shown.
