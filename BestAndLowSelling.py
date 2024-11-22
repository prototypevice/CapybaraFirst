import numpy as np
import pandas as pd

# Load the Excel file
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

# Sort for top 5 best-selling based on weighted score
df_sorted_best_selling = df.sort_values(by=['Weighted_Score'], ascending=False).head(7)

# Identify low-sellers: SlowMoving and low or zero sales
df_sorted_low_selling = df[
    (df['InventoryMovementStatus'] == 0) &
    (df['60_DaySales'] <= 20)  # Replace 10 with your threshold for low sales
].sort_values(by=['60_DaySales', 'InventoryMovementStatus'], ascending=[True, True]).head(7)

#Assign top 5 best-selling and low-selling products
top_7_best_selling = df_sorted_best_selling
top_7_low_selling = df_sorted_low_selling

# Display results
print("Top 5 Best-Selling Products (Weighted):")
print(top_7_best_selling[['SKU', '60_DaySales', '60_DaySalesValue', 'Weighted_Score', 'Sellable Stock']])
print("\nTop 5 Low-Selling Products:")
print(top_7_low_selling [['SKU', '60_DaySales', '60_DaySalesValue', 'Weighted_Score', 'Sellable Stock']])
