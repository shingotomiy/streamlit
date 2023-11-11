st.title("Data Exploration App")
  
# Data loading and display
df = load_data("https://ai-jobs.net/salaries/download/salaries.csv")
st.write("Data Overview:", df)
  
st.write(df.describe())

  # Linear Regression
x_col, y_col = st.selectbox('Select X Column', df.columns), st.selectbox('Select Y Column', df.columns)
X = df[[x_col]].values.reshape(-1, 1)
Y = df[y_col].values
model = LinearRegression()
model.fit(X, Y)
st.write(f"Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}")

