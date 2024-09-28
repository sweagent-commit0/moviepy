"""
Misc. useful functions that can be used at many places in the program.
"""
import os
import subprocess as sp
import sys
import warnings
import proglog
from .compat import DEVNULL

def sys_write_flush(s):
    """ Writes and flushes without delay a text in the console """
    pass

def verbose_print(verbose, s):
    """ Only prints s (with sys_write_flush) if verbose is True."""
    pass

def subprocess_call(cmd, logger='bar', errorprint=True):
    """ Executes the given subprocess command.
    
    Set logger to None or a custom Proglog logger to avoid printings.
    """
    pass

def is_string(obj):
    """ Returns true if s is string or string-like object,
    compatible with Python 2 and Python 3."""
    pass

def cvsecs(time):
    """ Will convert any time into seconds. 
    
    If the type of `time` is not valid, 
    it's returned as is. 

    Here are the accepted formats::

    >>> cvsecs(15.4)   # seconds 
    15.4 
    >>> cvsecs((1, 21.5))   # (min,sec) 
    81.5 
    >>> cvsecs((1, 1, 2))   # (hr, min, sec)  
    3662  
    >>> cvsecs('01:01:33.045') 
    3693.045
    >>> cvsecs('01:01:33,5')    # coma works too
    3693.5
    >>> cvsecs('1:33,5')    # only minutes and secs
    99.5
    >>> cvsecs('33.5')      # only secs
    33.5
    """
    pass

def deprecated_version_of(f, oldname, newname=None):
    """ Indicates that a function is deprecated and has a new name.

    `f` is the new function, `oldname` the name of the deprecated
    function, `newname` the name of `f`, which can be automatically
    found.

    Returns
    ========

    f_deprecated
      A function that does the same thing as f, but with a docstring
      and a printed message on call which say that the function is
      deprecated and that you should use f instead.

    Examples
    =========

    >>> # The badly named method 'to_file' is replaced by 'write_file'
    >>> class Clip:
    >>>    def write_file(self, some args):
    >>>        # blablabla
    >>>
    >>> Clip.to_file = deprecated_version_of(Clip.write_file, 'to_file')
    """
    pass
extensions_dict = {'mp4': {'type': 'video', 'codec': ['libx264', 'libmpeg4', 'aac']}, 'ogv': {'type': 'video', 'codec': ['libtheora']}, 'webm': {'type': 'video', 'codec': ['libvpx']}, 'avi': {'type': 'video'}, 'mov': {'type': 'video'}, 'ogg': {'type': 'audio', 'codec': ['libvorbis']}, 'mp3': {'type': 'audio', 'codec': ['libmp3lame']}, 'wav': {'type': 'audio', 'codec': ['pcm_s16le', 'pcm_s24le', 'pcm_s32le']}, 'm4a': {'type': 'audio', 'codec': ['libfdk_aac']}}
for ext in ['jpg', 'jpeg', 'png', 'bmp', 'tiff']:
    extensions_dict[ext] = {'type': 'image'}