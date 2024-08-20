#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests

def top_ten(subreddit):
    """ Queries the Reddit API and prints the top ten hot posts of a subreddit """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if res.status_code != 200:
        print(None)
        return
    
    try:
        dic = res.json()
    except ValueError:
        # This will catch JSON decoding errors
        print(None)
        return
    
    hot_posts = dic.get('data', {}).get('children', [])
    
    if not hot_posts:  # Simplified the check for an empty list
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])


# #!/usr/bin/python3
# """
# Function that queries the Reddit API and prints
# the top ten hot posts of a subreddit
# """
# import requests
# import sys


# def top_ten(subreddit):
#     """ Queries to Reddit API """
#     u_agent = 'Mozilla/5.0'

#     headers = {
#         'User-Agent': u_agent
#     }

#     params = {
#         'limit': 10
#     }

#     url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
#     res = requests.get(url,
#                        headers=headers,
#                        params=params,
#                        allow_redirects=False)
#     if res.status_code != 200:
#         print(None)
#         return
#     dic = res.json()
#     hot_posts = dic['data']['children']
#     if len(hot_posts) == 0:
#         print(None)
#     else:
#         for post in hot_posts:
#             print(post['data']['title'])
