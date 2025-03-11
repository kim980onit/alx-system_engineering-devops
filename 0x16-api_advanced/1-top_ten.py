#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by u/example_user)"}
    params = {"limit": 10}

    response = requests.get
    (url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    results = response.json().get("data", {}).get("children", [])

    if not results:
        print("None")
        return

    for post in results:
        print(post.get("data", {}).get("title", "None"))
