import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    hashtag = sys.argv[1]
    client = get_twitter_client()

    fname = "hashtag_timeline_{}.jsonl".format(hashtag)

    with open(fname, 'w') as f:
        for tweet in Cursor(client.search, q="#{}".format(hashtag), count=200).pages(16):
            # print(tweet.created_at, tweet.text)
            for status in tweet:
                f.write(json.dumps(status._json)+"\n")