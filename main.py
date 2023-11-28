import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://ai-jobs.net/salaries/download/salaries.csv")

st.header('Statistics for Data Science - Group 11')
st.write('https://ai-jobs.net/salaries/download/salaries.csv')
st.write(df.describe())


  # Linear Regression
x_col, y_col = st.selectbox('Select X Column', df.columns), st.selectbox('Select Y Column', df.columns)
X = df[[x_col]].values.reshape(-1, 1)
Y = df[y_col].values
model = LinearRegression()
model.fit(X, Y)
st.write(f"Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}")

st.dataframe(df)






from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re as re
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://ai-jobs.net/salaries/download/salaries.csv")

st.header('Statistics for Data Science - Group 11')
st.write('https://ai-jobs.net/salaries/download/salaries.csv')
st.write(df.info())
st.write(df.describe())


columns_of_interest = ['work_year', 'salary','salary_in_usd', 'remote_ratio']

# Generating descriptive statistics for the specified columns
st.write(df[columns_of_interest].describe())


# Set display options to show more rows and columns
pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns

# Grouping by 'job_title' and calculating the mean salary for each title
salarybytitle = df.groupby(['job_title'])[['salary_in_usd']].agg(['mean']).round(2)

 
st.write(salarybytitle)

df['experience_level'].value_counts()

df['employment_type'].value_counts()

# Function to categorize job titles based on keywords
def categorize_job_title(title):
    if 'Analyst' in title :
        return 'Analyst'
    elif 'Manager' in title:
        return 'Manager'
    elif 'Director' in title:
        return 'Director'
    elif 'Engineer' in title:
        return 'Engineer'
    elif 'Engineer' in title:
        return 'Architect'
    elif 'Scientist' in title:
        return 'Developer'
    # Add more conditions for other categories as needed
    else:
        return 'Other'

# Apply the function to create a new column 'Job_Category' in the existing DataFrame 'df'
df['Job_Category'] = df['job_title'].apply(lambda x: categorize_job_title(x))

# Grouping by 'job_category' and calculating the mean salary for each title
salarybycategory = df.groupby(['Job_Category'])[['salary_in_usd']].agg(['mean']).round(2)

st.write(salarybycategory)

df['Job_Category'].value_counts()

df['employee_residence'].value_counts()

df['company_location'].value_counts()

df['company_size'].value_counts()

# Recode 'company_location' into categories 'US', 'GB', 'CA', 'ES', and 'Other'
def recode_location(location):
    if location in ['US', 'GB', 'CA', 'ES']:
        return location
    else:
        return 'Other'

# Apply the recoding function to create a new column 'recoded_location' in the existing DataFrame 'df'
df['recoded_location'] = df['company_location'].apply(recode_location)

df['recoded_residence'] = df['employee_residence'].apply(recode_location)

mapper_companysize = {'S' : 0, 'M' : 1, 'L' : 2}

# Mapping
df['CompanySize_ordinal'] = pd.to_numeric(df['company_size'].map(mapper_companysize))

mapper_experience = {'EN' : 0, 'MI' : 1, 'SE' : 2, 'EX':3}

# Mapping
df['Experience_ordinal'] = pd.to_numeric(df['experience_level'].map(mapper_experience))

df.head(10)

selected=df[['work_year', 'salary_in_usd', 'remote_ratio','CompanySize_ordinal','Experience_ordinal']]

correlation =selected.corr(method="pearson")
display(correlation)




