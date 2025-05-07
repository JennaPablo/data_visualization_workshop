#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  6 20:21:57 2025

@author: jennapablo
"""

#Example: How to use JP's graph functions


#%%imports
import pandas as pd 
import os
os.chdir('/Users/jennapablo/Desktop/data_visualization/') #graph function script path
import graph_functions as gf


#%%load in data
#load in the dataset
wm_df = pd.read_csv("wm_dataset.csv")
#view first few rows
wm_df.head()

#%% bar graph

gf.two_way_graph(x = 'SetSize', y = 'Accuracy', data = wm_df, split = 'Domain',
                  x_label = 'Set Size', y_label = 'Proportion Correct',
                  y_lim = [0.45, 1.05],color_pal = 'bone',colors = [2,4],
                  jitter = .20,legend_loc = 'upper right', legend='on',
                  save = 'wm_acc_bar.png')

