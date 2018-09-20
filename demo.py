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

@profile
def function():
    lst = []
    for i in range (1_000_000):
        lst.append(i)
    return lst

@profile
def funcion_with_shortcut():
    lst = []
    append = lst.append()
    for i in range(1_000_000):
        append(i)
    return lst

@profile
def function_list_comprehension():
    return [i for i in range (1_000_000)]

@profile
def function_convert_to_list():
    return list(range(1_000_000))

@profile
def get_random_user():
    response = requests.get('https://randomuser.me/api')
if __name__== '__main__':
    for i in range(10):
        my_func()
    function()
    function_with_shortcut()
    function_list_comprehension()
    function_convert_to_list()
    get random_user()