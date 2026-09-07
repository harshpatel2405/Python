str = 'Python is easy and powerful language and Python is the the best language in the world'
sentence = str.split()
print(len(sentence))

word_freq_count = {}
for word in sentence:
    if word in word_freq_count.keys() :
        word_freq_count[word] +=1
    else:
        word_freq_count[word] =1

print(word_freq_count)        