# Word Frequency

sentence = "The quick brown fox jumps over the lazy dog."
word_frequncies = {}

# Split the sentence into words
words = sentence.split()

# Count word frequncies
for word in words:
    if word in word_frequncies:
        word_frequncies[word] += 1
    else:
        word_frequncies[word] = 1
print(word_frequncies)
