import praw
import random
import time

reddit = praw.Reddit(
    client_id="client id",
    client_secret="secret",
    user_agent="<console:PYJOKES:6.8>",
    username = "Botty_Py",
    password = "password"
)

subreddit = reddit.subreddit("programming")

python_jokes = ["Why does Python live on land? Becasue it is above C level!", "Ppl: You can just copy paste pseudo code and excpect it to work!, Python: That's Where You are Wrong Kiddo"]

for submission in subreddit.hot(limit=10):
    print('******')
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " python " in comment_lower:
                print('------')
                print(comment.body)
                random_index = random.randint(0, len(python_jokes) -1)
                comment.reply(python_jokes[random_index])
                time.sleep(660)
