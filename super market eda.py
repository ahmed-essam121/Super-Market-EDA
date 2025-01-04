# Importing libraries
import numpy as np
import pandas as pd

# Data visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------------
# Load the dataset
file_path = r'C:\Users\Elbostan\Desktop\full project\supermarket_sales - Sheet1.csv'

# Ensure the file path is valid
import os
assert os.path.exists(file_path), "File not found!"

data = pd.read_csv(file_path)

# Display basic dataset information
print(data.head())
print(data.tail())
print(data.info())
print(data.isna().sum())

# ----------------------------------------------------
# Summary statistics
summary = data.describe()

# Plot a heatmap for summary statistics
fig = px.imshow(
    summary,
    color_continuous_scale="RdYlGn",
    title='Heat Map for Summary Statistics of Data',
    labels={"x": "Data Columns", "y": "Statistics"}
)

fig.update_layout(
    title_font_size=20,
    xaxis_title='Data Columns',
    yaxis_title='Summary',
    xaxis_tickangle=45
)
fig.show()

# ----------------------------------------------------
# Group data by Customer Type and Gender
gender_customer_counts = data.groupby(['Customer type', 'Gender']).size().reset_index(name='Count')
print(gender_customer_counts)

# Barplot for Gender by Customer Type
sns.barplot(x='Customer type', y='Count', hue='Gender', data=gender_customer_counts)
plt.title('Number of Genders by Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Count')
plt.show()

# ----------------------------------------------------
# Group data by Customer Type and Branch
customer_type_in_branches = data.groupby(["Customer type", "Branch"]).size().reset_index(name='Count')
print(customer_type_in_branches)

# Plot a grouped bar chart for Customer Type in Branches
fig = px.bar(customer_type_in_branches, x="Branch", y="Count", color="Customer type", barmode="group")
fig.show()

# ----------------------------------------------------
# Barplot for Product Prices
plt.figure(figsize=(25, 8))
sns.barplot(x='Product line', y='Unit price', data=data, palette='Blues')
plt.title('Product Prices')
plt.xlabel('Product Line')
plt.ylabel('Unit Price')
plt.show()

# -----------------------------------------------------
# Value counts for Product Line
product_line_counts = data['Product line'].value_counts().reset_index()
product_line_counts.columns = ['Product line', 'Count']
print(product_line_counts)

# Plot Quantity by Product Line with Unit Price as color
fig = px.bar(data, x="Product line", y="Quantity", color='Unit price', barmode="group")
fig.show()

# --------------------------------------------------------
# Plot Quantity by Date and Product Line
fig = px.bar(data, x="Date", y="Quantity", color="Product line", title="مجموع الكميات حسب خط الإنتاج والتاريخ")
fig.show()

# Plot Quantity by Date and Branch
fig = px.bar(data, x="Date", y="Quantity", color="Branch", title="مجموع الكميات حسب الفرع والتاريخ")
fig.show()

# --------------------------------------------------------
# COGS and Product Line
cogs_product_line = data.groupby(['cogs', 'Product line']).size().reset_index(name='Count')
cogs_product_line.drop(['Count'], axis=1, inplace=True)
print(cogs_product_line)

# -------------------------------------------------------
# Scatter plot for Quantity vs COGS and Quantity vs Gross Income
fig = go.Figure()

# Add Quantity vs COGS
fig.add_trace(go.Scatter(x=data['Quantity'], y=data['cogs'], mode='markers', name='Quantity vs COGS'))

# Add Quantity vs Gross Income
fig.add_trace(go.Scatter(x=data['Quantity'], y=data['gross income'], mode='markers', name='Quantity vs Gross Income'))

fig.update_layout(
    title='Multiple Relationships Between Columns',
    xaxis_title='Quantity',
    yaxis_title='Values',
    legend_title='Relationships'
)
fig.show()

# ----------------------------------------------------
# Barplot for Product Line Ratings
plt.figure(figsize=(25, 8))
sns.barplot(x='Product line', y='Rating', data=data, palette='Blues')
plt.title('Product Line vs Rating')
plt.xlabel('Product Line')
plt.ylabel('Rating')
plt.show()

# ----------------------------------------------------
# Pairplot for numerical columns
sns.pairplot(
    data[["Quantity", "Tax 5%", "gross margin percentage", "gross income"]],
    palette="viridis"
)
plt.show()

# -----------------------------------------------------
# Correlation Heatmap for Numerical Columns
numerical_columns = data.select_dtypes(include=['int', 'float']).columns
correlation_matrix = data[numerical_columns].corr()

# Use Seaborn's built-in styles
sns.set_style('darkgrid')  # Options: 'white', 'dark', 'whitegrid', 'darkgrid', 'ticks'

# Heatmap for Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap='viridis',
    vmin=-1,
    vmax=1
)
plt.title('Correlation Heatmap')
plt.show()
