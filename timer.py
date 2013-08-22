# filename: timer.py
# author: Roy Roth (roykroth@gmail.com)


from time import time, sleep
import numpy as np
import functools 
def timer(n = 10):
    '''
    Decorator Factory producing a decorator the runs the decorated
    funtion n times and reports the average execution time, as well 
    as returning the return value of the  function being timed 
    (The return value for the timed function is the value from the 
    last time the funtion is called)
   
    Parameters
    ----------
    n: the number of times to run the function. Optional, default: 10

    Returns
    -------
    decorator
    '''
    def _timer(func): # This is the actual decorator
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

if __name__ == '__main__':
    @timer(10)
    def f(x):
        '''
        X's documentation
        '''
        a = np.arange(x)
        b = a**2
        return b.sum()