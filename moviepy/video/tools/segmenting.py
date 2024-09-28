import numpy as np
import scipy.ndimage as ndi
from moviepy.video.VideoClip import ImageClip

def findObjects(clip, rem_thr=500, preview=False):
    """ 
    Returns a list of ImageClips representing each a separate object on
    the screen.
        
    rem_thr : all objects found with size < rem_Thr will be
         considered false positives and will be removed
    
    """
    pass