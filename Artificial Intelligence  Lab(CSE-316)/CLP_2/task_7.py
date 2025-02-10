import pandas as pd

data=pd.read_csv('files/sales_data.csv')
data['total revenue per product']=data['quantity']*data['price']
total_revenue=sum(data['total revenue per product'])

print(data)
print("Total's revenue of all products:",total_revenue)