import numpy as numpy
import pylab as pylab

# x=[1,2,3,4,5]
# # y=[1,2,10,3,7]
# #
# # pylab.plot(x, y);
# # pylab.show();

x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]
pylab.plot(x1, y1, 'r')
pylab.plot(x2, y2, 'g')
pylab.title('Plot of y vs. x')
pylab.xlabel('x axis')
pylab.ylabel('y axis')
pylab.xlim(0.0, 9.0)
pylab.ylim(0.0, 30.)
pylab.show()