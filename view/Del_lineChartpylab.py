from matplotlib.pylab import grid, show, ylabel, xlabel, plot

# x axis
days = ["A", "B", "B", 4, 5]

# y axis
sales = [55, 78, 100, 150, 400]
plot(days, sales)

xlabel('Days')
ylabel('Sale')
grid(True)

show()