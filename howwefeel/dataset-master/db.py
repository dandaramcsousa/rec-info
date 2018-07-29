#conding: utf-8

import sys
from pony import orm
import pandas as pd

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
db = orm.Database()


class Tweet(db.Entity):
    tweet_id = orm.Required(str)
    text = orm.Required(str)
    sentiment = orm.Required(int)

db.bind('sqlite', 'tweets.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@orm.db_session
def add_tweet(tweet, sentiment):
    text = tweet.text.translate(non_bmp_map)
    tweet = Tweet(tweet_id=str(tweet.id), text=text, sentiment=sentiment)
    orm.commit()


@orm.db_session
def get_tweets():
    return orm.select(t for t in Tweet)[:].show()


@orm.db_session
def exist_tweet(tweet_id):
    return Tweet.get(tweet_id=tweet_id) is not None


@orm.db_session
def to_csv():
    tweets = orm.select(t for t in Tweet)

    df = pd.DataFrame([], columns=['id', 'text', 'sentiment'])

    for tweet in tweets:
        df_temp = pd.DataFrame([[int(tweet.id), tweet.text, tweet.sentiment]], columns=[
                               'id', 'text', 'sentiment'])
        df = df.append(df_temp)

    df.to_csv('db.csv', sep=';', index=False)
