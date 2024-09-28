resize_possible = True
try:
    import cv2
    import numpy as np
    resizer.origin = 'cv2'
except ImportError:
    try:
        from PIL import Image
        import numpy as np
        resizer.origin = 'PIL'
    except ImportError:
        try:
            from scipy.misc import imresize
            resizer = lambda pic, newsize: imresize(pic, map(int, newsize[::-1]))
            resizer.origin = 'Scipy'
        except ImportError:
            resize_possible = False
from moviepy.decorators import apply_to_mask

def resize(clip, newsize=None, height=None, width=None, apply_to_mask=True):
    """ 
    Returns a video clip that is a resized version of the clip.
    
    Parameters
    ------------
    
    newsize:
      Can be either 
        - ``(width,height)`` in pixels or a float representing
        - A scaling factor, like 0.5
        - A function of time returning one of these.
            
    width:
      width of the new clip in pixel. The height is then computed so
      that the width/height ratio is conserved. 
            
    height:
      height of the new clip in pixel. The width is then computed so
      that the width/height ratio is conserved.
    
    Examples
    ----------
             
    >>> myClip.resize( (460,720) ) # New resolution: (460,720)
    >>> myClip.resize(0.6) # width and heigth multiplied by 0.6
    >>> myClip.resize(width=800) # height computed automatically.
    >>> myClip.resize(lambda t : 1+0.02*t) # slow swelling of the clip
    
    """
    pass
if not resize_possible:
    doc = resize.__doc__
    resize.__doc__ = doc