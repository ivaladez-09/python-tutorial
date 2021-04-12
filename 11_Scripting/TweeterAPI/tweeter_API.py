import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")

def limit_handler(cursor):
    """To handle the times that you use the Tweeter API
    in certain time and avoiding RateLimitError"""
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

# Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Ajeasmith':  # random user
        follower.follow()
        break