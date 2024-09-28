"""
This module contains different functions for tracking objects in videos,
manually or automatically. The tracking functions return results under
the form:  ``( txy, (fx,fy) )`` where txy is of the form [(ti, xi, yi)...]
and (fx(t),fy(t)) give the position of the track for all times t (if the
time t is out of the time bounds of the tracking time interval
fx and fy return the position of the object at the start or at the end
of the tracking time interval).
"""
import numpy as np
from moviepy.decorators import convert_to_seconds, use_clip_fps_by_default
from ..io.preview import imdisplay
from .interpolators import Trajectory
try:
    import cv2
    autotracking_possible = True
except:
    autotracking_possible = False

@convert_to_seconds(['t1', 't2'])
@use_clip_fps_by_default
def manual_tracking(clip, t1=None, t2=None, fps=None, nobjects=1, savefile=None):
    """
    Allows manual tracking of an object(s) in the video clip between
    times `t1` and `t2`. This displays the clip frame by frame
    and you must click on the object(s) in each frame. If ``t2=None``
    only the frame at ``t1`` is taken into account.
    
    Returns a list [(t1,x1,y1),(t2,x2,y2) etc... ] if there is one
    object per frame, else returns a list whose elements are of the 
    form (ti, [(xi1,yi1), (xi2,yi2), ...] )
    
    Parameters
    -------------

    t1,t2:
      times during which to track (defaults are start and
      end of the clip). t1 and t2 can be expressed in seconds
      like 15.35, in (min, sec), in (hour, min, sec), or as a
      string: '01:03:05.35'.
    fps:
      Number of frames per second to freeze on. If None, the clip's
      fps attribute is used instead.
    nobjects:
      Number of objects to click on each frame.
    savefile:
      If provided, the result is saved to a file, which makes
      it easier to edit and re-use later.

    Examples
    ---------
    
    >>> from moviepy.editor import VideoFileClip
    >>> from moviepy.video.tools.tracking import manual_tracking
    >>> clip = VideoFileClip("myvideo.mp4")
    >>> # manually indicate 3 trajectories, save them to a file
    >>> trajectories = manual_tracking(clip, t1=5, t2=7, fps=5,
                                       nobjects=3, savefile="track.txt")
    >>> # ...
    >>> # LATER, IN ANOTHER SCRIPT, RECOVER THESE TRAJECTORIES
    >>> from moviepy.video.tools.tracking import Trajectory
    >>> traj1, traj2, traj3 = Trajectory.load_list('track.txt')
    >>> # If ever you only have one object being tracked, recover it with
    >>> traj, =  Trajectory.load_list('track.txt')
    
    """
    pass

def findAround(pic, pat, xy=None, r=None):
    """
    find image pattern ``pat`` in ``pic[x +/- r, y +/- r]``.
    if xy is none, consider the whole picture.
    """
    pass

def autoTrack(clip, pattern, tt=None, fps=None, radius=20, xy0=None):
    """
    Tracks a given pattern (small image array) in a video clip.
    Returns [(x1,y1),(x2,y2)...] where xi,yi are
    the coordinates of the pattern in the clip on frame i.
    To select the frames you can either specify a list of times with ``tt``
    or select a frame rate with ``fps``.
    This algorithm assumes that the pattern's aspect does not vary much
    and that the distance between two occurences of the pattern in
    two consecutive frames is smaller than ``radius`` (if you set ``radius``
    to -1 the pattern will be searched in the whole screen at each frame).
    You can also provide the original position of the pattern with xy0.
    """
    pass