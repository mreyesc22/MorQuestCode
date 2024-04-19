#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Module to Channel Analysis
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

def analyze_channel_area(selection):
    # Read the data from Shapefile
    shp_path = 'Data/Channel_Area/Channel_area_2016.shp'
    channel = gpd.read_file(shp_path, encoding='utf-8')

    # Group by name2 and calculate sum of areas
    channel_analysis = channel.groupby(['name2'])['area'].sum() / 1000000
    channel_analysis = pd.DataFrame(channel_analysis).reset_index()

    if selection in channel_analysis['name2'].values:
        print("Valid estuary selected:", selection)
        select_channel = channel_analysis[channel_analysis['name2'] == selection]
        return select_channel
    else:
        print("Invalid estuary selected:", selection)
        return None
