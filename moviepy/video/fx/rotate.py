import numpy as np
from moviepy.decorators import apply_to_mask
try:
    from PIL import Image
    PIL_FOUND = True
except ImportError:
    PIL_FOUND = False

def rotate(clip, angle, unit='deg', resample='bicubic', expand=True):
    """
    Change unit to 'rad' to define angles as radians.
    If the angle is not one of 90, 180, -90, -180 (degrees) there will be
    black borders. You can make them transparent with

    >>> newclip = clip.add_mask().rotate(72)

    Parameters
    ===========

    clip
      A video clip

    angle
      Either a value or a function angle(t) representing the angle of rotation

    unit
      Unit of parameter `angle` (either `deg` for degrees or `rad` for radians)

    resample
      One of "nearest", "bilinear", or "bicubic".

    expand
      Only applIf False, the clip will maintain the same True, the clip will be resized so that the whole
    """
    pass