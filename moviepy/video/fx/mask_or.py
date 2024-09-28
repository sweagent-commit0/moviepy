import numpy as np
from ..VideoClip import ImageClip

def mask_or(clip, other_clip):
    """ Returns the logical 'or' (max) between two masks.
        other_clip can be a mask clip or a picture (np.array).
        The result has the duration of 'clip' (if it has any)
    """
    pass