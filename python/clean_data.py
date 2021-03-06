import pandas as pd
import sys
import re
import os
import numpy as np

ace_data = pd.read_csv('../data/ACE_MAGSWE_Data.txt', delimiter=' ')
ace_hour = pd.read_csv('../data/full_mag_data.txt', delimiter=' ')

# Handy stuff - remove errorneous data
ace_data = ace_data[ace_data.bgsex != -9999.9]
ace_data = ace_data[ace_data.bgsey != -9999.9]
ace_data = ace_data[ace_data.bgsez != -9999.9]

ace_hour = ace_hour[ace_hour.b_gse_x != -9999.9]
ace_hour = ace_hour[ace_hour.b_gse_y != -9999.9]
ace_hour = ace_hour[ace_hour.b_gse_z != -9999.9]


# Use this to cycle through the days required and make a gif
days_needed = ace_hour['day'].unique().tolist()
hours_needed = ace_hour['hr'].unique().tolist()

# axis limiters for main script
xmin = ace_hour.b_gse_x.min()
xmax = ace_hour.b_gse_x.max()
ymin = ace_hour.b_gse_y.min()
ymax = ace_hour.b_gse_y.max()
