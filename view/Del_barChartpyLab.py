import numpy
from matplotlib.pylab import bar, yticks, xticks, xlim, gca, show

labels = ["Customer1", "Customer2", "Customer3", "Customer4"]
data =   [50,100,150,200]

xlocations = numpy.array(range(len(data)))+0.5
width = 0.5
bar(xlocations, data, width=width)
yticks(range(0, 8))
xticks(xlocations+ width/2, labels)
xlim(0, xlocations[-1]+width*2)
gca().get_xaxis().tick_bottom()
gca().get_yaxis().tick_left()

show()