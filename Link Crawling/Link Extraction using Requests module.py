
# In[1]:


# Importing the requests module and re module for regular expressions
import requests
import re


# In[2]:


# This method find the links in an HTML page using regular expressions and returns them as a list.
def getlink(code):
    links = re.findall('"((http|ftp)s?://.*?)"',  code)
    links = [i[0] for i in links]
    return links


# In[3]:


# Separate out the 'img' tag from HTML code and then use getlink() to extract image links from each img tag.
def findimg(code):
    links = []
    start = 0
    while(start != -1):
        start = code.find('<img')
        end = code.find('>', start)
        tag  = code[start:end+1]
        link = getlink(tag)
        links.append(link)
        code = code[end+1:]
    return links


# In[4]:


# Fetching a web page and storing its metadata
page = requests.get('https://towardsdatascience.com/getting-started-with-graph-analysis-in-python-with-pandas-and-networkx-5e2d2f82f18e')
print(page)


# In[5]:


# Get all the links in webpage using getlink() and print them.
alllinks = getlink(page.text)
print('All the links are ' + str(len(alllinks)) + ' :')
for link in alllinks:
    print(link)


# In[6]:


# Get all the links in webpage using findimg() and print them.
imglinks = findimg(page.text)
print('All the image links are ' + str(len(imglinks)) + ' :')
for link in imglinks:
    if len(link):
        print(link[0])

