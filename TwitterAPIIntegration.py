import tweepy
import time
import Trending_Searches

# Read Twitter Bearer Token
twitter_bearer_token_filepath = r"C:\Users\YuvrajKorotana\PycharmProjects\PythonAutomationScriptforCloudServices\twitter-bearer-token"

with open(twitter_bearer_token_filepath, 'r') as f:
    twitter_bearer_token = f.read()


def fetch_tweets(product_name):
    """
    Fetch recent tweets about a product, making a single API call and handling rate limits.
    """
    client = tweepy.Client(bearer_token=twitter_bearer_token)

    query = f"{product_name} -is:retweet"
    print(f"Fetching tweets for: {product_name}")

    response = client.search_recent_tweets(query=query, max_results=10)

    try:

        # Make the actual request
        # response = client.search_recent_tweets(query=query, max_results=10)

        # Rate limit information from response headers
        remaining = int(response.headers.get('x-rate-limit-remaining', 0))
        reset_time = int(response.headers.get('x-rate-limit-reset', 0))

        print(f"Remaining requests: {remaining}")

        if remaining == 0:
            current_time = time.time()
            sleep_time = reset_time - current_time
            if sleep_time > 0:
                print(f"Rate limit exceeded. Sleeping for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)  # Wait until the reset time
            else:
                print("Rate limit is already reset, continuing with the next request.")

        # Process tweets if available
        if response.data:
            print(f"Fetched {len(response.data)} tweets for '{product_name}'.")
            return [(tweet.id, tweet.text) for tweet in response.data]
        else:
            print(f"No tweets found for '{product_name}'.")
            return []
    except tweepy.TooManyRequests:
        # Handle TooManyRequests exception explicitly
        print("Rate limit exceeded. Waiting until the reset period...")
        time.sleep(180)  # Conservative wait time
    except Exception as e:
        print(f"Error fetching tweets for '{product_name}': {e}")
        return []

# Main process
tweets_data = []

try:
    # Get trending searches for Canada
    trending_searches = Trending_Searches.get_trending_searches('canada')

    print(f"Fetching tweets for the following trends:\n {trending_searches}")
    for trend in trending_searches:
        # Fetch tweets for each trend sequentially
        tweets = fetch_tweets(trend)
        # Optional: Introduce a delay to avoid hitting rate limits unnecessarily
        print(f"Sleeping for 5 seconds between requests...")
        time.sleep(5)

        tweets_data.append({trend: tweets})

except Exception as e:
    print(f"Error in processing: {e}")

# Output tweets data
print("Tweets Data:")
print(tweets_data)
