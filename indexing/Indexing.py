
# In[1]:


# Importing necessary modules
from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup


# In[2]:


# Preprocessing a list of words of a document
def preprocess(words):
    for i in range(len(words)):
        word = words[i].strip()
        if not word[0].isalnum():
            word = word[1:]
        if not word[-1].isalnum():
            word = word[:-1]
        words[i] = word.lower()
    return words

# Get the offsets of a word in a list of words
def getoffsets(words, word):
    offsets = []
    for i in range(len(words)):
        if words[i]==word:
            offsets.append(i)
    return offsets

# Create index of passed document 'doc' based on its 'doc_id'
def createindex(doc, doc_id):
    words = doc.split(' ')
    words = [word for word in words if word!='']
    words = preprocess(words)
    index = {}
    for i in set(words):
        offsets = getoffsets(words, i)
        postings = [doc_id, offsets]
        index[i] = [words.count(i), [postings]]
    return index

# Merge the doc_index and index
def appendindex(doc_index, index):
    for key in doc_index.keys():
        if key in index.keys():
            index[key][0] += doc_index[key][0]
            index[key][1] += doc_index[key][1]
        else:
            index[key] = doc_index[key]
    return index

# Print the index in tabular format
def printindex(index):
    table = PrettyTable(['Word', 'Frequency', 'Postings'])
    for word in sorted(index.keys()):
        frequency, postings = index[word][0], index[word][1]
        table.add_row([word, frequency, postings])
    print(table)


# In[3]:


# Create the index of sample input files
index = {}
files = ['input1.txt', 'input2.txt', 'input3.txt']
doc_id = 0
for file in files:
    doc_id += 1
    content = None
    with open(file, 'r') as content_file:
        content = content_file.read()
    doc_index = createindex(content, doc_id)
    index = appendindex(doc_index, index)


# In[4]:


printindex(index)


# In[5]:


# Create the index of four of Robert Frost's poems
index = {}
links = ['https://www.poemhunter.com/poem/the-road-not-taken/', 'https://www.poemhunter.com/poem/stopping-by-woods-on-a-snowy-evening-2/', 'https://www.poemhunter.com/poem/nothing-gold-can-stay/', 'https://www.poemhunter.com/poem/a-question/']


# In[6]:


for id in range(len(links)):
    link = links[id]
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    poem = str(soup.find_all('p')[1])
    poem = poem[4:-4].replace('<br/>', ' ').strip()
    print('Parsed poem #{}:\n{}\n'.format(id, poem))
    poem_index = createindex(poem, id)
    index = appendindex(poem_index, index)


# In[7]:


for word in sorted(index.keys()):
    freq, postings = index[word][0], index[word][1]
    print('{}: {}'.format(word, freq))
    for i in postings:
        print('\t{}'.format(i))
    print()

