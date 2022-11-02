"""
A patch for a bug which can pop up under mpltern v0.3.5 and matplotlib > v3.6
"""
import matplotlib.axes 
import mpltern.ternary

def get_children(self):
    children = super(matplotlib.axes._axes.Axes, self).get_children()
    self.xaxis.set_visible(False)
    self.yaxis.set_visible(False)
    return children

mpltern.ternary._axes.TernaryAxesBase.get_children = get_children
