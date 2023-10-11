#Question 2: merge.py

def merge_list(firstList, secondList):
    #Initially, we must determine that firstList and secondList are lists
    if not isinstance(firstList, list) or not isinstance(secondList, list):
        raise TypeError("Error, both have to be lists!")
    
    #Now, we shall merge the two lists 
    merged = firstList + secondList 

    #We use an algorithm to sort the merge list 
    for i in range(len(merged)):
        for j in range (0, len(merged) - i - 1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
   
    return merged
<<<<<<< HEAD

=======
>>>>>>> c92abe198ced218369ede59c23fb4deef07d0314
