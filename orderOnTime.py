import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read execel
df = pd.read_excel('data/Order Data Sample - Hackathon.xlsx')

# compare values of rts and sot if both the same
df['OrderFulFilledInTime'] = np.where(df['Marketplace RTS SLA'] == df['Marketplace SOT SLA'], 1,0)

# normalize data for percentage
OrderFulFilledInTime_percentage = (df['OrderFulFilledInTime'].value_counts(normalize=True) * 100).round(2)

# Plotting the results
OrderFulFilledInTime_percentage.plot(kind='line')

# Adding titles and labels for clarity
plt.title('Percentage of Orders Fulfilled on Time')
plt.xlabel('Order Fulfillment Status (1 = On Time, 0 = Not On Time)')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.show()