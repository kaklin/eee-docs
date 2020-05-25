import matplotlib.pyplot as plt
import numpy as np


def band_gap(T, E=1.166, a=0.473e-3, b=636):
    """Experimental band gap vs temperature.
    Default fitting parameters are for Silicon"""
    return E - (a * T**2) / (T + b)


def celsius_to_kelvin(C):
    return C + 273.15


def kelvin_to_celsius(K):
    return K - 273.15


vband_gap = np.vectorize(band_gap)
vcelsius_to_bandgap = np.vectorize(celsius_to_kelvin)
start = -80
stop = 130
x = np.arange(start, stop, 5)
E = vband_gap(vcelsius_to_bandgap(x))
fig, ax = plt.subplots(figsize=(8.5, 4.8))
secax = ax.secondary_xaxis('top', functions=(celsius_to_kelvin, kelvin_to_celsius))
secax.set_xlabel('Temperature ($K$)')
ax.set_xlabel('Temperature ($ \degree C $)')
ax.set_ylabel('Bandgap ($eV$)')
ax.plot(x, E)
ax.grid()

plt.show()
