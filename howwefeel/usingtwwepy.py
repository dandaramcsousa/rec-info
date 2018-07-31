import tweepy
import csv
import pandas as pd
####input your credentials here 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# Open/Create a file to append data
csvFile = open('lulala.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile, delimiter = '\t')
csvWriter.writerow(['DATE', 'TWEET'])
for tweet in tweepy.Cursor(api.search,q="#lulalivre",count=100,
                           lang="pt",
                           since="2018-04-07").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
