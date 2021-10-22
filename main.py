# importing the required module
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import interpolate, make_interp_spline, BSpline, interp1d

def creategraph(k, A, B, C, trig):
    period = (2 * np.pi) / B
    
    xvalue = np.linspace(0, period, num=100)
    phaseshift = xvalue + (C / B)
    # Introducing trig and B and phaseshift
    y = trig(B*phaseshift)
    # Introducing A
    y = (A * y)
    # Introducing k
    y = y + k
    x = np.linspace(0, period, num=100)
    f_cubic = interp1d(x, y, kind='cubic')

    print(period / np.pi)

    fig, ax = plt.subplots()

    

    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[3] = (period / np.pi) / 2
    labels[6] = period / np.pi

    ax.set_xticklabels(labels)

    plt.xlim([0, period])
    plt.plot(x, f_cubic(x))
    plt.legend(loc='best')
    plt.xlabel('radians (π)')
    plt.grid('both')

    plt.show()
    
creategraph(0, 2, 1, 0, np.sin)

# y = k + Atrig(B(x + (C / B)))