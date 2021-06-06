import tweepy
import pandas as pd
import time
import os



consumer_key = '--REDACTED--'
consumer_secret = '--REDACTED--'
access_token = '--REDACTED--'
access_token_secret = '--REDACTED--'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets_list = []

def query_to_txt(text_query, count):
    try:
        for tweets in tweepy.Cursor(api.search, q=text_query).items(count):
            if 't.co' not in tweets.text:
                tweets_list.append(tweets.text.replace('\n', ''))
    
        filepath = text_query + '.txt'
        with open(filepath, 'w', encoding='utf-8') as f:
            for i in tweets_list:
                f.write("\n" + i)
                
        print('Count: ', count, '\nTweets: ', len(tweets_list))
        
    except BaseException as e:
        print('failed on_status,', str(e))
    
    
# X is number of tweets to be retrieved
text_query = 'donald trump'
count = 200

query_to_txt(text_query, count)

