import yaml
import twing
import threading
from time import sleep
from random import choice
import tweepy

ck, cs, tk, ts = open('key.config').read().split()
account = twing.twingbot(ck, cs, tk, ts)
bots = [list(v.values())[0] for v in yaml.load(open('settings.yaml', 'r'))]

class Bot(threading.Thread):
    def __init__(self, bot):
        self.__bot = bot
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                ch = choice(self.__bot['db'])
                if type(ch) == type(''):
                    account.tweet(ch)
                    print('Tweet sent: ' + ch)
                else:
                    account.tweet_media(list(ch.values())[0], msg=list(ch.keys())[0])
                    print('Tweet sent: ' + list(ch.values())[0])
            except tweepy.error.TweepError as e:
                print('Error: ' + e.args[0][0]['message'])
            finally:
                sleep(10 * self.__bot['interval'])

for b in bots:
    bot_th = Bot(b)
    bot_th.start()
