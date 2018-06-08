from nltk import word_tokenize, sent_tokenize

text = "The quick brown fox jumped! Where? over the lazy dog."
#Misahin perkata, dipisahin spasi
words = word_tokenize(text)
print(words)

#Misahin perkalimat, dipisahin tanda baca
sentences = sent_tokenize(text)
print(sentences)

#Misahin perkata dari kalimat yang didapat dari sent_tokenize()
for sentence in sentences:
    words = word_tokenize(sentence)
    print(words)