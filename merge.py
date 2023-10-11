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

#example run
if __name__ == "__main__":
    firstList = [1,3,5,7,9]
    secondList = [2,4,6,8,10]
    result = merge_list(firstList, secondList)
    print(result)  # This will print [1, 2, 3, 4, 5, 6, 7]