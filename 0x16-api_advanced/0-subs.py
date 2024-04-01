#!/usr/bin/python3
"""Python module that queries the Reddit API and returns the
number of sunscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Obtains number of subscribers in a parsed
    subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        output = response.json()
        number_of_subscribers = output['data']['subscribers']
        return (number_of_subscribers)
    else:
        return 0
