from gensim.summarization import summarize
import sys

#Summarize file lord_of_the_rings.txt
#jalanin python demo_gensim.py lord_of_the_rings.txt
fname = sys.argv[1]

with open(fname, 'r') as f:
    content = f.read()
    summary = summarize(content, split=True)
    for i, sentence in enumerate(summary):
        print("{0}) {1}".format(i+1, sentence))