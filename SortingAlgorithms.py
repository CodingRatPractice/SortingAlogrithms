from random import randint
from timeit import repeat

ARRAY_LENGTH = 1000

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

def run_sorting_algorithm(algorithm, array):

    # Code supplied by: https://realpython.com/sorting-algorithms-python/ 

    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

# Compare value with neighbor, if your value is bigger swap positions
def bubble_sort(array):


    loops = len(array)

    for array_index in range(loops):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        for j in range(loops - array_index - 1):
            #Compare value with neighbor
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                #sorting occured, so not sorted
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Works backwards in the array to find the items correct position
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for item in range(1, len(array)):
        key_item = array[item]
        reverseCount = item - 1

        while reverseCount >= 0 and array[reverseCount] > key_item:
            # moves the key item position by one
            array[reverseCount + 1] = array[reverseCount]
            reverseCount -= 1

        # When loop is satisfied set the final key item position
        array[reverseCount + 1] = key_item

    return array

if __name__ == "__main__":
    run_sorting_algorithm(algorithm="insertion_sort", array=array)