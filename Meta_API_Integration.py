import requests
import time

# Your access token and user ID (replace with your actual data)
meta_access_token_filepath = "MetaAPIToken"
user_id = "122103148604678"


with open(meta_access_token_filepath, 'r') as f:
     meta_access_token = f.read()


def fetch_instagram_posts(user_id, access_token):
    """
    Fetch recent posts from an Instagram Business Account using the Graph API.
    """
    url = f"https://graph.instagram.com/{user_id}/media"
    params = {
        'fields': 'id,caption,media_type,media_url,thumbnail_url,permalink,timestamp',
        'access_token': access_token
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'data' in data:
            posts = data['data']
            print(f"Fetched {len(posts)} posts.")
            return posts
        else:
            print("No posts found or error occurred.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

# Main process
posts_data = []

# Fetch posts
posts = fetch_instagram_posts(user_id, meta_access_token)
posts_data.extend(posts)

# Handle rate limits if necessary
# Check response headers for rate limits or include time.sleep if you notice limits.
