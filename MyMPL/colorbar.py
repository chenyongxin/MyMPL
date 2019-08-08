"""
Set up colorbar.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np

def label(cbar, text, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12):
    """
    Set up colorbar label
    
    Parameters
    ----------
    cbar: object
        Colorbar object.
        
    text: string
        Label content.
        
    fontPath: string
        Path of font.
    
    fontSize: integer
    """
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    cbar.set_label(text, fontProperties=prop)
    
def horizontal(cbar, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, direction='in'):
    """
    Set up a horizontal colorbar
    
    Parameters
    ----------
    cbar: object
        Colorbar object. Get from
        >>> draw = plt.contour(x, y, z)
        >>> cbar = ax.figure.color(draw, orientation='horizontal')
        
    fontPath: string
        Path of font.
    
    fontSize: integer
    
    direction: string
        Tick direction, 'in', 'out' and 'inout'.
        
    """
    cbar.ax.xaxis.set_tick_params(direction=direction)
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    cbar.ax.xaxis.set_ticklabels(cbar.ax.xaxis.get_majorticklabels(), fontProperties=prop)
    
def vertical(cbar, fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
          fontSize=12, direction='in'):
    """
    Set up a vertical colorbar
    
    Parameters
    ----------
    cbar: object
        Colorbar object. Get from
        >>> draw = plt.contour(x, y, z)
        >>> cbar = ax.figure.color(draw, orientation='vertical')
        
    fontPath: string
        Path of font.
    
    fontSize: integer
    
    direction: string
        Tick direction, 'in', 'out' and 'inout'.
        
    """
    cbar.ax.yaxis.set_tick_params(direction=direction)
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    cbar.ax.yaxis.set_ticklabels(cbar.ax.yaxis.get_majorticklabels(), fontProperties=prop)
    
def make_horizontal_colorbar(cmap, extent, ratio=0.1, ticks=None,
                             fontPath=os.path.join(rcParams["datapath"], "fonts/ttf/Helvetica.ttf"),
                             fontSize=12, direction='in'):
    """
    Make a horizontal colorbar with default matplotlib colorbars
    
    Parameters
    ----------
    cmap: string
        Name of default colorbar.
        
    extent: tuple, list or array with 2 entities, e.g. [0., 10]
        Colorbar range.
        
    ratio: float
        Ratio of short side to long side.
        
    ticks: list of float
        User defined ticks, e.g. [1,2,3,4,5].
    """
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    xticks = []
    if ticks is not None: xticks = ticks
    fig, ax = plt.subplots(1, subplot_kw=dict(xticks=xticks, yticks=[]))
    ax.imshow([colors], extent=[extent[0], extent[1], 0, ratio*(extent[1] - extent[0])])
    if ticks is not None:
        prop = fm.FontProperties(fname=fontPath, size=fontSize)
        ax.xaxis.set_tick_params(direction=direction)
        ax.xaxis.set_ticklabels(ax.get_xticks(), fontProperties=prop)
        
if __name__ == '__main__':
    make_horizontal_colorbar('bwr', [-1.2,1.2], ratio=0.05, ticks=[-1,0,1], direction='in')