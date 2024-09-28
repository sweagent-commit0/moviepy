import os
import subprocess as sp
import warnings
import numpy as np
from moviepy.compat import DEVNULL, PY3
from moviepy.config import get_setting
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos

class FFMPEG_AudioReader:
    """
    A class to read the audio in either video files or audio files
    using ffmpeg. ffmpeg will read any audio and transform them into
    raw data.

    Parameters
    ------------

    filename
      Name of any video or audio file, like ``video.mp4`` or
      ``sound.wav`` etc.

    buffersize
      The size of the buffer to use. Should be bigger than the buffer
      used by ``to_audiofile``

    print_infos
      Print the ffmpeg infos on the file being read (for debugging)

    fps
      Desired frames per second in the decoded signal that will be
      received from ffmpeg

    nbytes
      Desired number of bytes (1,2,4) in the signal that will be
      received from ffmpeg

    """

    def __init__(self, filename, buffersize, print_infos=False, fps=44100, nbytes=2, nchannels=2):
        self.filename = filename
        self.nbytes = nbytes
        self.fps = fps
        self.f = 's%dle' % (8 * nbytes)
        self.acodec = 'pcm_s%dle' % (8 * nbytes)
        self.nchannels = nchannels
        infos = ffmpeg_parse_infos(filename)
        self.duration = infos['duration']
        if 'video_duration' in infos:
            self.duration = infos['video_duration']
        else:
            self.duration = infos['duration']
        self.infos = infos
        self.proc = None
        self.nframes = int(self.fps * self.duration)
        self.buffersize = min(self.nframes + 1, buffersize)
        self.buffer = None
        self.buffer_startframe = 1
        self.initialize()
        self.buffer_around(1)

    def initialize(self, starttime=0):
        """ Opens the file, creates the pipe. """
        pass

    def seek(self, pos):
        """
        Reads a frame at time t. Note for coders: getting an arbitrary
        frame in the video with ffmpeg can be painfully slow if some
        decoding has to be done. This function tries to avoid fectching
        arbitrary frames whenever possible, by moving between adjacent
        frames.
        """
        pass

    def buffer_around(self, framenumber):
        """
        Fills the buffer with frames, centered on ``framenumber``
        if possible
        """
        pass

    def __del__(self):
        self.close_proc()