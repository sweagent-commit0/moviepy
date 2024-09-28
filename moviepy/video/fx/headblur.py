import numpy as np
try:
    import cv2
    headblur_possible = True
    if cv2.__version__ >= '3.0.0':
        cv2.CV_AA = cv2.LINE_AA
except:
    headblur_possible = False

def headblur(clip, fx, fy, r_zone, r_blur=None):
    """
    Returns a filter that will blurr a moving part (a head ?) of
    the frames. The position of the blur at time t is
    defined by (fx(t), fy(t)), the radius of the blurring
    by ``r_zone`` and the intensity of the blurring by ``r_blur``.
    Requires OpenCV for the circling and the blurring.
    Automatically deals with the case where part of the image goes
    offscreen.
    """
    pass
if not headblur_possible:
    doc = headblur.__doc__
    headblur.__doc__ = doc