#!/usr/bin/python3
"""
subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json" 
    headers = {"User-Agent": "MyRedditBot/1.0 (by u/your_reddit_username)"}

    try;
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        except requests.RequestException:
            return 0

        return 0
