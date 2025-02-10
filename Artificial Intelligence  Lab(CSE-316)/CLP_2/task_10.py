import matplotlib.pyplot as plt

regions = ['dhaka', 'comilla', 'khulna', 'barishal', 'rajshahi','chattogram']
sales_revenue = [50000, 55000, 60000, 45000, 35000,25000]

plt.bar(regions, sales_revenue)

plt.title('Sales Revenue Across Different Regions')
plt.xlabel('Regions')
plt.ylabel('Sales Revenue (bdt)')

plt.show()
