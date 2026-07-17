'''
Word Length Analyzer

Given a sentence, store all words in a list and display:

Longest word
Shortest word
Average word length
Words having more than 5 characters
'''

sentence = 'Python is a very powerful language with a marvellous number of libraries'

sentence = sentence.split()
print(sentence)

# * longest word
longWord = ''
for word in sentence:
    if(len(longWord) < len(word)):
        longWord = word
print("Longest Word :",longWord)

# * shortest word
shortWord = sentence[0]
for word in sentence:
    if(len(shortWord) > len(word)):
        shortWord = word

print("Shortest Word :",shortWord)

# * average word length 
sumWord = 0
for word in sentence:
    sumWord += len(word)

avgLength = sumWord / len(sentence)
print("Average Word Length :",avgLength)

# * Words having more than 5 characters
print("Word Having more Than 5 Characters : ", end = " ")
for word in sentence:
    if(len(word) > 5):
        print(word, end= ", ")
