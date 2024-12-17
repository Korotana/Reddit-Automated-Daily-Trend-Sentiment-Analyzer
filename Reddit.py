import praw
# Initialize the Reddit API client

reddit = praw.Reddit(
    client_id="pxwTvvfE-JJ6uPYYSbzmag",
    client_secret='TXxhXnQ1o5G0-wZVxiem8c5-Jh_vEQ',  # Replace with your Client Secret
    user_agent='TrendAnalyzer'  # Set a user agent (e.g., 'myRedditApp')
    )

subreddit = reddit.subreddit('all')  # You can also choose specific subreddits


def fetch_reddit_posts(trend):
    return subreddit.search(trend, limit=10)



# Fetch the top 10 recent posts
