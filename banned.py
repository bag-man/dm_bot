#!/bin/python2.7
import praw

r = praw.Reddit(user_agent='saved_links')
r.login('DailMail_Bot', 'redacted', disable_warning=True)

print "I have been banned from: "
for message in r.get_inbox(limit=None, time='all'):
    if "banned" in message.body:
        print "  * /r/" + str(message.subreddit)
