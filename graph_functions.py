#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:38:40 2024

@author: jennapablo
"""

# written for quicker graphing purposes
# sharing for Nevada ENDURE Data Visualization Workshop

import seaborn as sns
import matplotlib.pyplot as plt 


def graph_settings():
    plt.rcParams.update({'axes.edgecolor': "Black", 
                         'axes.linewidth': 3,
                         'axes.labelsize': 16,
                         'text.color': "Black", 
                         'font.size': 15, 
                         'font.family': 'Times New Roman',
                         'axes.labelweight': 'bold'})

#Two-way graph (i.e., two groups on x and two or more groups in legend)

def two_way_graph(x,y,data,split, x_label = "X-Label", y_label = "Y-Label",
                  color_pal = "Greys", colors = [2,4], y_lim = "auto", 
                  legend = "on", legend_loc='best',
                  save = "off", individual_pts = 1, pts_size = False, jitter = True):
    graph_settings()
    
    colorPal = sns.color_palette(color_pal)

        
    plt.figure()
    if individual_pts == 1:
        if pts_size:
            ax = sns.stripplot(data = data, x = x, y = y, hue = split,
                          color = 'black', alpha = 0.5,
                          dodge = True, size = pts_size, jitter = jitter)
        else:
            ax = sns.stripplot(data = data, x = x, y = y, hue = split,
                          color = 'black', alpha = 0.5,
                          dodge = True, jitter = jitter)
        
    ax = sns.barplot(data = data, x = x, y = y, hue = split,
                palette= [colorPal[colors[0]], colorPal[colors[1]]],
                capsize = 0.05, errcolor = 'black',
                edgecolor='black',linewidth=1)
    
    ax.tick_params(left = False, bottom = False)
    sns.despine()
    if y_lim != "auto":
        plt.ylim([y_lim[0],y_lim[-1]])
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.tight_layout()
    
    if legend == "off":
        ax.get_legend().remove()
    elif individual_pts == 0: 
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles = handles[0:], labels = labels[0:],loc=legend_loc)
    elif individual_pts == 1:
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles = handles[2:], labels = labels[2:],loc=legend_loc)
        
    if save != "off":
        plt.savefig(save, dpi = 600)
    
    plt.show()

#One-way graph    

def one_way_graph(x,y,data, x_label = "X-Label", y_label = "Y-Label",
                  color_pal = "Greys", colors = [4,4], y_lim = "auto", width=0.8,
                  save = "off", individual_pts = 1, pts_size = False, jitter = True):
    graph_settings()
    
    colorPal = sns.color_palette(color_pal)

        
    plt.figure()
    if individual_pts == 1:
        if pts_size:
            ax = sns.stripplot(data = data, x = x, y = y,
                         color = 'black', alpha = 0.5,
                         dodge = True, size = pts_size, jitter = jitter)
        else:
            ax = sns.stripplot(data = data, x = x, y = y,
                         color = 'black', alpha = 0.5,
                         dodge = True, jitter = jitter)
        
    ax = sns.barplot(data = data, x = x, y = y,
                palette= [colorPal[colors[0]], colorPal[colors[1]]],
                capsize = 0.05, errcolor = 'black', width=width)
    
    ax.tick_params(left = False, bottom = False)
    sns.despine()
    if y_lim != "auto":
        plt.ylim([y_lim[0],y_lim[-1]])
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.tight_layout()
    
    if save != "off":
        plt.savefig(save, dpi = 600)
    
    plt.show()    

# Scatter graph

def scatter(data, x, y, color_pal = "Greys", colors = 3,x_label = "X-Label",
            y_label = "Y-Label",label = None,save = "off", y_lim = [0, 1],
            x_lim = [0, 1]):
   
     graph_settings()
    
     colorPal = sns.color_palette(color_pal)
    
     plt.figure()
     sns.regplot(data = data, x = x, y = y, color = colorPal[colors], label= label)
     plt.xlabel(x_label)
     plt.ylabel(y_label)
     plt.xlim(x_lim)
     plt.ylim(y_lim)
     plt.tick_params(left = False, bottom = False)
     
     if label != None:
         plt.legend()
         
     sns.despine()
    
     if save != "off":
        plt.savefig(save, dpi=600)
        
     plt.show()
        
        
        
        
    
