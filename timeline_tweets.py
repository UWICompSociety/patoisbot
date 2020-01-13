import tweepy
import argparse


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
	description='Arguments for authentication')
	parser.add_argument('--consumer_key', help='consumer key', required=True)
	parser.add_argument('--consumer_secret', help='consumer key', required=True)
	parser.add_argument('--access_key', help='consumer key', required=True)
	parser.add_argument('--access_secret', help='consumer key', required=True)

	args = parser.parse_args()

	# Authenticate to Twitter
	auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)
	auth.set_access_token(args.access_key, args.access_secret)

	# Create API object
	api = tweepy.API(auth)
	# Create a tweet

	#api.update_status("I am skynet")

	#View timeline tweets

	timeline = api.home_timeline()
	for i, tweet in enumerate(timeline):
		print(i + 1, ")", tweet.user.name, " ",  tweet.user.location)


	#Filter tweets with query
	for i, tweet in enumerate(api.search(q="Jamaica", lang="en", rpp=10)):
		print(i+1, ")" , tweet.text)

	user = api.get_user("elonmusk")
	print(user.name)
	print(user.description)
	print("Last 20 Followers:")
	for follower in user.followers():
		print(follower.name)
