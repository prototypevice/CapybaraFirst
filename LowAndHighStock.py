import numpy as np
import pandas as pd

df = pd.read_excel('data/DATA_SAMPLE.xlsx')

# Replace InventoryMovementStatus categories
df['InventoryMovementStatus'] = df['InventoryMovementStatus'].replace({
    'FastMoving': 1,
    'SlowMoving': 0
})

# Normalize columns for weighted score calculation
df['SalesNormalized'] = df['60_DaySales'] / df['60_DaySales'].max()
df['MovementNormalized'] = df['InventoryMovementStatus'] / df['InventoryMovementStatus'].max()

# Apply weights to calculate the weighted score
sales_weight = 0.7
movement_weight = 0.3
df['Weighted_Score'] = (
    ( (sales_weight * df['SalesNormalized']) + (movement_weight * df['MovementNormalized']) ) * 100
)

# Sort for top 5 best-selling based on sellable stock
df_sorted_low_stock = df.sort_values(by=['Sellable Stock', 'Weighted_Score'], ascending=[True, False]).head(10)
df_sorted__high_stock = df.sort_values(by=['Sellable Stock', 'Weighted_Score'], ascending=[False, False]).head(10)

# Passing the sorted stock on variables
low_on_stock = df_sorted_low_stock
high_on_stock = df_sorted__high_stock


# For printing
print(low_on_stock[['SKU', '60_DaySales', 'Warehouse', 'Warehouse Stock', 'Sellable Stock', 'Buffer Stock', 'Locked Stock', 'Reserved Stock']])
print('\n')
print(high_on_stock[['SKU', '60_DaySales', 'Warehouse', 'Warehouse Stock', 'Sellable Stock', 'Buffer Stock', 'Locked Stock', 'Reserved Stock']])
