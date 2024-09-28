import numpy as np
from ..VideoClip import ImageClip

def mask_and(clip, other_clip):
    """ Returns the logical 'and' (min) between two masks.
        other_clip can be a mask clip or a picture (np.array).
        The result has the duration of 'clip' (if it has any)
    """
    pass