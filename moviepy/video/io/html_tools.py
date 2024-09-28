"""
This module implements ipython_display
A function to embed images/videos/audio in the IPython Notebook
"""
import os
from base64 import b64encode
from moviepy.audio.AudioClip import AudioClip
from moviepy.tools import extensions_dict
from ..VideoClip import ImageClip, VideoClip
from .ffmpeg_reader import ffmpeg_parse_infos
try:
    from IPython.display import HTML
    ipython_available = True

    class HTML2(HTML):

        def __add__(self, other):
            return HTML2(self.data + other.data)
except ImportError:
    ipython_available = False
sorry = "Sorry, seems like your browser doesn't support HTML5 audio/video"
templates = {'audio': "<audio controls><source %(options)s  src='data:audio/%(ext)s;base64,%(data)s'>" + sorry + '</audio>', 'image': "<img %(options)s src='data:image/%(ext)s;base64,%(data)s'>", 'video': "<video %(options)ssrc='data:video/%(ext)s;base64,%(data)s' controls>" + sorry + '</video>'}

def html_embed(clip, filetype=None, maxduration=60, rd_kwargs=None, center=True, **html_kwargs):
    """ Returns HTML5 code embedding the clip
    
    clip
      Either a file name, or a clip to preview.
      Either an image, a sound or a video. Clips will actually be
      written to a file and embedded as if a filename was provided.


    filetype
      One of 'video','image','audio'. If None is given, it is determined
      based on the extension of ``filename``, but this can bug.
    
    rd_kwargs
      keyword arguments for the rendering, like {'fps':15, 'bitrate':'50k'}
    

    **html_kwargs
      Allow you to give some options, like width=260, autoplay=True,
      loop=1 etc.

    Examples
    =========

    >>> import moviepy.editor as mpy
    >>> # later ...
    >>> clip.write_videofile("test.mp4")
    >>> mpy.ipython_display("test.mp4", width=360)

    >>> clip.audio.write_audiofile('test.ogg') # Sound !
    >>> mpy.ipython_display('test.ogg')

    >>> clip.write_gif("test.gif")
    >>> mpy.ipython_display('test.gif')

    >>> clip.save_frame("first_frame.jpeg")
    >>> mpy.ipython_display("first_frame.jpeg")

    """
    pass

def ipython_display(clip, filetype=None, maxduration=60, t=None, fps=None, rd_kwargs=None, center=True, **html_kwargs):
    """
    clip
      Either the name of a file, or a clip to preview. The clip will
      actually be written to a file and embedded as if a filename was
      provided.

    filetype:
      One of 'video','image','audio'. If None is given, it is determined
      based on the extension of ``filename``, but this can bug.

    maxduration
      An error will be raised if the clip's duration is more than the indicated
      value (in seconds), to avoid spoiling the  browser's cache and the RAM.

    t
      If not None, only the frame at time t will be displayed in the notebook,
      instead of a video of the clip

    fps
      Enables to specify an fps, as required for clips whose fps is unknown.
    
    **kwargs:
      Allow you to give some options, like width=260, etc. When editing
      looping gifs, a good choice is loop=1, autoplay=1.
    
    Remarks: If your browser doesn't support HTML5, this should warn you.
    If nothing is displayed, maybe your file or filename is wrong.
    Important: The media will be physically embedded in the notebook.

    Examples
    =========

    >>> import moviepy.editor as mpy
    >>> # later ...
    >>> clip.write_videofile("test.mp4")
    >>> mpy.ipython_display("test.mp4", width=360)

    >>> clip.audio.write_audiofile('test.ogg') # Sound !
    >>> mpy.ipython_display('test.ogg')

    >>> clip.write_gif("test.gif")
    >>> mpy.ipython_display('test.gif')

    >>> clip.save_frame("first_frame.jpeg")
    >>> mpy.ipython_display("first_frame.jpeg")
    """
    pass