from pytrends.request import TrendReq
import time

# Initialize pytrends API
pytrends = TrendReq(hl='en-US', tz=360)


def get_trending_searches(region='united_states'):
    try:
        # Attempt to get trending search terms for the region
        trending_searches = pytrends.trending_searches(pn=region)

        # Check if we get valid data
        if trending_searches.empty:
            print(f"No trending searches found for {region.capitalize()}.")
        else:
            print(f"Top 10 Global Trending Searches in:{region.capitalize()}")
            return trending_searches.head(10)[0]

    except Exception as e:
        # Handle errors (e.g., network issues, invalid region, etc.)
        print(f"Error occurred while fetching trending searches for {region.capitalize()}:{e}")
        time.sleep(5)  # Delay before retrying the request
        get_trending_searches(region)  # Retry after a delay


print(get_trending_searches())




# # Step 2: Use keywords instead of category ID
# keywords = ['car', 'tesla', 'laptops', 'headphones', 'TV', 'camera']  # Broad and popular keywords
# pytrends.build_payload(kw_list=keywords, timeframe='now 1-d')
#
# # Fetch related queries for the keyword
# try:
#     related_queries = pytrends.related_queries()
#     time.sleep(10)
#     print("\nRelated Queries for 'tesla':")
#
#     if related_queries.get('tesla') is not None:
#         data = related_queries['tesla']
#         if data.get('top') is not None:
#             print("Top related queries:")
#             print(data['top'])
#         else:
#             print("No top related queries available.")
#
#         if data.get('rising') is not None:
#             print("Rising related queries:")
#             print(data['rising'])
#         else:
#             print("No rising related queries available.")
#     else:
#         print("No related queries found for the keyword 'tesla'.")
# except Exception as e:
#     print(f"Error occurred: {e}")