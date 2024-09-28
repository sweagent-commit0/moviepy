import numpy as np

def find_audio_period(aclip, t_min=0.1, t_max=2, t_res=0.01):
    """ Finds the period, in seconds of an audioclip.
    
    The beat is then given by bpm = 60/T

    t_min and _tmax are bounds for the returned value, t_res
    is the numerical precision
    """
    pass