# filename: timer.py
# author: Roy Roth (roykroth@gmail.com)
# description: Just defines a few decorators

from time import time
import numpy as np
import functools 

def append_to_docstring(to_add):
    '''
    Decorator Factory producing a decorator appending to a functions
    doc string. This is useful when creating other decorators that
    modify the behavior of the functions they decorate

    Parameters
    ----------
    to_add: str 
        String to add to the doc string of decorated function
    '''
    def _append(func):
        if not func.__doc__:
            func.__doc__ = to_add
        else:
            func.__doc__ += '\n' + to_add
        return func
    return _append

def timer(n = 10):
    '''
    Decorator Factory producing a decorator the runs the decorated
    funtion n times and reports the average execution time, as well 
    as returning the return value of the  function being timed 
    (The return value for the timed function is the value from the 
    last time the funtion is called)
   
    Parameters
    ----------
    n: int, optional (default = 10)
        The number of times to run the function.
    '''
    def _timer(func): # This is the actual decorator
        add = ('Decorated Function Returns\n' + 
               '--------------------------\n' + 
               ("{Time: average execution time,\n" +
                "Value: Undecorated Function's return value}"))
        @append_to_docstring(add)
        @functools.wraps(func) #Preserve decorated function's documentation
        def inner(*args, **kwargs):
            time_list = []
            for i in xrange(n):
                t1 = time()
                val = func(*args, **kwargs)
                elapsed = time() - t1
                time_list.append(elapsed)
            avg_time = np.array(time_list).mean()
            ret = {'Time': avg_time, 'Value': val}
            return ret
        return inner
    return _timer

