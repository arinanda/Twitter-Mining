import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()

    fname = "user_mention.jsonl"

    with open(fname, 'w') as f:
        for page in Cursor(client.mentions_timeline, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+"\n")