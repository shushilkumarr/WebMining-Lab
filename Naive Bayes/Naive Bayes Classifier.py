
# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Finds the probabilities for all the target labels

def NBC(condition, target, data):
    
    n = df.shape[0]
    
    classes = df[target].unique()
    prob = {}
    for i in classes:
        p = df.loc[df[target]==i].shape[0]/n
        prob[i]= round(p, 3)

    for feature in condition.keys():
        for i in classes:
            df2 = df.loc[df[target]==i]
            df3 = df2.loc[df[feature]==condition[feature]]
            x = df3.shape[0]
            y = df2.shape[0]
            if x==0:
                x += 1
                y += 1
            p = x/y
            prob[i] *= p
            prob[i] = round(prob[i], 3)

    result = None
    max_prob = 0
    
    print('Probabilities:\n', prob)

    for i in classes:
        if prob[i]>max_prob:
            result = i
            max_prob = prob[i]

    print('\nCondition classified in:\n', result)


# In[3]:


# Reading data for part 1

df = pd.read_csv('nbc.csv')
print(df.head(14))


# In[4]:


# Setting neccessary conditions for classification

condition = {
    'Age': '<=30',
    'Income': 'Medium',
    'Student': 'Yes',
    'Credit_rating': 'Fair'
}

target = 'Buys_computer'

NBC(condition, target, df)


# In[5]:


# Reading data for part 2

df = pd.read_csv('data2.csv')
df.head(10)


# In[6]:


# Modifying from continuous to categorical data

df = df.applymap(str)
for attr in df.columns[:-1]:
    df.loc[df[attr] > '3', attr] = 'high'
    df.loc[df[attr] <= '3', attr] = 'low'
df.head(10)


# In[7]:


# Setting necessary conditions for classification

condition = {
    'TDP': 'low',
    'Nifty': 'low',
    'Sidhu': 'low',
    'BJP': 'low',
    'Sensex': 'high',
    'Sixer': 'low',
    'Congress': 'low',
    'Century': 'low',
}

target = 'Category'

NBC(condition, target, df)

