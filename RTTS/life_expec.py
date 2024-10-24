import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("RTTS/LifeExpectancy.csv")
print(df.info())
print(len(df.columns))

# Qa. Rename some columns if they contain leading and trailing spaces (by removing spaces).

df.columns = df.columns.str.strip()

#to check whether spaces are removed
print(df.columns)
print(df.info())


# b. Which columns in the dataset have missing values and how many?
missing_values = df.isnull().sum()

missing_columns = missing_values[missing_values > 0]

print(missing_columns)


# Qc. Drop all the columns from the DataFrame containing more than 15% percent of the missing values.
missing_percentage = df.isnull().mean() * 100
columns_to_drop = missing_percentage[missing_percentage > 15].index
clean_df = df.drop(columns=columns_to_drop)

print(clean_df)

#Qd- Replace the missing values in the remaining columns with the median
 
num_cols = clean_df.select_dtypes(include=['int64','float64'])
clean_df[num_cols.columns] = num_cols.fillna(num_cols.median())

print(clean_df)
print(clean_df.info())