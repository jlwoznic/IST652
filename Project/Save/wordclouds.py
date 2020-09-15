# wordcloud
#
# To bring the data in:

fields = ['Crime type']

text2 = pd.read_csv('allCrime.csv', usecols=fields)

# To generate the word cloud:

wordcloud2 = WordCloud().generate(text2)
# Generate plot
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()

# However, I get this error:

# TypeError: expected string or bytes-like object

# I was able to create an earlier word cloud from the full dataset, using the following code, 
# but I want the word cloud to only generate words from the specific column, 'crime type' ('allCrime.csv' contains approx. 13 columns):

df = pd.read_csv('allCrime.csv', usecols=fields)

text = df['Crime type'].values 

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# I think this gives an error
text = open('allCrime.csv').read()
wordcloud = WordCloud().generate(text)
# Generate plot
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#-----------------------------------------------------
## Another example:
# Supress Warnings
import warnings
warnings.filterwarnings('ignore')

#loading all necessary libraries
import numpy as np
import pandas as pd

import string
import collections
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.cm as cm
import matplotlib.pyplot as plt
% matplotlib inline

# loading the data file
df = pd.read_csv('emails2.csv')

#shape of the dataframe
print('The shape of the dataframe is :',df.shape)

#first few records
df.head()

#Checking for null values in `description`
df['text'].isnull().sum()

spam1 = df[df.spam == 1]
print(spam1.shape)

spam1['text']= spam1['text'].str.lower()
spam1['text'].head()

all_spam = spam1['text'].str.split(' ')
all_spam.head()

all_spam_cleaned = []

for text in all_spam:
    text = [x.strip(string.punctuation) for x in text]
    all_spam_cleaned.append(text)

all_spam_cleaned[0]

text_spam = [" ".join(text) for text in all_spam_cleaned]
final_text_spam = " ".join(text_spam)
final_text_spam[:500]

wordcloud_spam = WordCloud(background_color="white").generate(final_text_spam)

# Lines 2 - 5
plt.figure(figsize = (20,20))
plt.imshow(wordcloud_spam, interpolation='bilinear')
plt.axis("off")
plt.show()

stopwords = set(STOPWORDS)
stopwords.update(["subject","re","vince","kaminski","enron","cc", "will", "s", "1","e","t"])

wordcloud_spam = WordCloud(stopwords=stopwords, background_color="white", colormap = 'Set1',
                           prefer_horizontal = 0.5, max_font_size=40, max_words=100).generate(final_text_spam)

# Lines 4 to 7
plt.figure(figsize = (15,15))
plt.imshow(wordcloud_spam, interpolation='bilinear')
plt.axis("off")
plt.show()

filtered_words_spam = [word for word in final_text_spam.split() if word not in stopwords]
counted_words_spam = collections.Counter(filtered_words_spam)

word_count_spam = {}

for letter, count in counted_words_spam.most_common(30):
    word_count_spam[letter] = count
    
for i,j in word_count_spam.items():
        print('Word: {0}, count: {1}'.format(i,j))


### Another example
        
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
text = data.Tweet.values
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'black',
    stopwords = STOPWORDS).generate(str(text))
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()        
        

        








