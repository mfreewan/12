#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter 

import warnings 
warnings.filterwarnings("ignore")
import MetaTrader5 as mt5


# In[121]:


#Read csv File Data 
Data1 = pd.read_csv(r"C:\Users\mfree\Desktop\project csv\icpc-result.csv")


# In[122]:


#Show DataBase Info 
Data1.info


# In[186]:


#Create Class for Histogram database 
def plotHistogram(histo):
    
    plt.figure()
    plt.hist(Data1[histo] , bins = 85 , color= "Orange")
    plt.xlabel(histo)
    plt.ylabel("freekans")
    plt.title("Histogram {}".format(histo))
    plt.show()


# In[187]:


#Show Histogram for 
NewHistogram=["Year" ,"Score Percentage", "Score","Penalty","Rank"]
for i in (NewHistogram):
    plotHistogram(i)
    


# In[76]:


#Describe Data Base
Data1.describe()


# In[104]:


# get dummais of data base
getdummies=Data1.copy()
getdummies=pd.get_dummies(getdummies , columns = ["Gold","Silver"])
getdummies.head(10)


# In[111]:


getdummies.loc[:,["Year","Gold_False", "Gold_True","Silver_False","Silver_True"]].corr()


# In[160]:


#Add get dummais and groub by of data 
df = pd.DataFrame(np.random.randn(10, 5), columns=['Year', 'Rank' ,'Gold' ,'Silver','Penalty'])
pd.get_dummies(df, columns=['Gold','Silver']).groupby(['Year'], as_index=False).sum()


# In[ ]:





# In[184]:


#Scatter for U Waterloo Team 
EindhovenCity=Data1[Data1.City == "Eindhoven"]
EindhovenCity.head(1)


# In[183]:


#Scatter for St. Petersburg IFMO Team 
MarrakechCity=Data1[Data1.City == "Marrakech"]
MarrakechCity.head(1)


# In[66]:


#Scatter for Korea Kaist Tigers Team 
scatter3=Data1[Data1.Team == "Korea Kaist Tigers"]
scatter3.head()


# In[185]:


#Scatter Score , Penalty for Marrakech and Eindhoven
plt.figure()
plt.scatter(EindhovenCity.Score , EindhovenCity.Penalty , alpha=0.9 , label= "Eindhoven	" )
plt.scatter(MarrakechCity.Score , MarrakechCity.Penalty , alpha=0.9 , label= "Marrakech" )
plt.xlabel("Score")
plt.ylabel("Penalty")
plt.title("Scatter team with score and penalty")
plt.legend()
plt.show()


# In[69]:


#PoltBar data base :
def poltBar(deg , n=5):
    Data2=Data1[deg]
    var_value=Data2.value_counts()
    var_value=var_value[:n]
    plt.figure()
    plt.bar(var_value.index , var_value , color="Orange")
    plt.xticks(var_value.index , var_value.index.values)
    plt.xticks(rotation=45)
    plt.ylabel("freekans")
    plt.title("Boltbar Data - {}".format(deg))
    plt.show()
    print("{} : \n {}".format(deg,var_value))
    


# In[72]:


#set Columns for poltBar function
category_deg=["Year","Date","City","Rank","University","Gold","Silver","Bronze","Team","Score","Honorable"]
for i in category_deg:
    poltBar(i)


# In[73]:


#Year boxplot
plt.boxplot(Data1.Year)
plt.title("Year boxplot")
plt.xlabel("Year")
plt.ylabel("0000")
plt.show()


# In[77]:


#Show null data in Score Column
gold=Data1["Score"]
pd.isnull(gold).sum()


# In[80]:


gold_filter= pd.isnull(gold)


# In[81]:


#Filter Data 
Data3=Data1.copy()
Data3=Data3[gold_filter]
Data3.head(5)


# In[83]:


score=Data3["Score"]
score_filter = pd.isnull(score)
Data3=Data3[score_filter]
Data3.head(5)


# In[86]:


Venue=pd.unique(Data1.Venue)
print("Venue Data : {}".format(len(team)))
Venue[:10]


# In[89]:


#Pandas Data Frame for score and penalty
Data4=Data1.copy()
score_penalty=["Score","Penalty"]
for i in Venue :
    filter1=Data4.Venue == "Eindhoven University of Technology"
    filter2=Data4[filter1]
    
for s in score_penalty:
    determine=np.round(np.mean(filter2[s]),2)
    if np.isnan(determine):
        filter2[s]=filter2[s].fillna(determine)
    else :
        filter4=np.round(np.mean(Data1[s]),2)
        filter2[s]=filter2[s].fillna(filter4)
        
Data4[filter1] = filter2

Data5 = Data4.copy()
Data5.info()


# In[142]:


#Create pivot Table 
pivotTable=Data1.pivot_table(index="Penalty" , columns="University" ,
                           values=["Score","Score Percentage","Year"],
                           aggfunc={"Score":np.mean ,"Score Percentage":np.mean,"Year":[min,max,np.std]})
pivotTable.head()


# In[169]:


years=Data1.copy()
years.head(3)


# In[170]:


yearsunique=years.Year.unique()


# In[173]:


array1=np.sort(years.Year.unique())
array1


# In[176]:


plt.figure()
plt.scatter(range(len(array1)),array1)
plt.grid(True)
plt.xlabel("Year")
plt.ylabel("Years")
plt.show()


# In[ ]:


Data6=Data1.loc[]

