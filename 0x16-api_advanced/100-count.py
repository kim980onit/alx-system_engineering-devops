#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after=None):
    if instances is None:
        instances = {}

    if after is None:
        word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "RedditCounterBot/1.0"}
    params = {"after": after, "limit": 100}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    after = data.get("after")

    for post in data.get("children", []):
        title_words = post["data"]["title"].lower().split()
        for word in word_list:
            count = title_words.count(word)
            if count > 0:
                instances[word] = instances.get(word, 0) + count

    if after:
        return count_words(subreddit, word_list, instances, after)

    if instances:
        sorted_results = sorted(
                instances.items(), key=lambda kv: (-kv[1], kv[0])
                )
        for word, count in sorted_results:
            print(f"{word}: {count}")
