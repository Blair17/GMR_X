import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = 'TE.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength, spectrum = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = 'BG_TE.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelengthBG, spectrumBG = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

true_spectrum = ( ( spectrumBG / spectrum ) ) * 100

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(wavelength, spectrum, 'k', lw=2, label='TE') 
ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Reflectance (%)', fontsize=28, fontweight='bold')
ax.tick_params(axis='both', labelsize=25)
ax.legend(frameon=True, loc=0, prop={'size': 22})
plt.xlim([550, 1000])

plt.tight_layout()
plt.show()