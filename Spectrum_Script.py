import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import find_peaks

def FWHM(wavelength2,true_spectrum):
    deltax = wavelength2[1] - wavelength2[0]
    half_max = max(true_spectrum) / 2
    l = np.where(true_spectrum > half_max, 1, 0)
    
    return np.sum(l) * deltax

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = 'BG_TE.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTE, spectrum_bTE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = 'BG_TM.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTM, spectrum_bTM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

datafilename = 'TE.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TE, spectrum_TE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

datafilename = 'TM.txt' 
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_TM, spectrum_TM = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=0,
    unpack=True)

#############################################################################################

normTE = 70/10
normTM = 140/8

spectrum_TE1 = spectrum_bTE * normTE
true_spectrumTE = ( ( spectrum_TE / spectrum_TE1)) * 100

spectrum_TM1 = spectrum_bTM * normTM
true_spectrumTM = ( ( spectrum_TM / spectrum_TM1)) * 100

##############################################################################################

true_spectrumTE = true_spectrumTE[50:3000]
wavelength_TE = wavelength_TE[50:3000]

true_spectrumTM = true_spectrumTM[50:3000]
wavelength_TM = wavelength_TM[50:3000]

##############################################################################################

spectrum_TE = spectrum_TE[50:3000]
spectrum_bTE = spectrum_bTE[50:3000]

spectrum_TM = spectrum_TM[50:3000]
spectrum_bTM = spectrum_bTM[50:3000]

#############################################################################################

fwhm = FWHM(wavelength_TE,true_spectrumTE)

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(wavelength_TE, true_spectrumTE, 'mediumspringgreen', lw=2, label='BG Corrected TE') 
ax.plot(wavelength_TM, true_spectrumTM, 'k', lw=2, label='BG Corrected TM') 
ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Reflection (%)', fontsize=28, fontweight='bold')
ax.tick_params(axis='both', labelsize=25)
ax.legend(frameon=True, loc=0, prop={'size':18})
plt.xlim([500, 800])
plt.ylim([0, 100])
# plt.text(0.4, 0.9,f'{np.round(fwhm,2)}', ha='center', va='center', fontsize=10, 
#          fontweight='bold', color='c', transform=ax.transAxes)
plt.tight_layout()
plt.grid()
plt.savefig('TE_TM.png')

################################## PEAK VALUES ##############################################

backgrounda = true_spectrumTE[:2000]

idx_y_TE, _ = find_peaks(backgrounda, height=90)
peaks_y_TE = backgrounda[idx_y_TE]
peaks_x_TE = wavelength_TE[idx_y_TE]
print('TE Refl Peak Index=', idx_y_TE, 'TE Refl Peak Value=', peaks_y_TE, 
      'TE Wavelength At Peak=', peaks_x_TE)

TE_peak_value = np.around(peaks_x_TE, 2)

plt.text(0.5, 0.8,''+str(TE_peak_value)+'', ha='center', va='center', fontsize=16, 
         fontweight='bold', color='r', transform=ax.transAxes)
plt.text(0.8, 0.8, '[666.66]', ha='center', va='center', fontsize=16, 
         fontweight='bold', color='r', transform=ax.transAxes)