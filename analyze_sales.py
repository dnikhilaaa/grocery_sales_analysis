import pandas as pd

# Load the data
df = pd.read_csv('grocery_sales.csv')

# Calculate total revenue
df['revenue'] = df['units_sold'] * df['price']

# Group by store and category
summary = df.groupby(['store', 'category'])['revenue'].sum().reset_index()

print("Revenue by store and category:")
print(summary)

# Time-series total revenue per day
daily_sales = df.groupby('date')['revenue'].sum().reset_index()
print("\nDaily total revenue:")
print(daily_sales)
