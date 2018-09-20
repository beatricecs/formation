import requests
import functools
from datetime import datetime
from time import strftime

def debug(active=True):
    def decorator(function):
        @functools.wraps(function) # pour pouvoir avoi les documentations et d'autre infos mais pas obligatoire
        def wrapper(*args, **kwargs):
            #print ("function", function.__name__)
            #print ("args= ", args)
            result = function(*args, **kwargs)
            if active:
                print("function", function.__name__)
                print("args: ", args)
                print("kwargs: ", kwargs)
                print (result)
            return result
        return wrapper
    return decorator

def time_function(function):
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = function()
        t2 = datetime.now()
        t3 = t2-t1
        print(t1)
        print(t2)

        return t3
    return wrapper

@debug(active=True)
@time_function
def get_user():
    response = requests.get('https://randomuser.me/api')
    return response.json()

get_user()