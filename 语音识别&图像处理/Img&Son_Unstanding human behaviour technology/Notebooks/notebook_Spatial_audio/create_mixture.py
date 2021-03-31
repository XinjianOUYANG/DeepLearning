#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:55:20 2020

@author: sleglaive
"""

import numpy as np
import soundfile as sf 

def create_mixture(anechoic_FD_auralization, source_wavefiles, a, delta, wlen, hop, win):
        
    stereo_sources = []
    
    for j, wavefile in enumerate(source_wavefiles):
        
        s, fs = sf.read(wavefile) # mono source signal
        s = s/np.max(np.abs(s)) # normalize
        
        sim = anechoic_FD_auralization(s, a[j], delta[j], wlen, hop, win) # stereo source image
        stereo_sources.append(sim)

    T = np.max([sim.shape[0] for sim in stereo_sources]) # number of samples longest source signal
    
    x = np.zeros((T, 2)) # mixture signal
    for sim in stereo_sources:
        x[:sim.shape[0]] += sim
        
    return x