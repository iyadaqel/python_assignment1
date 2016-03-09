import pylab

# x axis
days = [1, 2, 3, 4, 5]

# y axis
sales = [55, 78, 100, 150, 400]
pylab.plot(days, sales)

pylab.xlabel('Days')
pylab.ylabel('Sale')
pylab.grid(True)

pylab.show()