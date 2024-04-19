#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Analyze nearshore slope and dc data for a given estuary
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

def analyze_nearshore_data(selection):
    # Read the data from Shapefile
    shp_path0 = 'Data/Nearshore_slopes/Nearshore_slopes.shp'
    nearshore = gpd.read_file(shp_path0, encoding='utf-8')

    # Group by name and calculate mean slope and dc
    nearshore_analysis_slope = nearshore.groupby(['name'])['slope'].mean()
    nearshore_analysis_slope = pd.DataFrame(nearshore_analysis_slope).reset_index()

    nearshore_analysis_dc = nearshore.groupby(['name'])['dc'].mean()
    nearshore_analysis_dc = pd.DataFrame(nearshore_analysis_dc).reset_index()

    nearshore_results = pd.merge(nearshore_analysis_slope, nearshore_analysis_dc, on='name')

    if selection in nearshore_results['name'].values:
        print("Valid estuary selected:", selection)
        select_nearshore = nearshore_results[nearshore_results['name'] == selection]
        return select_nearshore
    else:
        print("Invalid estuary selected:", selection)
        return None
