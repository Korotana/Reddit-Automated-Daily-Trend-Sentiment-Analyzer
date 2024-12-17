import requests
import time

# Your access token and user ID (replace with your actual data)
meta_access_token_filepath = "MetaAPIToken"
user_id = "122103148604678035"
with open(meta_access_token_filepath, 'r') as f:
    meta_access_token = f.read()

def fetch_facebook_posts_by_keyword(keyword, meta_access_token, limit=10):
    """
    Fetch recent Facebook posts based on a given keyword.
    """
    url = "https://graph.facebook.com/v12.0/search"  # Change to latest API version
    params = {
        'q': keyword,
        'type': 'post',
        'fields': 'id,message,created_time',
        'access_token': meta_access_token
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        data = response.json()

        # Log the full response to check for errors
        print("Response:", data)

        if 'data' in data:
            posts = data['data']
            print(f"Fetched {len(posts)} posts for keyword: {keyword}")
            return posts[:limit]  # Return only the number of posts requested (e.g., limit to 10)
        else:
            print("No posts found or error occurred.")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

# Example usage
keyword = "Manchester United"
posts = fetch_facebook_posts_by_keyword(keyword, meta_access_token)

# Display fetched posts
for post in posts:
    print(f"Post ID: {post['id']}")
    print(f"Message: {post['message']}")
    print(f"Created Time: {post['created_time']}")
    print("-" * 50)
