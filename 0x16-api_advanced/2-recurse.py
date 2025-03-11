#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "MyRedditBot/1.0 (by u/example_user)"
            }
    params = {"after": after, "limit": 100}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        hot_list.append(post.get("data", {}).get("title", "None"))

    after = data.get("after", None)

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
