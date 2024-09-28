painting_possible = True
try:
    from skimage.filter import sobel
except:
    try:
        from scipy.ndimage.filters import sobel
    except:
        painting_possible = False
import numpy as np

def to_painting(image, saturation=1.4, black=0.006):
    """ transforms any photo into some kind of painting """
    pass

def painting(clip, saturation=1.4, black=0.006):
    """
    Transforms any photo into some kind of painting. Saturation
    tells at which point the colors of the result should be
    flashy. ``black`` gives the anount of black lines wanted.
    Requires Scikit-image or Scipy installed.
    """
    pass
if not painting_possible:
    doc = painting.__doc__
    painting.__doc__ = doc