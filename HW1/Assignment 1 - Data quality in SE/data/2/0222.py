
from retrieveSpectrum.retrieveSpectrum import retrieve_spectrum 

data_filename = 'sample_file.json' 
elements =[] 

Spec = retrieve_spectrum(data_folder='', data_filename= data_filename, \
        N_temp= 1 , state_T= 'None' ,  \
        elements= elements, N_ab=1, state_ab='None',\
        spectrum_folder ='/home/malavika/Documents/petitRT/spectrum_codeastro/',\
        delta = 20 , wlmin = 0.3 , wlmax= 15)

Spec. Nspectra() 

import numpy as np
from CCF import  CrossCorr
from _utils import *

#read old data 
wavs,flux=readFile('/home/malavika/Documents/petitRT/spectrum_codeastro/CH4_CO2_CO_all_iso_H2_H2O_He_K_Na/spectrum.csv')
waves_downsampled=np.arange(1.4,2.4,1e-4)
flux_downsampled=np.interp(waves_downsampled,wavs,flux)
flux_noisy=addRandomNoise(flux_downsampled,noise_fraction=0.1)
vels=np.arange(-2000,2000,20)
CC=CrossCorr(vels)
window_size=101
order=1
CC.compareFluxes(waves_downsampled,
                flux_noisy,
                wavs,
                flux,
                window_size=window_size,
                order=order)
