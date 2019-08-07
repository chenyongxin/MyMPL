"""
Set up colorbar.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams

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
        Tick direction, 'in', 'out'.
        
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
        Tick direction, 'in', 'out'.
        
    """
    cbar.ax.yaxis.set_tick_params(direction=direction)
    prop = fm.FontProperties(fname=fontPath, size=fontSize)
    cbar.ax.yaxis.set_ticklabels(cbar.ax.yaxis.get_majorticklabels(), fontProperties=prop)
    