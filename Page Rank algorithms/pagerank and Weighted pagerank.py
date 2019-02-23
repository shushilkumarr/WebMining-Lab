def getnet():
    graph=[]
    pagelinks=[]
    n=int(input("enter no of pages:"))
    for i in range(n):
        pagelinks.clear()
        print("Page:",i)
        m=int(input("enter no of outlinks of page:"))
        for j in range(m):
            pagelinks.append(int(input("enter page no. which it refers to:")))
        graph.append(list(pagelinks))
        printGraph(graph)
    return graph

def printGraph(graph):
    for i in range(len(graph)):
        pagelinks=graph[i]
        print()
        for j in range(len(pagelinks)):
            print(pagelinks[j],end='\t')
    print()
    return None

def win(v,u,graph):
    rv = getinlinks(v,graph)
    ip = [len(getinlinks(p,graph)) for p in rv]
    win = len(getinlinks(u,graph))/sum(ip)
    return win

def wout(v,u,graph):
    rv = getinlinks(v,graph)
    ip = [len(getoutlinks(p,graph)) for p in rv]
    wout = len(getoutlinks(u,graph))/sum(ip)
    return wout

def getoutlinks(page,graph):
    links=[i for i in range(len(graph)) if graph[page][i]==1] 
    return links

def getinlinks(page,graph):
    links=[i for i in range(len(graph)) if graph[i][page]==1] 
    return links


def pagerank(graph,d,n):
    rankPrev=[1 for i in range(len(graph))]
    rank=[0 for i in range(len(graph))]
    for _ in range(n):
        for i in range(len(graph)):
            inlinks=getinlinks(i,graph)
            sigma=0
            for link in inlinks:
                sigma+=rankPrev[link]/len(getoutlinks(link,graph))
            rank[i]=1-d+d*sigma
        rankPrev=list(rank)
    return rank


def weightPR(graph,d,n):
    rankPrev=[1 for i in range(len(graph))]
    rank=[0 for i in range(len(graph))]
    for _ in range(n):
        for i in range(len(graph)):
            inlinks=getinlinks(i,graph)
            sigma=0
            for link in inlinks:
                sigma+=rankPrev[link]*wout(link,i,graph)*win(link,i,graph)
            rank[i]=1-d+d*sigma
        rankPrev=list(rank)
    return rank


    
#graph=getnet()
graph=[[0,1,1,1,0],
       [1,0,1,1,0],
       [0,0,0,1,0],
       [0,0,1,0,1],
       [0,1,1,1,0]]
#print("size of graph",len(graph))
printGraph(graph)
rank=pagerank(graph,0.5,10)
print(sum(rank))

wrank=weightPR(graph,0.25,10)

print(sum(wrank))
