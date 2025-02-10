import matplotlib.pyplot as plt

days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
temperatures = [22, 24, 19, 23, 25, 27, 26]
plt.plot(days, temperatures)

plt.title('Temperature Variations Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')

plt.show()
