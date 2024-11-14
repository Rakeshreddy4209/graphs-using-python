import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users/Delll/Downloads/Sales Data Analysis.csv")
quantity_by_category_city = data.groupby(['Product Category', 'City'])['Quantity Ordered'].sum().reset_index()
print(quantity_by_category_city)
pivot_data = quantity_by_category_city.pivot(index='City', columns='Product Category', values='Quantity Ordered')
pivot_data.plot(kind='bar', stacked=False, figsize=(10, 6))
plt.ylabel('Quantity Ordered')
plt.xlabel('City')
plt.title('Quantity Ordered by Product Category in Each City')
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.show()