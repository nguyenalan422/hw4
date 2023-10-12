#Question 7: Create a printing decorator 

def allcaps(input):
    def wrapper():
        answer = input()
        return answer.upper()
    return wrapper