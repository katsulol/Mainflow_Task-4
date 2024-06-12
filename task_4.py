import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv("USvideos.csv")

#print(df.head())
#print(df.shape)
#print(df.info())

df.drop_duplicates(inplace=True)

df.drop(["thumbnail_link", "description"], axis = 1, inplace= True)

#print(df.describe)

df["trending_date"] = df["trending_date"].apply(lambda x: datetime.strptime(x, "%y.%d.%m"))

df["publish_time"] = pd.to_datetime(df["publish_time"])
#print(df.head(2))

df["publish_day"] = df["publish_time"].dt.day
df["publish_month"] = df["publish_time"].dt.month
df["publish_year"] = df["publish_time"].dt.year
df['publish_hour'] = df['publish_time'].dt.hour


#Videos published per year
yearly= df.groupby("publish_year")['video_id'].count()
plt.figure(figsize=(10, 6))
yearly.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Year")
plt.ylabel("Total Publish Count")
plt.title("Total Videos Published per Year")
plt.tight_layout()
plt.show()


#Total views per year
views = df.groupby("publish_year")["views"].count()
plt.figure(figsize=(10, 6))
views.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.xlabel("Year")
plt.ylabel("Total Views")
plt.title("Total Views per Year")
plt.tight_layout()
plt.show()

cat = {1: 'Film and Animation',2: 'Autos and Vehicles',10: 'Music',15: 'Pets and Animals',17: 'Sports',19: 'Travel and Events',20: 'Gaming',22: 'People and Blogs',3: 'Comedy',24: 'Entertainment',25: 'News and Politics',26: 'How to and Style',27: 'Education',28: 'Science and Technology',29: 'Non Profits and Activism',30: 'Movies',43: 'Shows'}
df['category_name'] = df['category_id'].map(cat)
print(df.head())



viewsum = df.groupby("category_name")["views"].sum().reset_index()  
topcat = viewsum.sort_values(by="views", ascending=False).head(10)  

plt.figure(figsize=(12, 8))
sns.barplot(x='category_name', y='views', data=viewsum, edgecolor='black')  
plt.xlabel("Category")
plt.ylabel("Total Views")
plt.title("Total views of each catagory")  
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
sns.barplot(x='category_name', y='views', data=topcat, edgecolor='black')  
plt.xlabel("Category")
plt.ylabel("Total Views")
plt.title("Top 10 Categories by Total Views")  
plt.tight_layout()
plt.show()

#Video count per category
plt.figure(figsize=(14, 8))
sns.countplot(x="category_name", hue='category_name', data=df, order=df['category_name'].value_counts().index, edgecolor='black')
plt.xlabel("Category")
plt.ylabel("Video Count")
plt.title("Video Count by Category")
plt.tight_layout()
plt.show()

#Number of Videos Published per Hour
vph = df['publish_hour'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.barplot(x=vph.index, y=vph.values, hue=vph.index, edgecolor='black')
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.tight_layout()
plt.show()

#Videos Published Over Time
df['publish_date'] = df['publish_time'].dt.date
vcd= df.groupby('publish_date').size()

plt.figure(figsize=(12, 6))
sns.lineplot(data=vcd, color='blue')
plt.title("Videos Published Over Time")
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.tight_layout()
plt.show()

#Scatter plot between views and likes
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='views', y='likes', alpha=0.6, edgecolor=None)
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.show()


cm=df['views'].corr(df['likes'])
print(cm)
