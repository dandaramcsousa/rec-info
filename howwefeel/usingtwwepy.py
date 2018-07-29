import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = '8WapSfEhcer2K3Srrda7G381B'
consumer_secret = 'B2wR2jckiqB5Cc8SJ2EdUS9O97GnmKCxe84uw3jQnENDqvCYb7'
access_token = '967904006843625472-lpsgiZwCeKLWKLK8SIOwd8VaWCrmIsP'
access_token_secret = 'aUg8GsDn4jkU2g1smyjjMLZWDYyanVBdWHrpHQbxYODUZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('lula.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['DATE', 'TWEET'])
for tweet in tweepy.Cursor(api.search,q="#lulalivre",count=100,
                           lang="pt",
                           since="2018-04-07").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
