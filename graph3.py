import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users/Delll/Downloads/Sales Data Analysis.csv")

sales_by_city = data.groupby('City')['Sales'].sum().reset_index()
print(sales_by_city)
plt.pie(sales_by_city['Sales'], labels=sales_by_city['City'], autopct='%1.1f%%', startangle=90)
plt.title('Sales Contribution by City')
plt.show()