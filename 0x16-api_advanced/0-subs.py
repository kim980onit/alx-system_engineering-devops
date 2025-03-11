#!/usr/bin/python3
"""
subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about.json" 
    headers = {"User-Agent": "MyRedditBot/1.0 (by u/your_reddit_username)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)

        return 0
