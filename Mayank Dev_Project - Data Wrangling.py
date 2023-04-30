#!/usr/bin/env python
# coding: utf-8

# # 1. Import the dataset using Pandas from mentioned url

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')

print(df) 


# 
# # 2. High Level Data Understanding: 
# a. Find no. of rows & columns in the dataset 
# b. Data types of columns. 
# c. Info & describe of data in dataframe. 

# In[4]:


#to find no. of rows and columns in the dataset
df.shape


# In[5]:


#info of data in dataframe
df.info


# In[6]:


#Data -- describe
df.describe


# In[7]:


#data types of columns

r = df.dtypes
r


# # 3. Low Level Data Understanding : 
# a. Find count of unique values in location column. 
# b. Find which continent has maximum frequency using values counts. 
# c. Find maximum & mean value in 'total_cases'. 
# d. Find 25%,50% & 75% quartile value in 'total_deaths'. 
# e. Find which continent has maximum 'human_development_index'. 
# f. Find which continent has minimum 'gdp_per_capita'.

# In[21]:


#finding unique values in location
pd.unique(df.location)


# In[18]:


##finding count of unique values in location 
df.location.nunique()


# In[30]:


#Find which continent has maximum frequency using values counts. 
df.value_counts('continent')


# In[33]:


#max value in continent using value counts
mx_con=max(df.value_counts('continent'))
mx_con


# In[34]:


#continent with max value
df['continent'].value_counts().idxmax()


# In[35]:


#max value of cases in total_cases
mx_cases=max(df.value_counts('total_cases'))
mx_cases


# In[38]:


#mean value of cases in total_cases

mx_cases=df.value_counts('total_cases').mean()
mx_cases


# In[ ]:


d. Find 25%,50% & 75% quartile value in 'total_deaths'. 
e. Find which continent has maximum 'human_development_index'. 
f. Find which continent has minimum 'gdp_per_capita'.


# In[39]:


# Find 25%,50% & 75% quartile value in 'total_deaths'.
mx_cases=max(df.value_counts('total_deaths'))
mx_cases


# In[40]:


#Find 25%,50% & 75% quartile value in 'total_deaths'. 

df['total_deaths'].quantile([0.25, 0.5, 0.75])


# In[64]:


#Find which continent has maximum 'human_development_index'.
mx_hdi=max(df.value_counts('human_development_index'))
mx_hdi


# In[65]:


# Filter the DataFrame to include only the columns relevant to HDI and continent
hdi_df = df[['continent', 'human_development_index']]
hdi_df


# In[74]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')

#Filtering the DataFrame -  including the columns relevant HDI and continent
hdi_df = df[['continent', 'human_development_index']]

# Group the DataFrame by continent and calculate the average HDI for each continent
hdi_avg = hdi_df.groupby('continent')['human_development_index'].mean()

# Find the continent with the maximum average HDI
max_hdi_continent = hdi_avg.idxmax()

# Print the result
print("The continent with the maximum average HDI is", max_hdi_continent," with value: ", max(hdi_avg))
#hdi_avg


# In[75]:


#minimum HDI
min_hdi_continent = hdi_avg.idxmin()

print("The continent with the minimum average HDI is", min_hdi_continent," with value: ", min(hdi_avg))
#hdi_avg


# In[ ]:



#Filtering the DataFrame -  including the columns relevant gdp_per_capita and continent
gdp_df = df[['continent', 'gdp_per_capita']]

# Group the DataFrame by continent and calculate the average HDI for each continent
gdp_avg = gdp_df.groupby('continent')['gdp_per_capita'].mean()

# Find the continent with the maximum average HDI
min_gdp_continent = hdi_avg.idxmin()

# Print the result
print("The continent with the minimum average gdp_per_capita is", min_gdp_continent," with value: ", min(gdp_avg))
#gdp_avg


# # 5. Data Cleaning a. Remove all duplicates observations b. Find missing values in all columns c. Remove all observations where continent column value is missing Tip : using subset parameter in dropna d. Fill all missing values with 0

# In[79]:


#Remove all duplicates observations
df1=df.drop_duplicates()
df1


# In[80]:


df1.shape


# In[81]:


df.shape


# In[86]:


#Missing values
df.isna().sum()


# In[89]:


#Removing all observations where continent column value is missing

df.dropna(subset='continent')


# In[90]:


df.shape


# In[101]:


#replacing all nan with 0

df.replace(np.nan,0)


# In[102]:


df.fillna(0)


# # Date time format : 
# a. Convert date column in datetime format using pandas.to_datetime
# b. Create new column month after extracting month data from date column.

# In[107]:


df.shape


# In[111]:


df['date'] = pd.to_datetime(df['date'])
print(df.info())
df


# In[114]:


# Convert the date column to a Pandas DateTime format
df['date'] = pd.to_datetime(df['date'])

# Extraction of the month data from the date column 
df['Month'] = df['date'].dt.month

df


# # 7. Data Aggregation:
# a. Find max value in all columns using groupby function on 'continent' column Tip: use reset_index() after applying groupby 
# b. Store the result in a new dataframe named 'df_groupby'. (Use df_groupby dataframe for all further analysis)

# In[196]:


#max value in all columns using groupby function on 'continent'


df_groupby = df.groupby('continent').max()
df_groupby=df_groupby.reset_index()
df_groupby
# Group the data by a categorical column and calculate the mean of a numerical column
#df_groupby = df.groupby('category')['value'].mean()
#sns.pairplot(df_groupby)
#reset_index()


# # 8. Feature Engineering : 
# a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'

# In[197]:


# total deaths to total cases ration in new column
df_groupby['tot_dths_t_cses']= df_groupby['total_deaths'] / df_groupby['total_cases']
df_groupby


# # 9. Data Visualization : 
# a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot. 
# b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita' 
# c. Plot Pairplot on df_groupby dataset. 
# d. Plot a bar plot of 'continent' column with 'total_cases' .

# In[198]:


import seaborn as sns
df.replace(np.nan,0)
sns.displot(df_groupby['gdp_per_capita'], kde=False)


# In[199]:


import seaborn as sns
sns.scatterplot(y="total_cases",
                    x="gdp_per_capita",
                    data=df_groupby)
#sns.scatterplot(df['gdp_per_capita'], kde=False)


# In[200]:


sns.pairplot(df_groupby)


# In[201]:


#df_groupby
sns.barplot(x='continent', y='total_cases', palette='magma', data=df_groupby)


# In[202]:


# Save the result to a CSV file without the index
df_groupby.to_csv('df_groupby.csv', index=False)


# In[ ]:




