# Starts with element i at index 1 and compares with elements j (sorted part of the array),
# then puts element i in its correct position.
def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array