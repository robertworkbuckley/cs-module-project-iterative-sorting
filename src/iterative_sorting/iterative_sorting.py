# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for x in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap += 1

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum):
    # Your code here
    # new = []
    if arr is []:
        return arr
    counts = [0] * (maximum + 1)
    for i in range(len(arr)): # O(n)
        value = arr[i]
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[value] = counts[value] + 1
    curr_index = 0
    for i in range(len(counts)): # O(n)
        if counts[i] > 0:
            value = counts[i]
            for x in range(value): # O(n)
                arr[curr_index] = i
                curr_index += 1
            #     new.append(i)

    return arr