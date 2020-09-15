# Save for Later
# Example in shape - not working well!
        
imageFile = "/Users/joycewoznica/Syracuse/IST652/Project/images/racingShadow.png"
imageFile = "/Users/joycewoznica/Syracuse/IST652/Project/images/horse1.png"
maskArray = npy.array(Image.open(imageFile))

def create_word_cloud(string, maskA):
   word_cloud = WordCloud(collocations=False, background_color = "white", max_words = 175, colormap = "Dark2",
                          prefer_horizontal = 0.8,
                          mask = maskA, stopwords = stopwords).generate(string)
   plt.figure(figsize=(15,10),facecolor = 'white', edgecolor='blue')
   plt.imshow(word_cloud)
   plt.axis('off')
   plt.tight_layout(pad=0)
   plt.show()

create_word_cloud(final_text_ruling, maskArray)

filtered_text_ruling = [word for word in final_text_ruling.split() if word not in stopwords]
counted_word_ruling = collections.Counter(filtered_text_ruling)

word_count_ruling = {}

for letter, count in counted_word_ruling.most_common(100):
    word_count_ruling[letter] = count
    
for i,j in word_count_ruling.items():
        print('Word: {0}, count: {1}'.format(i,j))