import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sentences = ['This was a really good book.', 'This movie was so bad.',
             "I like to hate Michael Bay films, but I couldn't fault this one"]

sentences = ['I am so happy with this product.', 'It is fantastic.',
             'I can\'t wait to get another one just like it for my sister.',
             'It\'s super!']

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
	print(sentence)
	ss = sid.polarity_scores(sentence)
	for k in sorted(ss):
		print('{0}: {1}, '.format(k, ss[k]), end='')
	print()

# https://textblob.readthedocs.io/en/dev
# processes text and provides analysis
# can download in anaconda and use in python
    
from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

text = '''
I am so happy with this product. It is fantastic. I can't wait to get another one
just like it for my sister. It's super!
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341


# from Matthew Beck
    text = '''Celebrate #NationalPetDay with our puppy playlist: https://t.co/eBHHFPW0z7 https://t.co/uix5AY2FFQ<a href="http://msande.stanford.edu"> Management Science and Engineering <p class="MsoNormal"

  Address: Terman 311, Stanford CA 94305<br>

  Email: ashishg@cs.stanford.edu<br>

  Phone: (650)814-9999 [Cell], Fax: (650)723-9999<br>

  Admin asst: Roz Morf, Terman 405, 650-723-9999, rozm@stanford.edu</p>
The U.S.A. olympic teams have east-west training centers with up-to-date equipment.

'''
http = re.compile('(http)s?://*')
output = http.findall(text)
print(output)

phone = re.compile('[(]?[0-9]+[)]?[-]?[0-9]+[-][0-9]+')
output = phone.findall(text)
print(output)

email = re.compile('[a-z]+@[a-z]+.[a-z]+.?[a-z]+')
output = email.findall(text)
print(output)

acronyms = re.compile('([A-Z]{2}\s|[A-Z]\.[A-Z]\.[A-Z]\.)')
output = acronyms.findall(text)
print(output)

####################OUTPUT
['http', 'http', 'http']
['(650)814-9999', '(650)723-9999', '650-723-9999']
['ashishg@cs.stanford.edu', 'rozm@stanford.edu']
['CA ', 'U.S.A.']

