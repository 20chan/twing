import tweepy

f = open('key.config')
cons_key, cons_sec, tok_key, tok_sec = f.read().split()
class twingbot:
    def __init__(self, cons_key, cons_sec, tok_key, tok_sec):
        auth = tweepy.OAuthHandler(cons_key, cons_sec)
        auth.set_access_token(tok_key, tok_sec)
        self.api = tweepy.API(auth)

    def tweet(self, msg):
        self.api.update_status(msg)

    def tweet_media(self, path, msg=None):
        self.api.update_with_media(path, status=msg)

