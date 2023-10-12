#Question 8: log.py

import time

def timestamp(input): #created a decorator called timestamp 

    def wrapper(*args, **kwargs):

        print(time.ctime())
        input(*args, **kwargs)

    return wrapper    

