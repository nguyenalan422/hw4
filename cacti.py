#Question 9: Create a program to evaluate cacti planting

# cacti.py

def cacti_number(input):
    def cacti(arr):

        all = 0

        for row in arr:
            for cell in row:
                if cell == 1:
                    all += 1
        return all
    return cacti