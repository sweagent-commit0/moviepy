import numpy as np
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.tools import deprecated_version_of
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.on_color import on_color
from moviepy.video.VideoClip import ColorClip, VideoClip
try:
    reduce
except NameError:
    from functools import reduce

def concatenate_videoclips(clips, method='chain', transition=None, bg_color=None, ismask=False, padding=0):
    """ Concatenates several video clips

    Returns a video clip made by clip by concatenating several video clips.
    (Concatenated means that they will be played one after another).

    There are two methods:

    - method="chain": will produce a clip that simply outputs
      the frames of the succesive clips, without any correction if they are
      not of the same size of anything. If none of the clips have masks the
      resulting clip has no mask, else the mask is a concatenation of masks
      (using completely opaque for clips that don't have masks, obviously).
      If you have clips of different size and you want to write directly the
      result of the concatenation to a file, use the method "compose" instead.

    - method="compose", if the clips do not have the same
      resolution, the final resolution will be such that no clip has
       to be resized.
       As a consequence the final clip has the height of the highest
       clip and the width of the widest clip of the list. All the
       clips with smaller dimensions will appear centered. The border
       will be transparent if mask=True, else it will be of the
       color specified by ``bg_color``.

    The clip with the highest FPS will be the FPS of the result clip.

    Parameters
    -----------
    clips
      A list of video clips which must all have their ``duration``
      attributes set.
    method
      "chain" or "compose": see above.
    transition
      A clip that will be played between each two clips of the list.

    bg_color
      Only for method='compose'. Color of the background.
      Set to None for a transparent clip

    padding
      Only for method='compose'. Duration during two consecutive clips.
      Note that for negative padding, a clip will partly play at the same
      time as the clip it follows (negative padding is cool for clips who fade
      in on one another). A non-null padding automatically sets the method to
      `compose`.

    """
    pass
concatenate = deprecated_version_of(concatenate_videoclips, oldname='concatenate')