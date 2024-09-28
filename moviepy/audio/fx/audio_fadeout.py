import numpy as np
from moviepy.decorators import audio_video_fx, requires_duration

@audio_video_fx
@requires_duration
def audio_fadeout(clip, duration):
    """ Return a sound clip where the sound fades out progressively
        over ``duration`` seconds at the end of the clip. """
    pass