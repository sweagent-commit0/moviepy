"""
This module implements all the functions to communicate with other Python
modules (PIL, matplotlib, mayavi, etc.)
"""
import numpy as np

def PIL_to_npimage(im):
    """ Transforms a PIL/Pillow image into a numpy RGB(A) image.
        Actually all this do is returning numpy.array(im)."""
    pass

def mplfig_to_npimage(fig):
    """ Converts a matplotlib figure to a RGB frame after updating the canvas"""
    pass