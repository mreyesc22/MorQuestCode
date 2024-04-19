#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Module to Hydrology Analysis
# Author:   Mishel Reyes, # mreyec@uni.pe
###############################################################################
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
###############################################################################
# changes 19Apr2024
# If the input image is a multi-band one, use all the channels in
# building the stack.
# mreyec@uni.pe

import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import math

def analyze_hydrology(selection):
    # Read hydrological data
    HH = np.genfromtxt(f"Data/hydrology/{selection}.txt", skip_header=36)
    df = DataFrame(HH, columns=['USGS', 'CODE', 'CODE_P', 'C', 'Year', 'Q'])

    # Global Data
    Q_cov = df['Q'] * 0.0283168466
    Qmax = Q_cov.max()
    mean = np.mean(Q_cov)
    mean_r = round(mean, 2)

    # Calculate the mean discharge for the same years as intertidal area
    window_size = 3
    df['Mean_Q'] = df['Q'].rolling(window_size, center=True).mean()
    y_sele = np.arange(1985, 2017, 3)
    s_values = df.loc[df['Year'].isin(y_sele), ['Year', 'Mean_Q']]
    s_values.reset_index(drop=True, inplace=True)

    Qm = s_values['Mean_Q'] * 0.0283168466
    mean_m = np.mean(Qm)
    mean_r_m = round(mean_m, 2)

    # Save data to CSV
    Qm.to_csv(f'results/00_Input_Qr_{selection}.csv', index=False)

    # Plot data
    y = np.arange(1984, 2015, 1)
    xmax = math.ceil(df['Year'].max())
    xmin = math.ceil(df['Year'].min())

    fig = plt.figure(figsize=(20, 8))
    plt.subplot(211)
    plt.title(f"Mean Annual Discharge : {selection}", fontsize=14, color="black")
    plt.plot(df['Year'], Q_cov, color='#4169E1', linewidth=1.5, linestyle='--', marker='o', markersize=8,
             label='Qmean:' + str(mean_r) + ' m$^3$/s')
    plt.ylabel('Discharge (m3/s)')
    plt.fill_between(y, 0, Qmax, facecolor='grey', alpha=.3)
    plt.minorticks_on()
    plt.xlim(xmin, xmax)
    plt.xticks(np.arange(xmin, xmax, 2))
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.legend(loc='upper right', ncol=1, prop={'size': 14}, fancybox=True)

    plt.subplot(212)
    plt.plot(s_values['Year'], Qm, color='#4169E1', linewidth=1.5, linestyle='--', marker='o', markersize=8,
             label='Qmean:' + str(mean_r_m) + ' m$^3$/s')
    plt.bar(s_values['Year'], Qm, color='grey', width=2, edgecolor='grey', alpha=0.3)
    plt.ylabel('Discharge (m3/s)')
    plt.xlabel('Time (year)')
    plt.minorticks_on()
    plt.xticks(np.arange(1984, 2017, 1))
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.legend(loc='upper right', ncol=1, prop={'size': 14}, fancybox=True)

    plt.savefig(f"results/00_Input_Qr_{selection}.png", bbox_inches='tight')

    return s_values
