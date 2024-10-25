#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit exists or if there's an error
    if response.status_code != 200:
        print(None)
        return

    # Parse response safely
    try:
        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post['data'].get('title', ''))
    except (ValueError, KeyError, TypeError):
        print(None)

