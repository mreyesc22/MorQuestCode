#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  MorQuestCode
# Purpose:  Module to Read Images
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

import os
from PIL import Image
import matplotlib.pyplot as plt

def display_images(image_dir):
    """
    Display images in a grid layout from the specified directory.

    Parameters:
    - image_dir (str): Directory path containing images.
    """
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    images = [Image.open(os.path.join(image_dir, f)) for f in image_files]
    plt.figure(figsize=(15, 10))
    for i, image in enumerate(images, start=1):
        plt.subplot(3, 3, i)
        plt.imshow(image)
        plt.axis('off')
        plt.title(os.path.splitext(image_files[i-1])[0])  # Remove file extension from title
    plt.tight_layout()
    plt.show()
