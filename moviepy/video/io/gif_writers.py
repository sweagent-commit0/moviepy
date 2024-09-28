import os
import subprocess as sp
import numpy as np
import proglog
from moviepy.compat import DEVNULL
from moviepy.config import get_setting
from moviepy.decorators import requires_duration, use_clip_fps_by_default
from moviepy.tools import subprocess_call
try:
    import imageio
    IMAGEIO_FOUND = True
except ImportError:
    IMAGEIO_FOUND = False

@requires_duration
@use_clip_fps_by_default
def write_gif_with_tempfiles(clip, filename, fps=None, program='ImageMagick', opt='OptimizeTransparency', fuzz=1, verbose=True, loop=0, dispose=True, colors=None, logger='bar'):
    """ Write the VideoClip to a GIF file.


    Converts a VideoClip into an animated GIF using ImageMagick
    or ffmpeg. Does the same as write_gif (see this one for more
    docstring), but writes every frame to a file instead of passing
    them in the RAM. Useful on computers with little RAM.

    """
    pass

@requires_duration
@use_clip_fps_by_default
def write_gif(clip, filename, fps=None, program='ImageMagick', opt='OptimizeTransparency', fuzz=1, verbose=True, withmask=True, loop=0, dispose=True, colors=None, logger='bar'):
    """ Write the VideoClip to a GIF file, without temporary files.

    Converts a VideoClip into an animated GIF using ImageMagick
    or ffmpeg.


    Parameters
    -----------

    filename
      Name of the resulting gif file.

    fps
      Number of frames per second (see note below). If it
        isn't provided, then the function will look for the clip's
        ``fps`` attribute (VideoFileClip, for instance, have one).

    program
      Software to use for the conversion, either 'ImageMagick' or
      'ffmpeg'.

    opt
      (ImageMagick only) optimalization to apply, either
      'optimizeplus' or 'OptimizeTransparency'.

    fuzz
      (ImageMagick only) Compresses the GIF by considering that
      the colors that are less than fuzz% different are in fact
      the same.


    Notes
    -----

    The gif will be playing the clip in real time (you can
    only change the frame rate). If you want the gif to be played
    slower than the clip you will use ::

        >>> # slow down clip 50% and make it a gif
        >>> myClip.speedx(0.5).write_gif('myClip.gif')

    """
    pass

def write_gif_with_image_io(clip, filename, fps=None, opt=0, loop=0, colors=None, verbose=True, logger='bar'):
    """
    Writes the gif with the Python library ImageIO (calls FreeImage).

    Parameters
    -----------
    opt

    """
    pass