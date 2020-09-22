import pandas as pd
import sys
import re
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import gif
import pylab
from clean_data import *

@gif.frame
def space_plot(day, df):
    data = df[df.day == day]
    hours_needed = data['hr'].unique().tolist()
    
    for hr in hours_needed:
        data = data[data.hr == hr]
        x_border = [xmin, xmax]
        y_border = [ymin, ymax]

        x_data = data.b_gse_x.append(pd.Series(xmax))
        x_data = x_data.append(pd.Series(xmin))
        y_data = data.b_gse_y.append(pd.Series(ymax))
        y_data = y_data.append(pd.Series(ymin))
        
        grid_setting = 50
        
        fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(14, 8))
        fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
        fig.patch.set_facecolor('white')
        fig.patch.set_alpha(1)
        ax = axs[0]
        hb = ax.hexbin(x_data, y_data, cmap='inferno', 
                       gridsize=(grid_setting,grid_setting))
        # vmin=0, vmax=15 - for controlling the colour limits
        ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
        ax.set_title("Regular Hexagon binning")
        ax.set_xlabel('Magentic Field (nT) across X position')
        ax.set_ylabel('Magentic Field (nT) across Y position')
        cb = fig.colorbar(hb, ax=ax)
        cb.set_label('Counts')

        ax = axs[1]
        hb = ax.hexbin(x_data, y_data, bins='log', cmap='inferno', 
                       gridsize=(grid_setting,grid_setting))

        ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
        ax.set_title("With a log color scale")
        ax.set_xlabel('Magentic Field (nT) across X position')
        ax.set_ylabel('Magentic Field (nT) across Y position')
        cb = fig.colorbar(hb, ax=ax)
        cb.set_label('log10(N)')
        
        fig.suptitle("""Magnetic Field Experiment - Day: {0}, Hour: {1}""".format(day, hr), 
                     size = 16)
    

frames = []
for day in days_needed:
    for hr in hours_needed:
        data = ace_hour[(ace_hour.hr==hr) & (ace_hour.day==day)]
        frame = space_plot(day=day, df=data)
        frames.append(frame)



gif.save(frames, 'mag_field.gif', duration=100)
