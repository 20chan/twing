import twitter

f = open('key.config')
cons_key, cons_sec, tok_key, tok_sec = f.read().split()

api = twitter.Api(consumer_key=cons_key,
        consumer_secret=cons_sec,
        access_token_key=tok_key,
        access_token_secret=tok_sec)

# print(api.VerifyCredentials())

adnim = api.GetUser(screen_name='0xadnim')
print(adnim)
