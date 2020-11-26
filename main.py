import praw
import time

reddit = praw.Reddit(client_id='ZZcN-zl26sktNA',
                     client_secret='p-Aw1vaH6_nKvV6n48Sq3kgaZ0kdNA',
                     user_agent='a reddit instance',
                     username='Jewish-Grandma',
                     password='zzzzzz10', )


def subspam():
    textmintuit = "We are building a personal finance tool that goes to " \
                  "the product level. No more of Mint's terrible categorization, like 'Shopping' for all Amazon " \
                  "purchases. Interested in getting early access? "
    textynab = "We are building a personal finance tool that goes to the product level and categorizes products " \
               "automatically. No more ugly categorization, like 'Shopping' for all Amazon purchases. Interested in " \
               "getting early access? "
    textstartups = "We are building a personal finance tool that goes to the product level. No more of Mint's " \
                   "terrible categorization, like 'Shopping' for all Amazon purchases. Interested in getting early " \
                   "access? "
    textentrepeneur = "We are building a personal finance tool that goes to the product level. No more of Mint's " \
                      "terrible categorization, like 'Shopping' for all Amazon purchases. Interested in getting early" \
                      " access? "
    textsideproject = "My project is a personal finance tool that goes to the product level to help you budget and " \
                      "save. No more of Mint's terrible categorization, like 'Shopping' for all Amazon purchases. " \
                      "Interested in getting early access? "
    subname = 'ynab+mintuit+startups+EntrepreneurRideAlong+SideProject'  # you need to change this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Hello, {name}'
        if name in usedusernames:
            continue
        try:
            if comment.subreddit.display_name == "ynab":
                text = textynab
            elif comment.subreddit.display_name == "mintuit":
                text = textmintuit
            elif comment.subreddit.display_name == "startups":
                text = textstartups
            elif comment.subreddit.display_name == "EntrepreneurRideAlong":
                text = textentrepeneur
            else:
                text = textsideproject
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(f'u/{name} r/{comment.subreddit.display_name}')
        time.sleep(40)


subspam()
