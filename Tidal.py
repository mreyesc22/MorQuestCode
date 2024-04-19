#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Analyze tidal data
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

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import math

def analyze_tidal_data():
    # Read tidal data
    basin = pd.read_csv('Data/Tidal/d575a.csv', names=['Year', 'month', 'day', 'data'], skiprows=0)
    basin = basin[basin['data'] >= 0]
    basin['date'] = pd.to_datetime(basin[['Year', 'month', 'day']])
    tidal_range = (basin['data'].max() + basin['data'].min())//2

    # Calculate the range (min and max) for each month
    monthly_min_max = basin.groupby(basin['date'].dt.to_period('M')).agg({'data': ['min', 'max']})
    monthly_min_max['mean'] = monthly_min_max[('data', 'min')] + (monthly_min_max[('data', 'max')] - monthly_min_max[('data', 'min')]) / 2
    monthly_min_max.reset_index(inplace=True)

    # Convert the "date" column to a datetime format (if it's not already)
    monthly_min_max['Year'] = monthly_min_max['date'].dt.year
    monthly_min_max['month'] = monthly_min_max['date'].dt.month

    # Mean value per year
    yearly_mean = monthly_min_max.groupby('Year')['mean'].mean().reset_index()

    # Trendline calculation
    coef_A = np.polyfit(yearly_mean['Year'], yearly_mean['mean'], 1)
    slope_A = coef_A[0]
    intercept_A = coef_A[1]
    trendline_A = slope_A * yearly_mean['Year'] + intercept_A

    # Calculate the mean over a window
    window_size = 3
    yearly_mean['mean3'] = yearly_mean['mean'].rolling(window_size, center=True).mean()
    y_sele = np.arange(1985,2017,3)
    b_values = yearly_mean.loc[yearly_mean['Year'].isin(y_sele), ['Year', 'mean3']]
    b_values.reset_index(drop=True, inplace=True)

    # Plot
    fig = plt.figure(figsize=(20,10))
    plt.subplot(311)
    plt.plot(basin['date'], basin['data'], linewidth=0.5, color='#4682B4', label='tidal range:' + str(tidal_range) + 'mm')
    plt.ylabel('Relative Water Level (MHHW,mm)')
    plt.title('Charleston, OR - USA - Mean MHHW per day')
    plt.legend(loc='upper right', ncol=1, prop={'size':14}, fancybox=True)
    plt.grid(True)

    plt.subplot(312)
    plt.plot(yearly_mean['Year'], yearly_mean['mean'], linewidth=0.5, color='#4682B4', linestyle='--', marker='o')
    plt.plot(yearly_mean['Year'], trendline_A, color='black', linewidth=1.5, linestyle='--', label='Trend Line')
    plt.ylabel('Tidal Range (mm)')
    plt.title('Charleston, OR - USA - Tidal Range per Year')
    plt.ylim(2250, 2600)
    plt.legend(loc='upper right', ncol=1, prop={'size':14}, fancybox=True)
    plt.fill_between(y_sele, 1400, 1900, facecolor='grey', alpha=0.3)
    plt.grid(True)

    plt.subplot(313)
    plt.plot(b_values['Year'], b_values['mean3'], linewidth=0.5, color='#4682B4', linestyle='--', marker='o')
    plt.bar(b_values['Year'], b_values['mean3'], color='grey', width=2, edgecolor='grey', alpha=0.3)
    plt.ylim(2000, 2800)
    plt.xticks(np.arange(1984, 2017, 1))
    plt.xlabel('Year')
    plt.ylabel('Tidal Range (mm)')
    plt.title('Charleston, OR - USA - Tidal Range per Year (1984-2016)')

    for x, y in zip(b_values['Year'], b_values['mean3']):
        plt.text(x, y, '{:.2f}'.format(y), ha='center', va='bottom')

    plt.grid(True)

    plt.savefig(f"results/00_Input_Tidal_Alsea_bay.png")

    # Prepare tidal data for return
    tidal_data = b_values[['Year', 'mean3']]
    tidal_data.columns = ['Year', 'Tidal Range (mm)']
    return tidal_data
