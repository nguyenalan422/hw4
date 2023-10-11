#Question 1: ladder.py
def my_steps(s):
    if s < 1 or s > 25:                                                         #if the number of steps is out of bounds 
        raise ValueError('The input you put is out of bounds!')      
               #Throw an execption 
    elif s == 1:                                                                #If s = 1, then we return 1
        return 1
    
    elif s == 2:
        return 2
    
    else:
        return my_steps(s-1) + my_steps(s-2)
    