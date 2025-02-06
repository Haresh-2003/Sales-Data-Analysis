import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path (raw string notation)
file_path = r'C:\Users\HARESH PS\Desktop\sales_data_sample.csv'

# Collect Data with specified encoding and handling bad lines
df = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip')

# Inspecting column names
print("Columns in dataset:", df.columns)

# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)

# EDA
print(df.describe())
# Modify 'REGION' to the correct column name
if 'REGION' in df.columns:
    print(df.groupby('REGION').mean())
else:
    print("Column 'REGION' not found. Please specify the correct column name.")

# Visualization
# Bar Chart for Sales by Region (use correct column name for region)
plt.figure(figsize=(12, 6))
if 'REGION' in df.columns:
    sns.barplot(x='REGION', y='SALES', data=df)
    plt.title('Sales by Region')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Column 'REGION' not found. Skipping bar chart for sales by region.")

# Line Graph for Sales Trends Over Time
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
plt.figure(figsize=(12, 6))
sns.lineplot(x='ORDERDATE', y='SALES', data=df, marker='o')
plt.title('Sales Trends Over Time')
plt.xticks(rotation=45)
plt.show()

# Pie Chart for Product Category Distribution
plt.figure(figsize=(8, 8))
df['PRODUCTLINE'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Product Line Distribution')
plt.show()

# Generate Insights
top_product = df.groupby('PRODUCTLINE').sum().sort_values(by='SALES', ascending=False).index[0]
peak_sales_month = df['ORDERDATE'].dt.month.mode()[0]
print(f"Top product line: {top_product}")
print(f"Peak sales month: {peak_sales_month}")
