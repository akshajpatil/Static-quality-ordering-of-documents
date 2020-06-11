
# coding: utf-8

# In[75]:

import math
def calculateIdf(df):
    dictIdf={}
    for keys in df:
        dictIdf[keys]=(19997/(1+df[keys]))
    return dictIdf


def calculateCosineScore(queryVectorTemp,docVectorTemp):
    cosineScore=0
    deno1=0
    deno2=0
    for i in range(len(queryVectorTemp)):
        cosineScore=cosineScore+queryVectorTemp[i]*docVectorTemp[i]
    for nums in queryVectorTemp:
        deno1=deno1+nums*nums
    deno1=math.sqrt(deno1)
    for nums in docVectorTemp:
        deno2=deno2+nums*nums
    deno2=math.sqrt(deno2)
    deno1=deno1*deno2
    
    cosineScore=cosineScore/(deno1+1)
    return cosineScore


def calculateCosine(num):
    #print(queryList)
    dictScoreCosine={}
    k=num

    
    for terms in queryList:
#         if num<=0:
#             break
        queryVector=[]
        docVector=[]
        cosineScore=0
        #num=k
        if terms not in highListDic:
            highListDic[terms]={}
            lowListDic[terms]={}
            
        for keys in highListDic[terms]:
            if terms not in dictIdf.keys():
                dictIdf[terms]=0
            scoreQuery=0
            scoreDoc=0


            scoreDoc=float(math.log(1+highListDic[terms][keys])/lengthDic[keys])*dictIdf[terms]

            if keys not in dictScoreCosine:
                dictScoreCosine[keys]=scoreDoc
                num=num-1
            else:
                dictScoreCosine[keys]=scoreDoc+dictScoreCosine[keys]

    print(len(dictScoreCosine))       
    if k>len(dictScoreCosine):
        print("In Lowlist")
        for terms in queryList:
    #         if num<=0:
    #             break
           # num=k-len(dictScoreCosine)
            queryVector=[]
            docVector=[]
            cosineScore=0


            for keys in lowListDic[terms]:
    #             if(num<=0):
    #                 break
                if terms not in dictIdf.keys():
                    dictIdf[terms]=0
                scoreQuery=0
                scoreDoc=0


                scoreDoc=float(math.log(1+lowListDic[terms][keys])/lengthDic[keys])*dictIdf[terms]

                if keys not in dictScoreCosine:
                    dictScoreCosine[keys]=scoreDoc
                    num=num-1
                else:
                    dictScoreCosine[keys]=scoreDoc+dictScoreCosine[keys]

            
        


        
    for keys in dictScoreCosine:
        dictScoreCosine[keys]=dictScoreCosine[keys]/lengthDic[keys]+float(gdDict[str(keys)])/float(maxGd)
   
    dictScoreCosine=dict( sorted(dictScoreCosine.items(), key=operator.itemgetter(1),reverse=True))

    
    for keys in dictScoreCosine:
        if(k==0):
            break
        print(keys,": and Score= ",dictScoreCosine[keys])
        k=k-1




# In[2]:

gdFile=open(r"E:/E/IIIT Delhi/IR/Assign3/file.txt")
gdDict={}
totalText=gdFile.readlines()
gdlist=[]
for lines in totalText:
    inputLine=lines.split(" ")
    TempinputLine=inputLine[1].split("\n")
    inputLine[1]=TempinputLine[0]
    gdDict[inputLine[0]]=int(inputLine[1])
    gdlist.append(int(inputLine[1]))
    
maxGd=max(gdlist)
print(gdDict["8"])


# In[3]:

import glob
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from num2words import num2words
lemmatizer=WordNetLemmatizer()
path="E:/E/IIIT Delhi/IR/Assign 1/20_newsgroups/temp/alt.atheism"
j=1
k=1

direDict={}
dictWords={}
globalList={}
globalDocNames=[]
lengthDic={}
df={}
direct = [f for f in sorted(glob.glob("E:/E/IIIT Delhi/IR/Assign3/20_newsgroups/*", recursive=True))]
for d in direct:
    files = [f for f in glob.glob(d+"/*", recursive=True)]
    filesRead={}
    i=1
    
    tokenizer = RegexpTokenizer(r'\w+')
    for f in files:
        list1=[]
        list2=[]
        fileRead = open(f, "r")
        input_str=fileRead.read().translate(str.maketrans("","",string.punctuation))
        input_str=tokenizer.tokenize(input_str.lower())
        #input_str = input_str.lower()
        #input_str=list(set(input_str))
        pattern='[0-9][a-z]|[0-9]'
        #input_str = [re.sub(pattern, '', j) for j in input_str]
        #input_str = str(input_str).translate(string.maketrans('',''), string.punctuation)
        #input_str = str(input_str).strip()

        stop_words = set(stopwords.words('english'))
        #from nltk.tokenize import word_tokenize
        #tokens = word_tokenize(str(input_str))
        result = [i for i in input_str if not i in stop_words]
        #list1=[word.strip(string.punctuation) for word in result]
        list1=result
        
        for word in list1:
            if word.isdecimal():
                word1=lemmatizer.lemmatize(word)
                #print(fileName," ",word)
                list2.append(num2words(word1))
            
            else:
                list2.append(lemmatizer.lemmatize(word))

        
        #list2.remove("")
        filesRead[i]=list(set(list2))
        for words in filesRead[i]:
            if words not in dictWords.keys():
                
                dictWords[words]={}
                dictWords[words][k]=list2.count(words)
                globalList[words]={}
                globalList[words][k]=gdDict[str(k)]
            else:
                
                dictWords[words][k]=list2.count(words)
                globalList[words][k]=gdDict[str(k)]
            
        
        tempListTokens=list(set(list2))
        for tokens in tempListTokens:
            if tokens not in df:
                df[tokens]=1
            else:
                df[tokens]=df[tokens]+1
        
        lengthDic[k]=len(list2)
        globalDocNames.append(k)
        i=i+1
        k=k+1
   # print(filesRead)
    
    direDict[j]=filesRead
    print(j)
    j=j+1
    
    
dictIdf=calculateIdf(df)
print(len(direDict))
print(len(dictWords))
print(len(globalList))
print(len(globalDocNames))


# In[4]:

import operator
for keys in dictWords:
    dictWords[keys]=dict( sorted(dictWords[keys].items(), key=operator.itemgetter(1),reverse=True))
    globalList[keys]=dict( sorted(globalList[keys].items(), key=operator.itemgetter(1),reverse=True))


# In[95]:

idflist=list(dictIdf.values())
print(max(idflist))
aMIdf=sum(idflist)/len(idflist)
print(aMIdf)
rareterms=[]
for terms in dictIdf:
    if dictIdf[terms]>aMIdf:
        rareterms.append(terms)
print(len(rareterms))
print(len(dictIdf))


# In[102]:

# import statistics
# vocab=list(dictWords.keys())
# highListDic={}
# lowListDic={}
# i=0
# for words in vocab:
#     if words in rareterms:
#         hm=statistics.harmonic_mean(list(dictWords[words].values()))
#         r = len([i for i in list(dictWords[words].values()) if i > hm]) 
#     else:
#         am=sum(list(dictWords[words].values()))/len(dictWords[words])
#         r=len([i for i in list(dictWords[words].values()) if i > am]) 
    
#     highListDic[words]=dict(list(dictWords[words].items())[0:r])
#     lowListDic[words]=dict(list(dictWords[words].items())[r:])
#     i+=1
#     if i%20000==0:
#         print(i)

#### Here r is consider by calculating harmonic and arithmetic mean.


# In[110]:

vocab=list(dictWords.keys())
highListDic={}
lowListDic={}

for words in vocab:
    highListDic[words]=dict(list(dictWords[words].items())[0:25]) # Here R can be considered as static value 25.
    lowListDic[words]=dict(list(dictWords[words].items())[25:])

# pickle_out = open("E:/E/IIIT Delhi/IR/Assign3/high-list.pickle","wb")
# pickle.dump(highListDic, pickle_out)

# pickle_out = open("E:/E/IIIT Delhi/IR/Assign3/low-list.pickle","wb")
# pickle.dump(lowListDic, pickle_out)

for words in vocab:
    temphigh=highListDic[words]
    templow=lowListDic[words]
    highListDic[words]={}
    lowListDic[words]={}
    for keys in globalList[words]:
        if keys in temphigh.keys():
            highListDic[words][keys]=temphigh[keys]
        else:
            lowListDic[words][keys]=templow[keys]
    
print(len(highListDic["wrote"]))
print(len(lowListDic["wrote"]))
#print("\n",globalList["wrote"])


# In[112]:

query=input("Enter Query: ")
#query="gnuplot, etc. make it easy to plot real valued functions of 2 variables."
print(query)
query=query.translate(str.maketrans("","",string.punctuation))
query=word_tokenize(query.lower())
result = [i for i in query if not i in stop_words]
#result=query   
queryList=[]  
#result=[word.strip(string.punctuation) for word in result]
for word in result:
    word=lemmatizer.lemmatize(word)
    if word.isdecimal():
        queryList.append(num2words(word))
    else:
        queryList.append(word)

print("Querylist= ",queryList)
k=input("Enter number of docs you wanna retrive")
calculateCosine(int(k))


# In[84]:




# In[97]:




# In[35]:




# In[ ]:



