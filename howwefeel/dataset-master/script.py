# coding=utf-8
import tweepy
import time
import db

consumer_key = '8WapSfEhcer2K3Srrda7G381B'
consumer_secret = 'B2wR2jckiqB5Cc8SJ2EdUS9O97GnmKCxe84uw3jQnENDqvCYb7'
token_key = '967904006843625472-lpsgiZwCeKLWKLK8SIOwd8VaWCrmIsP'
token_secret = 'aUg8GsDn4jkU2g1smyjjMLZWDYyanVBdWHrpHQbxYODUZ'


def download_tweets(id_file, sentiment):
    with open(id_file) as infile:
        for tweet_id in infile:
            tweet_id = tweet_id.strip()

            if db.exist_tweet(tweet_id):
                print("tweet com id: ", tweet_id, "ja foi capturado")
                continue

            try:
                tweet = api.get_status(tweet_id)
                db.add_tweet(tweet, sentiment)
            except tweepy.error.TweepError:
                print("tweet com id: ", tweet_id, "nao esta disponivel")

            time.sleep(1)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

#print("Capturando tweets positivos ...")
#download_tweets("positivos.txt", 1)

print("Capturando tweets negativos ...")
download_tweets("negativos.txt", 0)

print("Fim.")
