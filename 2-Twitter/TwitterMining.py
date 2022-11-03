import json
import csv
import tweepy
import re
import os

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
    ntweets: how many tweets do you want (be carefull, Twitter limits this to some maximum (200))
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, ntweets):

    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initialize Tweepy API
    api = tweepy.API(auth)

    # get the name of the spreadsheet we will write to
    totalFileList = os.listdir(
        "/home/woutd/Documents/School/Industriele Ingenieurswetenschappen/Ma1/Sem1/Machine Learning/Opdracht/Workspace/2-Twitter/")
    currentAvailableDatasets = []
    for fileName in totalFileList:
        if ('Barcelona' in fileName):
            currentAvailableDatasets.append(fileName)

    currentAvailableDatasets = sorted(currentAvailableDatasets)
    print(currentAvailableDatasets)
    count = int(
        ((currentAvailableDatasets[-1].split('_'))[1].split('.'))[0]) + 1
    fname = 'Barcelona_' + str(count)

    # open the spreadsheet we will write to
    with open('/home/woutd/Documents/School/Industriele Ingenieurswetenschappen/Ma1/Sem1/Machine Learning/Opdracht/Workspace/2-Twitter/%s.csv' % (fname), 'w', newline='', encoding='utf8') as file:

        w = csv.writer(file)
        print("file:", file)

        # write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username',
                   'all_hashtags', 'followers_count'])

        # for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag_phrase+' -filter:retweets',
                                   lang="en", tweet_mode='extended').items(ntweets):
            print(tweet)
            try:
                w.writerow([tweet.created_at, tweet.full_text.replace('\n', ' '), tweet.user.screen_name.encode(
                    'utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
            # except UnicodeEncodeError as unierr:
                #print("Some UnicodeError happened",unierr)
            except:
                print("An exception occurred")


consumer_key = 'OtmyGwl2Brs3rlfIJww3L5HTR'
consumer_secret = 'USKLKODU4IWCDJ5SsTRoLHWGbBejeN9u0udbfzYA27Oy2zmhcQ'
access_token = '3405275561-urpULOztEAr8hQvYgH09ZyZXIB08Z35j4qu61xp'
access_token_secret = 'puAYOe1QXsDtwlnz0fzpiLyBKMgZty81GOwT5OUBcTpVZ'

hashtag_phrase = 'FCBarcelona'

ntweets = 4000  # Twitter limits this value

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token,
                        access_token_secret, hashtag_phrase, ntweets)
