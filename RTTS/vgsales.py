import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('RTTS/vgsales.csv')
print(df.head())

#Qa-The Year and Publisher columns contain a few missing values. Treat them accordingly.
# check for missing values
print(df.info())

#Drop the null values in Year and Publisher column
df.drop(df[df.Year.isnull()].index, inplace = True) 
df.drop(df[df.Publisher.isnull()].index, inplace = True)

#check for the missing values again
print(df.info())

# Qb-Convert the values contained in the Year column into integer values.

#Convert the 'Year' column to integers
df['Year'] = df['Year'].astype(int)

# check the datatype again
print(df.info())

# Qc- Find the top 10 most-sold genres of video games sold globally. 

# Group by 'Genre' and sum the 'Global_Sales'
genre_sales = df.groupby('Genre')['Global_Sales'].sum()

# Sort the genres based on sales in descending order
top_10_genres = genre_sales.sort_values(ascending=False).head(10)

# Display the top 10 most-sold genres globally
print(top_10_genres)

# Qd Create genre-wise bar plots for the total number of units sold across different regions and the world

regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

region_sales = df.groupby('Genre').sum()[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]


for i in regions:
    plt.figure(figsize=(10, 6))  # Create a new figure for each plot
    plt.bar(region_sales.index, region_sales[i], color='green')
    plt.title(f'Total Sales by Genre - {i}')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()  # Display each plot one by one


#Qe What genre of video game is most popular in Japan in terms of the total number of units sold? Also, provide the total number of units sold in Japan for that genre.

# Group by 'Genre' and sum the 'JP_Sales' to get the total sales per genre in Japan
highest_sales_jp = df.groupby('Genre')['JP_Sales'].sum()

highest_sales_jp = highest_sales_jp.sort_values(ascending = False).head(1)

print("The most popular video game in Japan and its total number of units sold:  ", highest_sales_jp)

