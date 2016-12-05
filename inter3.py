import time                                                
import numpy as np
from scipy.interpolate import interp1d
import scipy as sp

#x size: 500
x = np.linspace(0, 100, num=10, endpoint=True)
y = x*2/9.0
#print "x: ", x

#xnew size:1000
xnew = np.linspace(0, 100, num=1000, endpoint=True)

#print "f(x)=cos(-x**2/9.0): ", y

#print "x.shape: ", x.shape
#print "y.shape: ", y.shape
#print "xnew.shape: ", xnew.shape


start= time.clock()
ynew = sp.interpolate.interp1d(x,y,kind='linear')(xnew)
end= time.clock()
total = end-start
print "spline linear total time: ", total
print "ynew: ", ynew
print "mean: ", np.mean(ynew)
print " "


start= time.clock()
ynew = sp.interpolate.interp1d(x,y,kind='cubic')(xnew)
end= time.clock()
total = end-start
#print "spline cubic total time: ", total
#print "ynew: ", ynew
print "mean: ", np.mean(ynew)
print " "
"""
start= time.clock()
ynew = sp.interpolate.PchipInterpolator(x,y)(xnew)
end= time.clock()
total = end-start
print "pchip total time: ", total
print "ynew: ", ynew
print "mean: ", np.mean(ynew)
print " "

start= time.clock()
ynew = sp.interpolate.UnivariateSpline(x,y)(xnew)
end= time.clock()
total = end-start
print "Univariate spline total time: ", total
print "ynew: ", ynew
print "mean: ", np.mean(ynew)

"""