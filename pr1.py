#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data1=pd.read_csv("Credit Bankingm.csv")
data1


# In[3]:


data2=pd.read_csv("Credit Bankingms.csv")
data2


# In[4]:


data3=pd.read_csv("Credit Bankingmss.csv")
data3


# In[5]:


data1=pd.read_csv("Credit Bankingm.csv")
data1.shape


# In[6]:


data2=pd.read_csv("Credit Bankingms.csv")
data2.shape


# In[7]:


data3=pd.read_csv("Credit Bankingmss.csv")
data3.shape


# In[8]:


data1.describe()


# In[9]:


data1=pd.read_csv("Credit Bankingm.csv")
mask=data1['Age']<18
data1[mask]


# In[10]:


import numpy as np
import pandas as pd
data1=pd.read_csv("Credit Bankingm.csv")
data1['Segment'].value_counts()


# In[11]:


data1=pd.read_csv("Credit Bankingm.csv")
mask=data1['Age']<18
array1=data1[mask]['Age'].values


# In[12]:


import numpy as np
import pandas as pd
data1=pd.read_csv("Credit Bankingm.csv")
mask=data1['Age']<18
array1=data1[mask]['Age']
l=data1[mask]['Age'].values.mean()
# n=len(array1)
# for i in range(n):
#    data1['Age'].replace('data1[mask]['Age'][i]','l',inplace=True)
# l
# # n=len(array1)
# # for i in range(n):
# # array1.replace('array1.values[i]','l')
# n=len(array1)
# array1.values[0:n]=[l]
# array1
# data1[mask]['Age']=array1
# # array1
data1.loc[data1['Age']<18,'Age']=l


# In[13]:


data1


# In[14]:


data3=pd.read_csv("Credit Bankingmss.csv")
dt_col=pd.DatetimeIndex(data3['Month'])
data3['Year']=dt_col.year
data3['Mth']=dt_col.month
data3


# In[15]:


Costomers=data3.groupby(['Costomer','Mth','Year'])


# In[16]:


df1=Costomers.Amount.agg("sum")
df1


# In[17]:


import numpy as np
import pandas as pd
# data1=pd.read_csv("Credit Bankingm.csv")
data2=pd.read_csv("Credit Bankingms.csv")
dt_col=pd.DatetimeIndex(data2['Month'])
data2['Year']=dt_col.year
data2['Mth']=dt_col.month
data2
Costomers=data2.groupby(['Costomer','Mth','Year'])

df2=Costomers.Amount.agg("sum")
df2


# In[18]:


df3=pd.merge(df1,df2,on=["Costomer","Mth","Year"])
df3


# In[19]:


# dt4=pd.merge(df3,data1,on="Costomer")
# dt4
# data1=pd.merge(df2,data1,on="Costomer")
data3


# In[20]:


data1.rename(columns={'Customer':'Costomer'},inplace=True)


# In[21]:


data1=pd.read_csv("Credit Bankingm.csv")
mask=data1['Age']<18
array1=data1[mask]['Age']
l=data1[mask]['Age'].values.mean()
data1.loc[data1['Age']<18,'Age']=l


# In[22]:


data1.rename(columns={'Customer':'Costomer'},inplace=True)
dt4=pd.merge(df3,data1,on="Costomer")
dt4


# In[23]:


dt4.rename(columns={'Amount_x':'Monthly_Repayment','Amount_y':'Monthly_Spent'},inplace=True)


# In[24]:


dt4


# In[25]:


df3.rename(columns={'Amount_x':'Monthly_Repayment','Amount_y':'Monthly_Spent'},inplace=True)


# df3

# In[26]:


df3['Limit']=df3['Monthly_Repayment']-df3['Monthly_Spent']


# df3

# In[27]:


df3


# In[28]:


df3.loc[df3['Limit']<0,'Limit']=0
df3.loc[df3['Limit']>0,'Limit']=1


# df3

# In[29]:


df3


# In[30]:


Lim=dt4[
    ["Costomer","Limit"]]
Lim


# In[31]:


# lo.loc[lo['Limit_x']==1,'Limit_y']=lo['Limit_y']+9
# lo["Limit_y"][0]


# In[32]:





# In[61]:


lo=df3.merge(Lim,on='Costomer')
lo


# In[63]:


h=dt4


# In[64]:


h


# In[65]:


p=h.sort_values(by=["Monthly_Repayment"],ascending=False)


# In[66]:


p.head(10)


# In[67]:


s=dt4
s


# In[68]:


p=s.groupby('Segment')


# In[69]:


p.size()


# In[70]:


p.sum().sort_values("Monthly_Spent",ascending=False)


# In[71]:


k=s.groupby('Age')


# In[72]:


k.size()


# In[73]:


k.sum().sort_values("Monthly_Spent",ascending=False)


# In[74]:


o=p.sum()
o


# In[75]:


o["diff"]=o["Monthly_Spent"]-o["Monthly_Repayment"]


# In[76]:


o


# In[77]:


o.sort_values("diff",ascending=False)


# In[78]:


data2


# In[79]:


data2.groupby('Type')


# In[80]:


data2.groupby('Type').size()


# In[81]:


data2.groupby('Type').sum()


# In[82]:


import numpy as np
import pandas as pd
data2=pd.read_csv("Credit Bankingms.csv")
data2.groupby('Type').sum().sort_values('Amount',ascending=False)


# In[83]:


lo


# In[84]:


lo['Repayment-Spent']=lo['Monthly_Repayment']-lo['Monthly_Spent']


# In[ ]:





# In[85]:


lo


# In[86]:


lo['Credit']=lo['Repayment-Spent']


# In[87]:


lo


# In[97]:


lo['Credit']=lo['Repayment-Spent']>0


# In[98]:


lo


# In[99]:


j=lo


# In[100]:


lo


# In[118]:


lo['Limit_y']=lo['Limit_y'].str.replace(',','')
lo['Limit_y']=lo['Limit_y'].str.replace('INR','')
lo['Limit_y']


# In[119]:


lo['Monthly_Spent']


# In[147]:


lo


# In[ ]:





# In[148]:


lo


# In[149]:


lo['Credit']=lo['Repayment-Spent']>0


# In[150]:


lo


# In[151]:


lo.loc[lo['Credit']==True,'Credit']=lo['Repayment-Spent']
lo.loc[lo['Credit']==False,'Credit']=0


# In[152]:


lo


# In[ ]:


# lo['Limit_y']=lo['Limit_y'].astype('int')
# lo['Credit']=lo['Credit']*lo['Limit_y']*0.02


# In[ ]:




