#from memory_profiler import profile

MEMORY_PROFILING = True # on peut passer une variable environement os.getenv

def activate(func):
    if MEMORY_PROFILING:
        return profile(func)
    else:
        return func

#@activate
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 **7)
    del b
    return a

if __name__== '__main__':
    for i in range(10):
        my_func()