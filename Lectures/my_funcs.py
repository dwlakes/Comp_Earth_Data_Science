## module my_funcs

def gimme_pi():  
    """
    Returns the value of pi.
    """
    
    return 3.141592653589793

def degrees_to_radians(degrees):  
    """
    Converts degrees to radians.
    """
    
    return degrees * 3.141592653589793 / 180.0

def print_args(*args):
    """
    Prints out argument list.
    """
    
    print ('The arguments were:')
    for arg in args:
        print(arg)
