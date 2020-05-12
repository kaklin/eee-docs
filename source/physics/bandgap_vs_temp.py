import matplotlib.pyplot as plt
import numpy as np


def band_gap(T, E=1.166, a=0.473e-3, b=636):
    """Experimental band gap vs temperature.
    Default fitting parameters are for Silicon"""
    return E - (a * T**2) / (T + b)


def celsius_to_kelvin(C):
    return C + 273.15


vband_gap = np.vectorize(band_gap)
start = celsius_to_kelvin(-80)
stop = celsius_to_kelvin(130)
x = np.arange(start, stop, 5)
E = vband_gap(x)
plt.plot(x, E)
plt.show()
