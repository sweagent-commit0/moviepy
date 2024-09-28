"""
all decorators used in moviepy go there
"""
import decorator
from moviepy.tools import cvsecs

@decorator.decorator
def outplace(f, clip, *a, **k):
    """ Applies f(clip.copy(), *a, **k) and returns clip.copy()"""
    pass

@decorator.decorator
def convert_masks_to_RGB(f, clip, *a, **k):
    """ If the clip is a mask, convert it to RGB before running the function """
    pass

@decorator.decorator
def apply_to_mask(f, clip, *a, **k):
    """ This decorator will apply the same function f to the mask of
        the clip created with f """
    pass

@decorator.decorator
def apply_to_audio(f, clip, *a, **k):
    """ This decorator will apply the function f to the audio of
        the clip created with f """
    pass

@decorator.decorator
def requires_duration(f, clip, *a, **k):
    """ Raise an error if the clip has no duration."""
    pass

@decorator.decorator
def audio_video_fx(f, clip, *a, **k):
    """ Use an audio function on a video/audio clip
    
    This decorator tells that the function f (audioclip -> audioclip)
    can be also used on a video clip, at which case it returns a
    videoclip with unmodified video and modified audio.
    """
    pass

def preprocess_args(fun, varnames):
    """ Applies fun to variables in varnames before launching the function """
    pass

def convert_to_seconds(varnames):
    """Converts the specified variables to seconds"""
    pass

@decorator.decorator
def add_mask_if_none(f, clip, *a, **k):
    """ Add a mask to the clip if there is none. """
    pass

@decorator.decorator
def use_clip_fps_by_default(f, clip, *a, **k):
    """ Will use clip.fps if no fps=... is provided in **k """
    pass