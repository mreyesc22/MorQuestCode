#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Analyze intertidal area data from a Shapefile for a specific estuary.
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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def analyze_intertidal_area(shapefile_path, selection):
    # Read the data from Shapefile
    data = gpd.read_file(shapefile_path, encoding='utf-8')

    # Filter data for the selected estuary
    data_selection = data[data['Est'] == selection]

    # Group the data and calculate sum of areas
    analysis = data_selection.groupby(['Est', 'Year'])['area'].sum() / 1000000
    df1 = pd.DataFrame(analysis).reset_index()

    ymax = math.ceil(df1['area'].max()) + 2
    coefficients = np.polyfit(df1['Year'], df1['area'], 1)
    slope = coefficients[0]
    intercept = coefficients[1]
    trendline = slope * df1['Year'] + intercept
    df1.to_csv(f'results/00_Input_Intertidal_Area_{selection}.csv', index=False)

    # Plot colormap
    colormap = plt.cm.get_cmap('viridis', len(df1['Year'].unique()))

    # Plot intertidal evolution
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    for idx, year in enumerate(df1['Year'].unique()[::-1]):
        subset = data_selection[data_selection['Year'] == year]
        subset.plot(ax=axes[0], color=colormap(idx), label=str(year))
    axes[0].set_title(f'{selection}', fontsize=14, color="black")
    axes[0].grid(True)

    plt.title(f"Intertidal Evolution : {selection}", fontsize=14, color="black")
    plt.bar(df1['Year'], df1['area'], label=selection,
            color=['#440154', '#482475', '#414487', '#355f8d', '#2a788e', '#21918c',
                   '#22a884', '#44bf70', '#7ad151', '#bddf26', '#fde725'],
            width=2, edgecolor='#708090', linewidth=2)
    plt.plot(df1['Year'], trendline, color='black', linewidth=1.5, linestyle='--', label='Trend Line')
    plt.ylabel('Area (km2)')
    plt.xlabel('Year')
    plt.ylim(0, ymax)
    plt.minorticks_on()
    plt.grid(True)
    plt.legend(loc='upper right', ncol=1, prop={'size': 14}, fancybox=True)
    plt.xticks(np.arange(1984, 2018, 3))
    for x, y in zip(df1['Year'], df1['area']):
        plt.text(x, y, '{:.2f}'.format(y), ha='center', va='bottom')

    plt.savefig(f"results//00_Input_Intertidal_Area_{selection}.png", bbox_inches='tight')

    return df1