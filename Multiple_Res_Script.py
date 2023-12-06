import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import glob

def custom_sort(filename):
    return int(filename[49:50])

root = os.getcwd()
date = datetime.now().strftime("%d-%m-%Y")

datafilename = 'BG.txt'
datafilepath = os.path.join(
    root,
    datafilename)
wavelength_bTE, spectrum_bTE = np.genfromtxt(
    fname=datafilepath,
    delimiter=";",
    skip_header=1,
    unpack=True)

###########################################################################################
filepath = ''
imagePaths = [f for f in glob.glob(filepath+'*.txt')]
files = sorted(imagePaths, key=custom_sort)
print(files)

norms = [190, 280, 210, 190, 270, 110, 110, 120, 190]

wavelength_array = []
spectrum_array = []
raw_spec_array = []

for index, (f, n) in enumerate(zip(files,norms)):
    
    datafilename = f'{f}' 
    datafilepath = os.path.join(
        root,
        datafilename)
    wavelength_TE, spectrum_TE = np.genfromtxt(
        fname=datafilepath,
        delimiter=";",
        skip_header=1,
        unpack=True)
    
    normTE = n/27
    
    spectrum_TE1 = spectrum_bTE * normTE
    true_spectrumTE = ( ( spectrum_TE / spectrum_TE1 )) * 100
    
    true_spectrumTE = ( true_spectrumTE[300:2000] )
    wavelength_TE = wavelength_TE[300:2000]
    spectrum_TE = ( ( spectrum_TE[300:2000] ) * 100 )

    raw_spec_array.append(spectrum_TE)
    wavelength_array.append(wavelength_TE)
    spectrum_array.append(true_spectrumTE)

labels = ['374', '380', '385', '391', '396', '402', '407', '413', '424']

colors = len(spectrum_array)
cmap = plt.cm.plasma(np.linspace(0,1,colors))

fig, ax = plt.subplots(figsize=(10, 7))
for i, (w, s, c) in enumerate(zip(spectrum_array,wavelength_array,range(colors))):
    ax.plot(s, w, 'k', lw=5, label=labels[i], color=cmap[i])
    ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=28, fontweight='bold')
    ax.tick_params(axis='both', labelsize=25)
    ax.legend(frameon=True, loc='upper right', prop={'size': 18})
    ax.set_ylim([0,100])
    ax.set_xlim([600,800])

plt.tight_layout()
plt.grid()
plt.savefig('TM.png')


