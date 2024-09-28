"""
This file is meant to make it easy to load the main features of
MoviePy by simply typing:

>>> from moviepy.editor import *

In particular it will load many effects from the video.fx and audio.fx
folders and turn them into VideoClip methods, so that instead of
>>> clip.fx( vfx.resize, 2 ) # or equivalently vfx.resize(clip, 2)
we can write
>>> clip.resize(2)

It also starts a PyGame session (if PyGame is installed) and enables
clip.preview().
"""
import os
import sys
import imageio
if os.getenv('FFMPEG_BINARY') is None:
    if sys.version_info < (3, 4):
        imageio.plugins.ffmpeg.download()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from .video.io.VideoFileClip import VideoFileClip
from .video.io.ImageSequenceClip import ImageSequenceClip
from .video.io.downloader import download_webfile
from .video.VideoClip import VideoClip, ImageClip, ColorClip, TextClip
from .video.compositing.CompositeVideoClip import CompositeVideoClip, clips_array
from .video.compositing.concatenate import concatenate_videoclips, concatenate
from .audio.AudioClip import AudioClip, CompositeAudioClip, concatenate_audioclips
from .audio.io.AudioFileClip import AudioFileClip
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import moviepy.video.compositing.transitions as transfx
import moviepy.video.tools as videotools
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from .video.io.html_tools import ipython_display
from .tools import cvsecs
try:
    from .video.io.sliders import sliders
except ImportError:
    pass
for method in ['afx.audio_fadein', 'afx.audio_fadeout', 'afx.audio_normalize', 'afx.volumex', 'transfx.crossfadein', 'transfx.crossfadeout', 'vfx.crop', 'vfx.fadein', 'vfx.fadeout', 'vfx.invert_colors', 'vfx.loop', 'vfx.margin', 'vfx.mask_and', 'vfx.mask_or', 'vfx.resize', 'vfx.rotate', 'vfx.speedx']:
    exec('VideoClip.%s = %s' % (method.split('.')[1], method))
for method in ['afx.audio_fadein', 'afx.audio_fadeout', 'afx.audio_loop', 'afx.audio_normalize', 'afx.volumex']:
    exec('AudioClip.%s = %s' % (method.split('.')[1], method))
VideoClip.ipython_display = ipython_display
AudioClip.ipython_display = ipython_display
try:
    from moviepy.video.io.preview import show, preview
except ImportError:

    def preview(self, *args, **kwargs):
        """NOT AVAILABLE : clip.preview requires Pygame installed."""
        pass

    def show(self, *args, **kwargs):
        """NOT AVAILABLE : clip.show requires Pygame installed."""
        pass
VideoClip.preview = preview
VideoClip.show = show
try:
    from moviepy.audio.io.preview import preview
except ImportError:

    def preview(self, *args, **kwargs):
        """ NOT AVAILABLE : clip.preview requires Pygame installed."""
        pass
AudioClip.preview = preview