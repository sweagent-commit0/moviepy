import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

def sliders(f, sliders_properties, wait_for_validation=False):
    """ A light GUI to manually explore and tune the outputs of 
        a function.
        slider_properties is a list of dicts (arguments for Slider )
        
        def volume(x,y,z):
            return x*y*z
    
        intervals = [ { 'label' :  'width',  'valmin': 1 , 'valmax': 5 },
                  { 'label' :  'height',  'valmin': 1 , 'valmax': 5 },
                  { 'label' :  'depth',  'valmin': 1 , 'valmax': 5 } ]
        inputExplorer(volume,intervals)
    """
    pass