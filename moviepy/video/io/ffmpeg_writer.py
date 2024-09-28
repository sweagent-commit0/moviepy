"""
On the long term this will implement several methods to make videos
out of VideoClips
"""
import os
import subprocess as sp
import numpy as np
from proglog import proglog
from moviepy.compat import DEVNULL, PY3
from moviepy.config import get_setting

class FFMPEG_VideoWriter:
    """ A class for FFMPEG-based video writing.

    A class to write videos using ffmpeg. ffmpeg will write in a large
    choice of formats.

    Parameters
    -----------

    filename
      Any filename like 'video.mp4' etc. but if you want to avoid
      complications it is recommended to use the generic extension
      '.avi' for all your videos.

    size
      Size (width,height) of the output video in pixels.

    fps
      Frames per second in the output video file.

    codec
      FFMPEG codec. It seems that in terms of quality the hierarchy is
      'rawvideo' = 'png' > 'mpeg4' > 'libx264'
      'png' manages the same lossless quality as 'rawvideo' but yields
      smaller files. Type ``ffmpeg -codecs`` in a terminal to get a list
      of accepted codecs.

      Note for default 'libx264': by default the pixel format yuv420p
      is used. If the video dimensions are not both even (e.g. 720x405)
      another pixel format is used, and this can cause problem in some
      video readers.

    audiofile
      Optional: The name of an audio file that will be incorporated
      to the video.

    preset
      Sets the time that FFMPEG will take to compress the video. The slower,
      the better the compression rate. Possibilities are: ultrafast,superfast,
      veryfast, faster, fast, medium (default), slow, slower, veryslow,
      placebo.

    bitrate
      Only relevant for codecs which accept a bitrate. "5000k" offers
      nice results in general.

    withmask
      Boolean. Set to ``True`` if there is a mask in the video to be
      encoded.

    """

    def __init__(self, filename, size, fps, codec='libx264', audiofile=None, preset='medium', bitrate=None, withmask=False, logfile=None, threads=None, ffmpeg_params=None):
        if logfile is None:
            logfile = sp.PIPE
        self.filename = filename
        self.codec = codec
        self.ext = self.filename.split('.')[-1]
        cmd = [get_setting('FFMPEG_BINARY'), '-y', '-loglevel', 'error' if logfile == sp.PIPE else 'info', '-f', 'rawvideo', '-vcodec', 'rawvideo', '-s', '%dx%d' % (size[0], size[1]), '-pix_fmt', 'rgba' if withmask else 'rgb24', '-r', '%.02f' % fps, '-an', '-i', '-']
        if audiofile is not None:
            cmd.extend(['-i', audiofile, '-acodec', 'copy'])
        cmd.extend(['-vcodec', codec, '-preset', preset])
        if ffmpeg_params is not None:
            cmd.extend(ffmpeg_params)
        if bitrate is not None:
            cmd.extend(['-b', bitrate])
        if threads is not None:
            cmd.extend(['-threads', str(threads)])
        if codec == 'libx264' and size[0] % 2 == 0 and (size[1] % 2 == 0):
            cmd.extend(['-pix_fmt', 'yuv420p'])
        cmd.extend([filename])
        popen_params = {'stdout': DEVNULL, 'stderr': logfile, 'stdin': sp.PIPE}
        if os.name == 'nt':
            popen_params['creationflags'] = 134217728
        self.proc = sp.Popen(cmd, **popen_params)

    def write_frame(self, img_array):
        """ Writes one frame in the file."""
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def ffmpeg_write_video(clip, filename, fps, codec='libx264', bitrate=None, preset='medium', withmask=False, write_logfile=False, audiofile=None, verbose=True, threads=None, ffmpeg_params=None, logger='bar'):
    """ Write the clip to a videofile. See VideoClip.write_videofile for details
    on the parameters.
    """
    pass

def ffmpeg_write_image(filename, image, logfile=False):
    """ Writes an image (HxWx3 or HxWx4 numpy array) to a file, using
        ffmpeg. """
    pass