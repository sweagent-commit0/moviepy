"""
Classes for easy interpolation of trajectories and Curves.
Requires Scipy installed.
"""
import numpy as np

class Interpolator:
    """ Poorman's linear interpolator, doesn't require Scipy. """

    def __init__(self, tt=None, ss=None, ttss=None, left=None, right=None):
        if ttss is not None:
            tt, ss = zip(*ttss)
        self.tt = 1.0 * np.array(tt)
        self.ss = 1.0 * np.array(ss)
        self.left = left
        self.right = right
        self.tmin, self.tmax = (min(tt), max(tt))

    def __call__(self, t):
        return np.interp(t, self.tt, self.ss, self.left, self.right)

class Trajectory:

    def __init__(self, tt, xx, yy):
        self.tt = 1.0 * np.array(tt)
        self.xx = np.array(xx)
        self.yy = np.array(yy)
        self.update_interpolators()

    def __call__(self, t):
        return np.array([self.xi(t), self.yi(t)])