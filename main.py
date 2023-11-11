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
