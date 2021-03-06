#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def simple():
        
    plt.plot([1,2,3,4],[1,4,9,16],'m-.')  # letter for colour and other bit for style
    plt.ylabel('some numbers')
    plt.axis([0,6,0,20])  # [xmin, xmax, ymin, ymax]
    
    plt.show()

def simple2():
    
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    
    # Can mess around with each of the different lines by tupling them out
    line1,line2,line3 = plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'r-',linewidth=3.0)
    line3.set_antialiased(False)
    plt.setp(line1, color='m', linewidth=3.0)
    plt.show()

def simple3():
    
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

    plt.show()


if __name__ == "__main__":
    simple3()
