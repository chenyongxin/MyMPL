"""
Setup figure page.

@author: CHEN Yongxin
"""

import os
from matplotlib import font_manager as fm
from matplotlib import rcParams
import matplotlib.pyplot as plt

def mm2inch(mm):
    """
    Convert millimetre to inch.
    """
    return 0.0393701 * mm

def figureWidth(wa=0.7, rb=0.9, wp=210):
    """
    Compute figure width in inch.
    
    Parameters
    ----------
    wa: float
        Ratio of figure width to text width. For example, wa=0.7 is equivalent to 
        width=0.7\textwidth in LaTeX. 
    
    rb: float
        Ratio of border of text. For example, rb=0.9 for the ratio of text to the 
        width of page is 0.9.
        
    wp: int, float
        Width of page in millimetre. Default value 210 is for a A4 paper.
        
    Returns
    -------
    width: int, float
        Figure width in inch.
    """
    return mm2inch(wa*rb*wp)

def figureHeight(width, ratio=0.618):
    """
    Compute figure height with a ratio.
    
    Parameters
    ----------
    width: int, float
        Figure width in inch.
        
    ratio: float
        Ratio of height to wdith.
    
    Returns
    -------
    height: int, float
        Figure height in inch.
    """
    return width*ratio

def figureSize(wa=0.7, rb=0.9, wp=210, ratio=0.618):
    """
    Compute figure width and height.
    
    Parameters
    ----------
    wa: float
        Ratio of figure width to text width. For example, wa=0.7 is equivalent to 
        width=0.7\textwidth in LaTeX. 
    
    rb: float
        Ratio of border of text. For example, rb=0.9 for the ratio of text to the 
        width of page is 0.9.
        
    wp: int, float
        Width of page in millimetre. Default value 210 is for a A4 paper.
        
    ratio: float
        Ratio of height to wdith.
        
    Returns
    -------
    figsize: tuple
        Figure width and height in inch.
    """
    width = figureWidth(wa, rb, wp)
    return (width, figureHeight(width, ratio))