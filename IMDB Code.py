# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:38:17 2025

@author: NivedithaVM
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("IMDB-Movie-Data.csv")

## DATA UNDERSTANDING ##


# Display top 10 rows in the dataset
data.head(10)
# Bottom 10 rows 
data.tail(10)

## Find the no of rows and no of columns
data.shape

## Getting more information like Datatypes of each column and memmory type
data.info()

### MISSING VALUES ### 

# check missing values in the dataset
print("Any missing data",data.isnull().values.any()) ## Will give output as TRUE or FALSE

data.isnull().sum()
sns.heatmap(data.isnull()) ## Missing values using Heatmap
percentange_missing = data.isnull().sum() *100 / len (data)
percentange_missing 
 
data.dropna(axis = 0) # axis =0 means it will drop rows containing missing values
# axis = 1 means it will remove columns containing missing values

### DUPLICATES REMOVAL ### 
dup_data = data.duplicated().any()
print("Are tehre any duplicates",dup_data)
data = data.drop_duplicates()
data 
### ANALYSIS ###

## Get overall statistics about our dataframe
data.describe() # This will give for only numeric values 
# But this will give for all the columns both numeric and categorical.

## 1. Display Title of the movie having runtime >= 180 minutes

data.columns
data['Runtime (Minutes)']>=180  # will give true or false to each rows
data[data['Runtime (Minutes)']>=180] ["Title"] # will give title of the rows satisfying the condition

## 2. Which year have the highest average voting? 

data.groupby('Year')['Votes'].mean().sort_values(ascending =False)
palette = sns.color_palette("tab10", 10)
sns.barplot (x='Year',y='Votes',data=data,palette=palette)

## 3. which year has the highest average revenue

data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending =False)

palette = sns.color_palette("tab10", 10)
sns.barplot(x="Year",y="Revenue (Millions)",data =data,palette=palette)

##4. Find the average rating for each of the director

data.groupby("Director")["Rating"].mean().sort_values(ascending = False)

## 5. Display top 10 lengthy movies title and Runtime
## data.groupby("Runtime (Minutes)").sort_values(Ascending = False).head(10) ["Runtime (Minutes)"] ["Title"]
# data.nlargest() 
# nlargest will returns the forst n rows ordered by columns in descending order.
top_10_len = data.nlargest(10 ,"Runtime (Minutes)",keep='first') [["Title","Runtime (Minutes)"]]\
    .set_index("Title") ## To get the Title as the index not the data index
    
# Barplot is used to show the relationship between categorical data and atleast one numerical data
palette = sns.color_palette("tab10", 10)
sns.barplot(x="Runtime (Minutes)",y=top_10_len.index,data=top_10_len,palette=palette)

## 6. Display no of movies Per Year
data["Year"].value_counts()
sns.countplot(x='Year',data =data) 
plt.title("No of movies per year")
plt.show()

## 7. Find most popular movie Title (Highest revenue)
data.columns
data [data['Revenue (Millions)'].max() == data['Revenue (Millions)']] ["Title"]

##8. Display top 10 Highest rated movies Titles and its directors
top_10_rating = data.nlargest(10,"Rating",keep='first')[["Title","Director","Rating"]]
top_10_rating
sns.barplot(x='Rating',y='Title',data = top_10_rating,palette=palette)


##9.Display top 10 highest revenue movie titles
top_10_rev = data.nlargest(10,"Revenue (Millions)",keep='first')[["Title","Revenue (Millions)"]]\
    .set_index("Title")
sns.barplot(x='Revenue (Millions)',y='Title',data=top_10_rev)

## 10. Find average rating of movies year wise
data.groupby("Year")["Rating"].mean()

## 11. Does rating affect the revenue?
sns.scatterplot(x="Rating",y="Revenue (Millions)",data = data)
# Here we can say  that rating is directly proportional to revenue.

## 12. Classsify movies based on Ratings [Excellent, Good, Average]
data.columns
def Movie_Classification (rating):
    if rating >= 7.0:
        return"Excellent"
    elif rating >= 5.0:
        return "Good"
    else:
        return "Average"
data["Rating_new"]= data['Rating'].apply(Movie_Classification)
data.head(2)

## 13. No of Action Movies
data.columns
len(data[data["Genre"].str.contains("Action")])

## 14. Find unique values form Genre
list1=[]
for value in data["Genre"]:
    list1.append(value.split(","))
one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)

one_d
unique_list = []
for item in one_d:
    if item not in unique_list:
        unique_list.append(item)

 ## 15. How many films of each genre was made
    
from collections import Counter 
Counter(one_d)

  
    
    
