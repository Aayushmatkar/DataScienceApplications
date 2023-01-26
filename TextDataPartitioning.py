import nltk
import os
nltk.download('gutenberg')

folder_path = "/root/nltk_data/corpora/gutenberg"

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        print(filename)
        
        
import nltk
from nltk.corpus import gutenberg
import re
import os,random
import pandas as pd
nltk.download('punkt')



# Function to create partitions of 100 words each
def create_partitions(text, label):
    partitions = []
    words = nltk.word_tokenize(text)

    for c in range(0, len(words)):
        partitions.append((words[c:c+100], label)) 
        c=c+100
    return partitions

#  for i in range(0, len(words), 100):
#  partitions.append((words[i:i+100], label))
#  return partitions

# Sample of a Gutenberg book

#book = input("enter the book name you want to partition")

book = gutenberg.raw('shakespeare-caesar.txt')

bookdeets = input("enter the label you want in classification")

###########################################################
#bookdeets = 'shakespeare-caesar-William Shakespeare-1599'
#authorname = 'William Shakespeare'
#publicationyear = '1599'
###########################################################



# Create partitions of 100 words each
partitions = create_partitions(book, bookdeets)

# Create 200 random samples of the partitions
samples = random.sample(partitions, 200)

#use synonyms for sample and partitions 
# Use regular expressions to clean the data
for r in range(len(samples)):
    samples[r] = (re.sub(r'[^\w\s]','', ' '.join(samples[r][0])), samples[r][1])

# Serialize the data using Pandas
df = pd.DataFrame(samples, columns=['random book sample', 'label'])

df.to_csv('books_in_partition.csv', index=False)


print("partition for the book is exported in books_in_partition.csv.")




bk_name = input("enter the book partition name to be read with .csv")
pd.read_csv(bk_name)


print(df.to_string())
