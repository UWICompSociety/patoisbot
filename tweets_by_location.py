import sys
import tweepy
import argparse


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        file = open("jamtweets.txt", "a+")
        file.write(status.text + "\n")
        file.close()

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print('Timeout...')
        return True # Don't kill the stream

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
	description='Arguments for authentication')
	parser.add_argument('--consumer_key', help='consumer key', required=True)
	parser.add_argument('--consumer_secret', help='consumer key', required=True)
	parser.add_argument('--access_key', help='consumer key', required=True)
	parser.add_argument('--access_secret', help='consumer key', required=True)

	args = parser.parse_args()

	auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)
	auth.set_access_token(args.access_key, args.access_secret)

	sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
	sapi.filter(locations=[-78.3377192858, 17.7011162379, -76.1996585761, 18.5242184514])