
# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


# Initializing the start URL and inverted index structure
start_url = 'http://www.vit.ac.in/'
invindex = {}


# In[3]:


# Extract links from the 'url' and modify the inverted index accordingly.
def getlinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    for anchor in soup.find_all('a'):
        link = anchor.get('href')
        # Discarding empty tags
        if(link == '#' or link == '' or link == None):
            continue
        # Converting relative URLs to absolute URLS
        if(link.find('http')==-1):
            link = url[:-1]+link
        # Creating a key for 'link' in inverted index
        if link not in invindex.keys():
            invindex[link] = [0, []]
        # Constructing the inverted index for 'link'
        if url not in invindex[link][1]:
            invindex[link][0] += 1
            invindex[link][1].append(url)
        # Discarding document type links
        if(link.find('.doc')>=0 or link.find('.pdf')>=0):
            continue
        # Discarding links except the domain of VIT
        if(link.find('vit')==-1 and link.find('vtop')==-1):
            continue
        links.append(link)
    return links


# In[4]:


# Initializing crawled and queued sets
crawled = set()
queue = set()
queue.add(start_url)


# In[5]:


# Loop to crawl 10 links and update the queued set.
while(len(crawled)!=10):
    url = queue.pop()
    if url in crawled:
        continue
    print("Crawling:" + url)
    links = getlinks(url)
    print('Got {0} URLS.'.format(len(links)))
    crawled.add(url)
    linkset = set(links)
    queue = queue | linkset


# In[6]:


print('Crawled URLS: {0}'.format(len(crawled)))
#for link in crawled:
#    print(link)


# In[7]:


print('Queued URLS: {0}'.format(len(queue)))
#for link in queue:
#    print(link)


# In[11]:


# Printing the inverted index.
for i in invindex.keys():
    print('{} : {}'.format(i, invindex[i][0]))
    for link in invindex[i][1]:
          print('\t {}'.format(link))
    print()

