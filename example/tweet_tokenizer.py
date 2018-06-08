from nltk.tokenize import TweetTokenizer

#Misahin perkata yang bisa detect link, emot, hashtag, dll.
tokenizer = TweetTokenizer()
tweet = '@marcobonzanini: an example! :D http://example.com #NLP'
print(tokenizer.tokenize(tweet))