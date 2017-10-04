dm_bot
======

** This bot has been decomissioned **

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

I was originally using imgur, however imgur would compress images over 1MB so [they were unreadable.](https://i.imgur.com/CQ5tLg1.jpg) I now use [a.pomf.se](http://a.pomf.se/sodjxu.jpg) as it allows for the full image to be shown.

I am aware the code is not in good shape, I keep just patching it manually to keep up with new image hosts, it is just intended to be a fun script, not a work of art!

I have been banned from: 
  * /r/sydney
  * /r/texas
  * /r/imagesofthe1970s
  * /r/ImagesOfThe2010s
  * /r/ImagesOfEngland
  * /r/DoctorWhumour
  * /r/historyblogs
  * /r/nufcirclejerk
  * /r/nufcirclejerk
  * /r/The_Donald
  * /r/Mr_Trump
  * /r/Minecraft
  * /r/ireland
  * /r/youranonnews
  * /r/army
  * /r/Conservatives_R_Us
  * /r/conservatives
  * /r/skeptic
  * /r/hipsterhuskies
  * /r/science
  * /r/SandersForPresident
  * /r/politota
  * /r/UKIP
  * /r/ukipparty
  * /r/gaming
  * /r/Romania
  * /r/worldnews
  * /r/photoshopbattles
  * /r/unitedkingdom
  * /r/funfacts
  * /r/travel
  * /r/China
  * /r/interestingasfuck
  * /r/conspiratard
  * /r/inthenews
  * /r/funny
  * /r/politics
  * /r/NaziHunting
  * /r/Celebs
  * /r/Conservative
  * /r/UpliftingNews
  * /r/WTF
  * /r/news
  * /r/AnyMore
  * /r/necrodancer
  * /r/celebnsfw
  * /r/space
  * /r/reactiongifs
  * /r/nottheonion
  * /r/ukpolitics
  * /r/WhiteRights
  * /r/unitedkingdom
  * /r/european
  * /r/ebola
  * /r/soccer

[List of potential image hosts](https://docs.google.com/spreadsheets/d/1kh1TZdtyX7UlRd55OBxf7DB-JGj2rsfWckI0FPQRYhE/edit#gid=0)
