from pprint import pprint
import statistics

def vectorize(doc,terms):
    docvector=[]
    count=0
    #print(doc.lower().rsplit(" ",500))
    for i in range(len(terms)):
        docvector.append(0)
        for syn in terms[i]:
            docvector[i]+=doc.lower().split(" ",500).count(syn.lower())
    return docvector

def calcDist(a,b):
    dist=0
    for x, y in zip(a,b):
        dist+=(x-y)**2
    return round(dist**0.5,4)

def distInit(mat,n):
    for i in range(n):
        mat.append([0 for j in range(n)])
    return None

def findMin(distMat):
    minval=float('inf')
    for i in range(len(distMat)):
        for j in range(len(distMat)):
            if(i==j):
                continue
            if(minval>distMat[i][j] and distMat[i][j]!=0):
                minval=distMat[i][j]
    return minval

def findMax(distMat):
    maxval=float('-inf')
    for i in range(len(distMat)):
        for j in range(len(distMat)):
            if(i==j):
                continue
            if(maxval<distMat[i][j] and distMat[i][j]!=0):
                maxval=distMat[i][j]
    return maxval

def cluster(index1,index2,nei,dlist,clist):
    found=0
    if nei[index1]!='':
        index2=nei[index1][0]
    else:
        addCluster(index1,dlist,clist)
        return None
    if(clist==[]):
        clist.append([index1,index2])
    else:
        for clus in clist:
            if(index1 in clus or index2 in clus):
                found=1
                if(index2 not in clus):
                    if(nei[index2][1]==nei[index1][1]):
                        clus.append(index2)
                    elif nei[index2][1]>nei[index1][1]:
                        addCluster(index2,dlist,clist)
                if(index1 not in clus):
                    if(nei[index1][1]==nei[index2][1]):
                        clus.append(index1)
                    elif nei[index1][1]>nei[index2][1]:
                        addCluster(index1,dlist,clist)
        if(found==0):
            #print('appending..')
            clist.append([index1,index2])
    return None

def addCluster(index,dlist,clist):
    for clus in clist:
        if index in clus:
            return None
    clist.append([index])
    return None

def vectorAvg(a):
    center=[0 for i in range(len(a[0]))]
    for vec in a:
        center=list(map(sum,zip(center,vec)))
    n=len(a)
    center[:]=[round(x/n,3) for x in center]
    return center

def nearClustering(docvectors,ite=1):
    print("level: ",ite," clustering")
    distMat=[]
    n=len(docvectors)
    distInit(distMat,n)
    for i in range(n):
        for j in range(i+1,n):
            dist=calcDist(docvectors[i],docvectors[j])
            distMat[i][j]=dist
            distMat[j][i]=dist
    #print("\ndistance mat:")
    #pprint(distMat)
    print("\nvectors to cluster:")
    pprint(docvectors)
    groups=[]
    d=(findMin(distMat)+findMax(distMat))/2
    print("\navg  dist=",d)
    for i in range(n):
        groups.append([i])
        for j in range(n):
            if i!=j:
                if distMat[i][j]<=d:
                    groups[i].append(j)
    #print(groups)
    nei=[]
    for i in range(len(groups)):
        nei.append("")
        mindist=float("inf")
        for j in groups[i]:
            if mindist>distMat[i][j] and i!=j and distMat[i][j]!=0:
                mindist=distMat[i][j]
                nei[i]=(j,mindist)
    #print(nei)
    clusterlist=[]
    for i in range(n):
        #print("i=",i)
        minval=float('inf')
        for j in range(n):
            if(i==j):
                continue
            if(distMat[i][j]<minval):
                minval=distMat[i][j]
                #print("minval:",minval)
        for j in range(n):
            if(i!=j):# and distMat[i][j]<=d):
                #"""if(distMat[i][j]==minval):
                 #   #print("minval:",minval,"i=",i)
                  #  if(minval==findMin(distMat) or minval==0):
                        #print('clustering..',i,' ',j)"""
                cluster(i,j,nei,doclist,clusterlist)
#"""                    else:
                        #print('addind...',i)
                       # addCluster(i,doclist,clusterlist)#"""
        #"""if(minval>d):
         #       addCluster(i,doclist,clusterlist)"""
    print("\nclusters formed:")
    pprint(clusterlist)
    newlist=[]
    for clus in clusterlist:
        vec=[docvectors[i] for i in clus]
        center=vectorAvg(vec)
        newlist.append(list(center))
    print("\ncentroid of the new clusters:")
    pprint(newlist)
    print('*'*50)
    if(len(newlist)>1):
        nearClustering(newlist,ite+1)
    return None
def distInitknn(mat,n,k):
    for i in range(n):
        mat.append([0 for j in range(k)])
    return None
def kMean(docvectors,centroids,k=2,prev=[],n=1):
    print("\niteration: ",n,"\n")
    cluster=[]
    distMat=[]
    print("\ncentroid vectors:\n")
    pprint(centroids)
    print("\ndoc vectors:\n")
    pprint(docvectors)
    
    veclen=len(docvectors)
    distInitknn(distMat,veclen,k)
    genDistMat(distMat,docvectors,centroids)
    for i in range(k):
        cluster.append([i])
    if prev==[]:
        for i in range(k,len(docvectors)):
            cluster[i%k].append(i)
    else:
        for i in range(k,veclen):
            cluster[getMinIndex(i,distMat)].append(i)
    newcentroid=[]
    print("cluster formed:\n",cluster)
    
    for clus in cluster:
        vec=[docvectors[i] for i in clus]
        center=vectorAvg(vec)
        newcentroid.append(list(center))
    print("\nnew centroids:\n")
    pprint(newcentroid)
    print("*"*50)
    if cluster!=prev:
        kMean(docvectors,newcentroid,k,cluster,n+1)
    return None
def calcManDist(a,b):
    dist=0
    for x,y in zip(a,b):
        dist+=abs(x-y)
    return dist
def genDistMat(distMat,docvectors,centroids):
    for i in range(len(docvectors)):
        for j in range(len(centroids)):
            dist=calcManDist(docvectors[i],centroids[j])
            distMat[i][j]=dist
    return None
def getMinIndex(i,mat):
    mindist=float("inf")
    minindex=0
    for j in range(len(mat[i])):
        if mindist>mat[i][j]:
            mindist=mat[i][j]
            minindex=j
    return minindex
terms=[['automotive'],['car','cars'],['motorcycles','motorcycle'],['self-drive'],['IoT'],['hire'],['dhoni']] #list of list of synonyms/same words like 'car' and 'cars' are same

doc1='Electric automotive maker Tesla Inc. is likely to introduce its products in India sometime in the summer of 2017'
doc2='Automotive major Mahindra likely to introduce driverless cars'
doc3='BMW plans to introduce its own motorcycles in india'
doc4='Just drive, a self-drive car rental firm uses smart vehicle technology based on IoT'
doc5='Automotive industry going to hire thousands in 2018'
doc6='Famous cricket player  Dhoni brought his priced car Hummer which is an SUV'
doc7='Dhoni led india to its second world cup victory'
doc8='IoT in cars will lead to more safety and make driverless vehicle revolution possible'
doc9='Sachin recommended Dhoni for the indian skipper post'

docvectors=[]
doclist=[doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8,doc9]
for doc in doclist:
    docvectors.append(vectorize(doc,terms))
k=4
kMean(docvectors,docvectors[:k],k)

print("\n\npart B:")

files = ['doc1.txt', 'doc2.txt', 'doc3.txt', 'doc4.txt','doc5.txt', 'doc6.txt', 'doc7.txt', 'doc8.txt', 'doc9.txt','doc10.txt','doc11.txt','doc12.txt']
terms=[['tesla',"tesla's"], ['electric'], ['car','cars','vehicle','vehicles','automobile','automobiles'],['pollution'], ['demonetisation','de-monetisation'], ['gst'], ['black-money']]
docvectors=[]
for fname in files:
    file=open(fname,'r')
    doclines=file.read().split('.')
    doc=''
    for line in doclines:
        doc+=" "+str(line)
    docvectors.append(vectorize(doc,terms))
kMean(docvectors,docvectors[:k],k)

