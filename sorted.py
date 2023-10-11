# #Question 3: sorted.py

def reverse_sort_dictionary(person):
    if not isinstance(person, dict):
        raise TypeError("Given name should be in dictionary")

    # Sorting in reverse order based in it's keys
    SortedPerson = sorted(person.items(), key = lambda x: x[0], reverse = True)

    # Now we will take the Name and Number of the person and transfer into list 
    answer = [(personName, data[0]) for personName, data in SortedPerson]
    return answer
