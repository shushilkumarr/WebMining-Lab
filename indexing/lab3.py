from pprint import pprint

index = {}

def preprocess(words):
    for i in range(len(words)):
        word = words[i].strip()
        if not word[0].isalnum():
            word = word[1:]
        if not word[-1].isalnum():
            word = word[:-1]
        words[i] = word.lower()
    return words

def getoffsets(words, word):
    offsets = []
    for i in range(len(words)):
        if words[i]==word:
            offsets.append(i)
    return offsets

def createindex(doc, doc_id):
    words = doc.split(' ')
    words = preprocess(words)
    index = {}
    for i in set(words):
        offsets = getoffsets(words, i)
        postings = [(doc_id, offset) for offset in offsets]
        index[i] = [words.count(i), postings]
    return index

files = ['input1.txt', 'input2.txt', 'input3.txt']
doc_id = 0
for file in files:
    doc_id += 1
    content = None
    with open(file, 'r') as content_file:
        content = content_file.read()
    doc_index = createindex(content, doc_id)
    for key in doc_index.keys():
        if key in index.keys():
            index[key][0] += doc_index[key][0]
            index[key][1] += doc_index[key][1]
        else:
            index[key] = doc_index[key]

pprint(index)


    
    
    
