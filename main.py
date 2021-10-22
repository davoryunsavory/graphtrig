# importing the required module
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import interpolate, make_interp_spline, BSpline, interp1d

xvalue = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
yvalue = np.sin(4*xvalue)
xnew = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
f_cubic = interp1d(xnew, yvalue, kind='cubic')
plt.plot(xnew, f_cubic(xnew))
plt.legend(loc='best')
plt.grid('both')
plt.show()