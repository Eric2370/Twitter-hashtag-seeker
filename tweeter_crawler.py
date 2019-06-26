'''
#Import the necessary methods from tweepy library
import twitter_credentials

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['education'])
'''


import twitter_credentials
import csv
import tweepy
import unicodedata


access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



def printout(api):
    user = api.get_user('jasonxwanggg')
    print(user.screen_name)
    print(user.followers_count)
    count = 0
    for friend in user.friends():
       print(friend.screen_name)
       count += 1
    print(count)


if __name__ == '__main__':
    #
    #This handles Twitter authetification and the connection to Twitter Streaming API
    api = tweepy.API(auth)
    diction = {}
    '''
    csvFile = open('edchat.csv', 'r')
    previous_file_list = []
    for item in csv.reader(csvFile):
        previous_file_list.append(item)
    csvFile.close()
    '''
    csvFile = open('edtech.csv', 'w')
    csvWriter = csv.writer(csvFile)
    count = 0
    for tweet in tweepy.Cursor(api.search,
                               q="#edtech",
                               tweet_mode = 'extended',
                               truncated = False,
                               lang = "en",
                               count = 200).items(10000):

        count += 1
        try:
            csvWriter.writerow([tweet.created_at, tweet.full_text])
        except UnicodeEncodeError:
            csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])
        #diction[str(tweet.created_at)] = tweet.full_text
        #print(tweet.full_text.encode('unicode-escape').decode('utf-8'))
    for item in previous_file_list:
        csvWriter.writerow(item)
    csvFile.close()
