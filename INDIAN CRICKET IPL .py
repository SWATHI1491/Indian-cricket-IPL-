#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Install required packages (pandasql)
get_ipython().system('pip install pandasql')


# In[2]:


import pandas as pd
from pandasql import sqldf


# In[ ]:


#Open and view dataset


# In[76]:


df = pd.read_csv("D:\Certificates\SQL Jupyter Notebook\Indian Cricket Auction - IPL\Indian Cricket Auction - IPL.csv", index_col=0)

df.head()


# In[6]:


Base Price


# In[ ]:


#  Data Exploration


# In[7]:


#Total number of rows and columns

print('Total number of Rows: ', df.shape[0])
print('Total number of Columns: ', df.shape[1])


# In[8]:


#Data Types

df.dtypes


# In[11]:


#Total number of Rows
df.shape[0]


# In[13]:


#Total number of Column 
df.shape[1]


# In[23]:


#Retreive Team data

df['Team']


# In[25]:


df = pd.read_csv("D:\Certificates\SQL Jupyter Notebook\Indian Cricket Auction - IPL\Indian Cricket Auction - IPL.csv", index_col=0)

df.head()


# In[27]:


#Retreive types data

df['Type'].unique()


# In[33]:


df = pd.read_csv("D:\Certificates\SQL Jupyter Notebook\Indian Cricket Auction - IPL\Indian Cricket Auction - IPL.csv", index_col=0)

df.head()


# In[36]:


#Retreive all column data 

print(df.columns)


# In[37]:


#Retreive Price data 

df['Price ']


# In[38]:


#Unique Values in 'Base Price' Column

df['Price '].unique()


# In[39]:


#Distribution of values inside column 'Base Price'

df['Price '].value_counts()


# In[40]:


#Retreive type data 

df['Type']


# In[41]:


#Unique Values in 'TYPE' Column

df['Type'].unique()


# In[42]:


#Distribution of values inside column 'Base Price'

df['Type'].value_counts(normalize=True)


# In[ ]:


#Questions to Answer
                     #Top 3 batsman who got paid the most?
                     #Top 5 bowlers who got paid the most?
                     #Highest paid all-rounders?
                     #Average pay for Batsman, Bowler, All-Rounder, Wicket-Keeper?
                      #List of Retained players with Salary?


# In[ ]:


#Data Transformation


# In[43]:


#Rename columns and save it in the variable df2

df2=df.rename(columns={'Player ':'Players',
                       'Price ':'Base_Price',
                       'Type':'Types',
                       'Cost In ? (CR.)':'Cost_INR',
                       'Cost IN $ (000': 'Cost_USD',
                       '2021 Squad':'IPL_2021_Team',
                       'Team':'IPL_2022_Team'})


# In[44]:


#Dropping USD Column

df3 = df2.drop(['Cost_USD'],axis=1)


# In[45]:


#Check updated Dataframe

df3.head()


# In[ ]:


#Setting up mysql function to run queries
#Basics : The main function used in pandasql is sqldf. sqldf accepts 2 parametrs - a sql query string - an set of session/environment variables (locals() or globals())

#Specifying locals() or globals() can get tedious. You can defined a short helper function to fix this.


# In[46]:


mysql = lambda q: sqldf(q, globals())


# In[ ]:


#Question 1 - Name top 3 batsman who got paid the most?


# In[48]:


print(df.columns)


# In[49]:


print(df3.columns)


# In[52]:


mysql = lambda q: sqldf(q, globals())


# In[58]:


mysql("""select * from df3""")


# In[63]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='BATTER' """)


# In[64]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='BATTER' ORDER BY 2 """)


# In[ ]:


#Question 1 - Name top 3 batsman who got paid the most?


# In[66]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='BATTER' ORDER BY 2 DESC LIMIT 3 """)


# In[ ]:


#Question 2 - Name top 5 bowlers who get paid the most?
    #2-Top 5 bowlers who got paid the most?


# In[67]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='BOWLER' ORDER BY 2 DESC LIMIT 5 """)


# In[ ]:





# In[68]:


mysql("""    """)


# In[ ]:


#Question 3 - Name 5 lowest paid wicket-keeper?


# In[69]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='WICKETKEEPER' """)


# In[ ]:


#Question 3 - Name 5 lowest paid wicket-keeper?


# In[73]:


mysql("""select Players, Cost_INR from df3 WHERE Types ='WICKETKEEPER' AND Cost_INR is not null ORDER BY 2 LIMIT 5 """)


# In[ ]:


#Question 4 - What is the Average pay for Batsman, Bowler, All-Rounder, Wicket-Keeper?


# In[74]:


mysql("""SELECT Types, round(avg(Cost_INR),2) average_price FROM df3 GROUP BY 1 ORDER BY 2 DESC LIMIT 5 """)


# In[ ]:


#Question 5 - List of Retained players with team name and salary?


# In[75]:


mysql("""SELECT PlayerS, Cost_INR FROM df3 WHERE Base_Price ="Retained" ORDER BY 2 DESC LIMIT 5 """)


# In[ ]:




