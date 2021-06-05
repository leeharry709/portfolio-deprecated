import os
os.chdir('C:/Users/leeha/Documents/pythons/sentiment analysis/')


import string
from collections import Counter
import matplotlib.pyplot as plt


# Create text file
text = open('read.txt', encoding='utf-8').read()

# Make text lowercase
lower_case = text.lower()

# Remove punctuation
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Split words into list
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Remove stop words (words that don't add meaning/emotion)
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
    else:
        pass

# Pre-process emotions.txt file
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clean_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clean_line.split(':')
        
# Add emotions from cleaned text into a list
        if word in final_words:
            emotion_list.append(emotion)

# Count frequency of emotions
emotion_count = Counter(emotion_list)

# Display histogram of emotions
fig,ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
