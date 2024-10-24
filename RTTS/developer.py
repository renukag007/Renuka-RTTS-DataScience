import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#creating a dataframe by reading the csv file
df = pd.read_csv('RTTS/Developers.csv')

print(df.head())

#check for column names and null values

print(df.info())

# Q1. Create customized line plots to compare the salary variations Age-wise for Python developer with Javascript developer.

# Filter the required columns
df2 = df[['Age', 'Python', 'JavaScript']]

print(df2)


# Create the line plot
plt.figure(figsize=(10,6))

# Plot Python developer salaries age-wise
plt.plot(df2['Age'], df2['Python'], label='Python Developer', color='green', marker='o')

# Plot JavaScript developer salaries age-wise
plt.plot(df2['Age'], df2['JavaScript'], label='JavaScript Developer', color='gold', marker='o')

# Add titles and labels
plt.title('Age-wise Salary Comparison: Python vs JavaScript Developers')
plt.xlabel('Age')
plt.ylabel('Average Annual Salary- in Dollars')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


#Q2. What can you conclude from the comparison?

print(''' We can conclude by seeing the data and the plots that python developers earn more than
      Javascript developers ie the salaries of python developers across all age groups are 
      higher than the salaries of JavaScript Developers''')
