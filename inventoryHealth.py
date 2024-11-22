import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('data/DATA_SAMPLE.xlsx')

# Replace StockStatus categories
df['StockStatus'] = df['StockStatus'].replace({
    'OutOfStock': 0,
    'LowStock': 1,
    'Healthy': 2
})

# Calculate stock health percentages
stock_health = df['StockStatus'].value_counts(normalize=True, ascending=True) * 100

#Mapped the categoris
category_mapping = {0: 'OutOfStock', 1: 'LowStock', 2: 'Healthy'}
stock_health.index = stock_health.index.map(category_mapping)

#Set the it to dictionary
stock_health_dict = stock_health.dropna().to_dict()

#iterate for printing
#for category, percentage in stock_health_dict.items():
#    print(f"{category}: {percentage:.2f}%")

#print("Stock Health Summary:", stock_health_dict)


plt.bar(stock_health_dict.keys(), stock_health_dict.values())
plt.title('Stock Health Summary')
plt.xlabel('Stock Status')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.show()