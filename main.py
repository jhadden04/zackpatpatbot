import praw
import time
reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     user_agent='a reddit instance',
                     username='*',
                     password='*', )

def subspam():
    title = 'hello, stranger'   #  you need to change this
    text = 'How is your day going'  # you need to change this
    subname = 'Johntesting' # you need to change this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        if name in usedusernames:
            continue
        try:
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(name)
        time.sleep(40)

subspam()
