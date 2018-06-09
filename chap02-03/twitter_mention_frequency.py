import sys
from collections import Counter
import json

#python twitter_hashtag_stats.py <file jsonl>

def get_mentions(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('user_mentions', [])
    return [tag['screen_name'] for tag in hashtags]

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        users = Counter()
        for line in f:
            tweet = json.loads(line)
            mention_in_tweet = get_mentions(tweet)
            users.update(mention_in_tweet)
        for user, count in users.most_common(20):
            print("{}: {}".format(user, count))