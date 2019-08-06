"""
Set up contour.

@author: CHEN Yongxin
"""

import numpy as np
import matplotlib.pyplot as plt

def paraview_colormap_generator(cmap, name, output=None, reverse=False):
    """
    Generate a Pavaview xml colormap
    
    Parameters
    ----------
    cmap: object
        Colormap object from matplotlib default color map, e.g. plt.cm.viridis.
        
    name: string
        Name of color map.
        
    output: path, optional
        The full path to save the customized color map.
        e.g. output = "A/B/C/myColorMap.xml".
        
    reverse: boolean, optional
        If reverse the range.
    """
    colors = np.array(cmap.colors)
    if reverse: colors = np.flipud(colors)
    N = colors.shape[0]
    dx = 1./(N-1)
    
    file = "./customized.xml"
    if output is not None: file = output
    with open(file, 'w') as fh:
        fh.write('<ColorMaps>\n')
        fh.write('<ColorMap name="{}" space="RGB">\n'.format(name))
        for i in range(N):
            a = colors[i, :]
            fh.write('<Point x="{}" o="1" r="{}" g="{}" b="{}"/>\n'.format(i*dx, a[0], a[1], a[2]))
        fh.write('</ColorMap>\n' )
        fh.write('</ColorMaps>')
        
        
        
if __name__ == "__main__":
    paraview_colormap_generator(cmap=plt.cm.magma, name="hahaha", reverse=True)