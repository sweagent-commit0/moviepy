import numpy as np
from moviepy.decorators import audio_video_fx

@audio_video_fx
def audio_fadein(clip, duration):
    """ Return an audio (or video) clip that is first mute, then the
        sound arrives progressively over ``duration`` seconds. """
    pass