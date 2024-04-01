#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            raise KeyError("Invalid JSON structure")
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            return 0  # Subreddit not found
        else:
            print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None  # Return None if an error occurs


# Example usage:
subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
if subscribers is not None:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print("Failed to retrieve subscriber count.")
