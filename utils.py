def printProps(props, name, var):
    """
    Print the properties of var
    Args:
        props: a tuple of functions to call on var
        name: string to be printed (name of var)
        var:  variable of interest. This can be any type, but currently restricted to function objects without arguments
    Returns: 
        None
    """   
    ## todo: calculate the max length of each field and format accordingly
    for p in props:
        print("{:>4} of {} is {}".format(p.__name__, name, p(var))) 