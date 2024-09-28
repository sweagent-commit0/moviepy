import threading
import time
import numpy as np
import pygame as pg
from moviepy.decorators import convert_masks_to_RGB, requires_duration
from moviepy.tools import cvsecs
pg.init()
pg.display.set_caption('MoviePy')

def imdisplay(imarray, screen=None):
    """Splashes the given image array on the given pygame screen """
    pass

@convert_masks_to_RGB
def show(clip, t=0, with_mask=True, interactive=False):
    """
    Splashes the frame of clip corresponding to time ``t``.
    
    Parameters
    ------------
    
    t
      Time in seconds of the frame to display.
    
    with_mask
      ``False`` if the clip has a mask but you want to see the clip
      without the mask.
    
    """
    pass

@requires_duration
@convert_masks_to_RGB
def preview(clip, fps=15, audio=True, audio_fps=22050, audio_buffersize=3000, audio_nbytes=2, fullscreen=False):
    """ 
    Displays the clip in a window, at the given frames per second
    (of movie) rate. It will avoid that the clip be played faster
    than normal, but it cannot avoid the clip to be played slower
    than normal if the computations are complex. In this case, try
    reducing the ``fps``.
    
    Parameters
    ------------
    
    fps
      Number of frames per seconds in the displayed video.
        
    audio
      ``True`` (default) if you want the clip's audio be played during
      the preview.
        
    audio_fps
      The frames per second to use when generating the audio sound.
      
    fullscreen
      ``True`` if you want the preview to be displayed fullscreen.
      
    """
    pass