import praw

import csv

REDDIT_CLIENT_ID = "VXYCrQAymaBrLQ"
REDDIT_CLIENT_SECRET = "0Wwvv9zptchx7iqweK52cvbtX4A"
REDDIT_USER_AGENT = "WSB"

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret = REDDIT_CLIENT_SECRET, 
                     user_agent=REDDIT_USER_AGENT)

reddit_financials = reddit.subreddit(
        'wallstreetbets+investing+stocks+options+SecurityAnalysis+RobinHood+tradevol+thewallstreet')

for comment in reddit_financials.stream.comments():
	row = [comment.id, comment.body, comment.created_utc, comment.subreddit_id]
	with open('comments.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerow(row)
