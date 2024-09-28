""" Misc. bindings to ffmpeg and ImageMagick."""
import os
import subprocess as sp
import sys
from moviepy.config import get_setting
from moviepy.tools import subprocess_call

def ffmpeg_movie_from_frames(filename, folder, fps, digits=6, bitrate='v'):
    """
    Writes a movie out of the frames (picture files) in a folder.
    Almost deprecated.
    """
    pass

def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ Makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    pass

def ffmpeg_merge_video_audio(video, audio, output, vcodec='copy', acodec='copy', ffmpeg_output=False, logger='bar'):
    """ merges video file ``video`` and audio file ``audio`` into one
        movie file ``output``. """
    pass

def ffmpeg_extract_audio(inputfile, output, bitrate=3000, fps=44100):
    """ extract the sound from a video file and save it in ``output`` """
    pass

def ffmpeg_resize(video, output, size):
    """ resizes ``video`` to new size ``size`` and write the result
        in file ``output``. """
    pass