"""
Here is the current catalogue. These are meant
to be used with clip.fx. There are available as transfx.crossfadein etc.
if you load them with ``from moviepy.editor import *``
"""
from moviepy.decorators import add_mask_if_none, requires_duration
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from .CompositeVideoClip import CompositeVideoClip

@requires_duration
@add_mask_if_none
def crossfadein(clip, duration):
    """ Makes the clip appear progressively, over ``duration`` seconds.
    Only works when the clip is included in a CompositeVideoClip.
    """
    pass

@requires_duration
@add_mask_if_none
def crossfadeout(clip, duration):
    """ Makes the clip disappear progressively, over ``duration`` seconds.
    Only works when the clip is included in a CompositeVideoClip.
    """
    pass

def slide_in(clip, duration, side):
    """ Makes the clip arrive from one side of the screen.

    Only works when the clip is included in a CompositeVideoClip,
    and if the clip has the same size as the whole composition.

    Parameters
    ===========

    clip
      A video clip.

    duration
      Time taken for the clip to be fully visible

    side
      Side of the screen where the clip comes from. One of
      'top' | 'bottom' | 'left' | 'right'

    Examples
    =========

    >>> from moviepy.editor import *
    >>> clips = [... make a list of clips]
    >>> slided_clips = [CompositeVideoClip([
                            clip.fx(transfx.slide_in, duration=1, side='left')])
                        for clip in clips]
    >>> final_clip = concatenate( slided_clips, padding=-1)

    """
    pass

@requires_duration
def slide_out(clip, duration, side):
    """ Makes the clip go away by one side of the screen.

    Only works when the clip is included in a CompositeVideoClip,
    and if the clip has the same size as the whole composition.

    Parameters
    ===========

    clip
      A video clip.

    duration
      Time taken for the clip to fully disappear.

    side
      Side of the screen where the clip goes. One of
      'top' | 'bottom' | 'left' | 'right'

    Examples
    =========

    >>> from moviepy.editor import *
    >>> clips = [... make a list of clips]
    >>> slided_clips = [CompositeVideoClip([
                            clip.fx(transfx.slide_out, duration=1, side='left')])
                        for clip in clips]
    >>> final_clip = concatenate( slided_clips, padding=-1)

    """
    pass

@requires_duration
def make_loopable(clip, cross_duration):
    """ Makes the clip fade in progressively at its own end, this way
    it can be looped indefinitely. ``cross`` is the duration in seconds
    of the fade-in.  """
    pass