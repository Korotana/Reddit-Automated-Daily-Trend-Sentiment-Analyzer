import time
import logging
import CloudConnection
import Trending_Searches
import Reddit
import Sentiment_Analyze

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def push_to_cloud(post, sentiment, trend):
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(prepared=True)

        # Use prepared statements to prevent SQL injection
        sql_insert_trend = "INSERT INTO Trends (name) VALUES (%s)"
        sql_insert_mention = "INSERT INTO Mentions (trend_id, post_url, sentiment, post_text) VALUES (%s, %s, %s, %s)"

        # Insert the trend and get its ID
        cursor.execute(sql_insert_trend, (trend,))
        trend_id = cursor.lastrowid  # Get the last inserted ID
        cursor.execute(sql_insert_mention, (trend_id, post.url, sentiment, post.title))

        connection.commit()
        connection.close()
        logging.info(f"Pushed post {post.id} to cloud for trend {trend}")
        return True  # Indicate success

    except Exception as e:
        logging.error(f"Error pushing to cloud: {e}")
        return False  # Indicate failure


try:
    # Get trending searches for Canada
    trending_searches = Trending_Searches.get_trending_searches('canada')

    print(f"Fetching tweets for the following trends:\n {trending_searches}")
    for trend in trending_searches:
        print(f"Fetching reddit posts for the following trends:\n {trend}")
        posts = Reddit.fetch_reddit_posts(trend)
        for each_post in posts:
            # Fetch the comments for the specific submission
            each_post.comments.replace_more(limit=0)  # Remove "MoreComments" objects
            comments = each_post.comments.list()  # Convert comments into a list

            sentiment = Sentiment_Analyze.analyze_multiple_sentiment_average(comments)

            # Retry mechanism to ensure successful push
            while True:
                success = push_to_cloud(each_post, sentiment, trend)
                if success:
                    break  # Exit the loop if successful
                else:
                    logging.warning("Retrying push to cloud...")
                    time.sleep(5)  # Wait before retrying

            time.sleep(5)  # Optional: Delay between posts

except Exception as e:
    logging.error(f"Error in processing: {e}")
    print(f"Error in processing: {e}")

