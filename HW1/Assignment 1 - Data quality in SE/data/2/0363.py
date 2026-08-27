# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:10:06 2018

@author: labuser
"""


# 2018-09-29

import os
import numpy as np
from scipy.stats import cauchy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd


def limit_scan(fname, ax):
    data = pd.read_csv(fname, sep='\t', comment="#", index_col=False)
    data['sig'] = data['s'] - data['sb']
    data.sort_values(by='f', inplace=True)
    data.plot(x='f', y='sig', ax=ax)
    return


def limit():
    """Using the HP 214B, see what the DIL is."""
    fig, ax = plt.subplots()
    fname = "1_lim_dye.txt"
    folder = os.path.join("..", "2018-09-29")
    fname = os.path.join(folder, fname)
    limit_scan(fname, ax)
    fname = "2_lim_dye.txt"
    folder = os.path.join("..", "2018-09-29")
    fname = os.path.join(folder, fname)
    limit_scan(fname, ax)
    return


def cauchy_model(x, a, loc, scale, y0):
    return a*cauchy.pdf(x, loc, scale) + y0


def cauchy_fit(x, y, d):
    if d is -1:
        a0 = -(max(y) - min(y))*(max(x) - min(x))/10
        loc0 = x[np.argmin(y)]
        scale0 = (max(x) - min(x))/10
        y00 = max(y)
    elif d is 1:
        a0 = (max(y) - min(y))*(max(x) - min(x))/10
        loc0 = x[np.argmax(y)]
        scale0 = (max(x) - min(x))/10
        y00 = min(y)
    else:
        a0 = 1
        loc0 = np.mean(x)
        scale0 = (max(x) - min(x))/10
        y00 = 1
    p0 = [a0, loc0, scale0, y00]
    print(p0)
    popt, pcov = curve_fit(cauchy_model, x, y, p0)
    print("Center Frequency is : ", popt[1]*1e-6, " MHz")
    print("FWHM is : ", 2*popt[2]*1e-6, " MHz")
    print("Q is : ", popt[1]/(2*popt[2]))
    return popt


def mw_fscan(fname, d, ax, plotting=True):
    data = pd.read_csv(fname, sep="\t", comment="#", index_col=False,
                       header=None, names=['f', 'b', 's', 'r'])
    data.sort_values(by='f', inplace=True)
    data['sig'] = data['s'] - data['b']
    data['ref'] = data['r'] - data['b']
    data['nrm'] = data['sig'] / data['ref']  # norm by signal / reference
    data['nrm'] = data['nrm']
    popt = cauchy_fit(data['f'].values, data['nrm'].values, d)
    # print(popt)
    if plotting is True:
        data.plot(x='f', y='nrm', ax=ax)
        ax.plot(data['f'].values, cauchy_model(data['f'].values, *popt))
        ax.plot(data['f'].values,
                data['nrm'].values - cauchy_model(data['f'].values, *popt))
    return data


def cavity_resonances():
    """Using the dye laser at -180 GHz, the MW f is scanned over the
    cavity resonances, finding center, FWHM, and Q values."""
    fig, axes = plt.subplots()
    folder = os.path.join("..", "2018-09-29")
    fname = "3_fscan.txt"
    fname = os.path.join(folder, fname)
    mw_fscan(fname, -1, axes)
    axes.axhline(0.9, c='k')
    fig.tight_layout()
    return


def mwion_scan():
    """Take ratios of MW on / MW off to get ionization rate at different values
    of the Variable Attenuator"""
    fig, ax = plt.subplots()
    # Data from 2018-09-27, using the SFIP
    fname = "4_mwion_blnk.txt"  # -180 GHz
    folder = os.path.join("..", "2018-09-29")
    fname = os.path.join(folder, fname)
    data = pd.read_csv(fname, sep="\t", comment="#")
    data['r'] = data['s1']/data['s2']
    data['f'] = np.power(10, data['d']/20)  # field equivalent
    data.sort_values(by='f', inplace=True)
    data.plot(x='f', y='r', marker='v', ax=ax, label="-180 GHz")
    return


if __name__ == "__main__":
    # limit()
    # cavity_resonances()
    mwion_scan()
