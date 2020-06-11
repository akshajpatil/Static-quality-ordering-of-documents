
# coding: utf-8

# In[132]:

file=open("E:/E/IIIT Delhi/IR/Assign3/Q2.txt")
text=file.readlines()
sortedValidList=[]
url=[]
for lines in text:
    templist=lines.split(" ")
    if templist[1]!="qid:4":
        break
    temp=[]
    temp.append(int(templist[0]))
    temp.append(templist[1])
    temp1=templist[76].split(":")
    temp.append(float(temp1[1]))
    sortedValidList.append(temp)
    url.append(lines)
#print(len(validList))
validList=[]
for lists in sortedValidList:   
    validList.append(lists)


# In[135]:

import math
def calculateDCG(datalist):
    dcg=0
    i=1
    for lists in datalist:
        rel=int(lists[0])
        dcg=dcg+(pow(2,rel)-1)/math.log(i+1,2)
        i=i+1
    return dcg

def calculateNDCG(n):
    templist=[]
    n1=n
    for lists in validList:
        templist.append(lists)
        n=n-1
        if n <= 0:
            break
        
    
    #print(len(templist))
    dcg=calculateDCG(templist)
    #print("dcg=",dcg)
    #templist.sort(reverse=True)
    #print(datalist[:3])
    dcgMax=calculateDCG(sortedValidList[:n1])
    #print("MaxDcg at ",n1,"=",dcgMax)
    ndcg=dcg/dcgMax
    return ndcg


    
sortedValidList.sort(reverse=True)
#print(sortedValidList[:50])
dcg=calculateDCG(sortedValidList)
print("Maxdcg =",dcg)
ndcg=calculateNDCG(50)
print("ndcg-@-50 =",ndcg)
ndcg=calculateNDCG(len(validList))
print("ndcg-total =",ndcg)


# In[142]:

import matplotlib.pyplot as plt
def calculatePreRec():
    i=1
    numRel=0
    for lists in validList:
        if lists[0]!=0:
            numRel+=1
    
    numRelCurr=0
    for lists in validList:
        if lists[0]!=0:
            numRelCurr+=1
        pre=numRelCurr/i
        rec=numRelCurr/numRel
        preList.append(pre)
        recList.append(rec)
        i=i+1
        
def plotGraph():
    plt.plot(x, preList, label = "Precision")
    plt.plot(x, recList, label = "Recall")
    plt.legend()
    plt.show()
    
def plotPreRecCurve():
    plt.plot(recList, preList)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()
    plt.show()


# In[143]:

validList.sort(key = lambda x: x[2],reverse=True)
preList=[]
recList=[]
calculatePreRec()
# print((preList))
# print((recList))
x=[]
for i in range(len(validList)):
    x.append(i)
plotGraph()
plotPreRecCurve()


# In[147]:

three=0
two=0
one=0
zero=0
for lists in validList:
    if lists[0]==0:
        zero+=1
    elif lists[0]==1:
        one+=1
    elif lists[0]==2:
        two+=1
    else:
        three+=1

zerofac=0
for i in range(zero+1):
    zerofac=zerofac+(math.factorial(59)/math.factorial(59-i))
print(three,two,one,zero)
ans=zerofac*math.factorial(one)*math.factorial(two)*math.factorial(three)+(math.factorial(one)*math.factorial(two)*math.factorial(three))
print(ans)


# In[148]:

print(len(url))
url.sort(reverse=True)
#print(url[:10])
f1=open("E:/E/IIIT Delhi/IR/Assign3/Q2-1.txt","a")
for lines in url:
    f1.write(lines)

f1.write("\n\n\n And Total number of combinations are "+str(ans))    
f1.close()



# In[ ]:



