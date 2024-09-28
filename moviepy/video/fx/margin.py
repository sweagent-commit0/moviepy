import numpy as np
from moviepy.decorators import apply_to_mask
from moviepy.video.VideoClip import ImageClip

@apply_to_mask
def margin(clip, mar=None, left=0, right=0, top=0, bottom=0, color=(0, 0, 0), opacity=1.0):
    """
    Draws an external margin all around the frame.
    
    :param mar: if not ``None``, then the new clip has a margin of
        size ``mar`` in pixels on the left, right, top, and bottom.
        
    :param left, right, top, bottom: width of the margin in pixel
        in these directions.
        
    :param color: color of the margin.
    
    :param mask_margin: value of the mask on the margin. Setting
        this value to 0 yields transparent margins.
    
    """
    pass