#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursive function to query the Reddit API, parse the title of hot articles, and print a sorted count of given keywords.
    """
    # Base case: subreddit is not valid
    if not subreddit:
        return

    # Initialize count_dict if not provided
    if count_dict is None:
        count_dict = {}

    # Reddit API endpoint for fetching hot posts from a subreddit
    reddit_api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Reddit API requires a User-Agent header to identify the client
    headers = {'User-Agent': 'Reddit API Client'}

    # Parameters for pagination
    params = {'limit': 100}  # Fetch 100 posts per request
    if after:
        params['after'] = after

    # Sending HTTP GET request to the Reddit API
    response = requests.get(reddit_api_url, headers=headers, params=params, allow_redirects=False)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()

        # Extracting information from the response
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for child in children:
                title = child['data']['title']
                # Check for keywords in the title
                for word in word_list:
                    if word.lower() in title.lower():
                        count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

            # Recursive call with the 'after' parameter for pagination
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                # Sort and print the count of keywords
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
