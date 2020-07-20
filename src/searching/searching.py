def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = (len(arr) -1)

    found = False

    while first <= last and not found:

        middle = (first + last) // 2

        if arr[middle] == target:
            found = True

        else:
            if target < arr[middle]:
                 last = middle -1

            else: 
                first = middle + 1

    return found

    # Your code here


    return -1  # not found


def insertion_sort(input_list):
    # separate the first element
    # think of it as sorted
    # no code required here / abstract step

    # for all unsorted items
    for i in range(1, len(input_list)):
        # makr the current item we are considering
        current = input_list[i]
        
        # look left until we find the proper place to insert current item
        j = i 
        while j > 0 and current < input_list[j - 1]:

            # as we are "looking left", we need to shift items to the right
            input_list[j] = input_list[j-1]
            j -= 1

        # when we've found our insertion point (j)
            # insert item
        input_list[j] = current

    return input_list 

print(insertion_sort([3,4,2,4,5,6,23]))
