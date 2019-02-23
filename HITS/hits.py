def getinlinks(page,graph):
        links=[i for i in range(len(graph)) if graph[i][page]==1]
        return links
def getoutlinks(page,graph):
        links=[i for i in range(len(graph)) if graph[page][i]==1]
        return links

def initSc(n):
        hubSc=[1 for i in range(n)]
        return hubSc
def norm(sc):
        sc_temp=[0 for i in range(len(sc))]
        for i in range(len(sc)):
                sc_temp[i]=sc[i]/sum(sc)
        return sc_temp

def calcSc(sc,graph):
        sc1=[0 for i in range(len(sc))]
        for i in range(len(sc)):
                sc1[i]=0
                inlinks=getinlinks(i,graph)
                for j in inlinks:
                        sc1[i]+=sc[j]
        return sc1
def calchubSc(sc,graph):
        sc1=[0 for i in range(len(sc))]
        for i in range(len(sc)):
                sc1[i]=0
                outlinks=getoutlinks(i,graph)
                for j in outlinks:
                        sc1[i]+=sc[j]
        return sc1

def hits(itr,graph):
        hubSc=initSc(len(graph))
        for i in range(itr):
                authSc=calcSc(hubSc,graph)
                authSc=norm(authSc)
                hubSc=calchubSc(authSc,graph)
                hubSc=norm(hubSc)
                print("\n"*3,"iteration ",i+1,"\n")
                print("\nhubSc:\n",hubSc)
                print("\nauthSc:\n",authSc)
        return hubSc,authSc

def generateMatrix(keys,graph_dict):
        graph_mat=[[0 for i in range(len(keys))] for _ in range(len(keys))]
        for key in keys:
                links=graph_dict[key]
                index=keys.index(key)
                for link in links:
                        graph_mat[index][keys.index(link)]=1

        return graph_mat

def printSc(Sc,keys):
        for key in keys:
                print(key,":",Sc[keys.index(key)])
        return None
graph=[[0,1,1,1,0],
                [1,0,1,1,0],
               [0,0,0,1,0],
               [0,0,1,0,1],
               [0,1,1,1,0]]
hubSc,authSc=hits(5,graph)
print("\n\n","*"*80,"\n\n")
graph2 = { "home" : ["about","product","links"],
          "about" : ["home"],
          "product" : ["home"],
          "links" : ["extA","extB","extC","extD","revA","revB","revC","revD"],
          "extA" : [],
          "extB" : [],
          "extC" : [],
          "extD" : [],
          "revA" : ["home"],
          "revB" : ["home"],
          "revC" : ["home"],
          "revD" : ["home"]
        }

keys=graph2.keys()
graph2_mat=generateMatrix(list(keys),graph2)

hubSc,authSc=hits(5,graph2_mat)
print("\nhubSc:\n\n")
printSc(hubSc,list(keys))
print("\n\nauthSc:\n")
printSc(authSc,list(keys))
print("\nsum of hub: ",sum(hubSc))
print("sum of auth ",sum(authSc))


