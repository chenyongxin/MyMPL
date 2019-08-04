# MyMPL
> Customized Python Matplotlib package settings


## Two points before use
* This package is used in Mac/Linux system, where the path is defined as A/B/C/D.
* I assume the font 'Helvetica' has been installed in PythonDistribution/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf. If not, you need to specify the complete path of your font accodingly.

## Example
The original code for a sine wave plot is like

``` python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
plt.plot(x, y, label='Sin')
plt.legend(frameon=False)
```
and this may give the result is like
![original](https://github.com/chenyongxin/MyMPL/blob/master/figures/original.png?raw=true)


With additional settings from this repository, for example
``` python
import MyMPL.axis
import MyMPL.label
import MyMPL.legend
ax = plt.gca()
MyMPL.axis.tick_direction(ax, direction='in')
MyMPL.axis.spines(ax)
MyMPL.axis.xytick(ax)
MyMPL.axis.ytick_formatter(ax)
MyMPL.label.xlabel(ax, r"$\Phi$")
MyMPL.label.ylabel(ax, r"Sin($\mathcal{\Phi}$)")
MyMPL.legend.legend(ax, fontsize=12)
```
and the customized result is like

![Customized](https://github.com/chenyongxin/MyMPL/blob/master/figures/customized.png?raw=true)
