import random

#creates a random array
def random_array(array):
    rand = random.randint(0, 100)
    for i in range(0, rand):
        array.append(random.randint(0, 1000))

# Constant Time O(1)
def addtolist(list_a, item):
    list_a.append(item)

# linear search O(n)
def linearsearch(target, array):
    count = 0
    found = False
    for item in array:
        count += 1
        if item == target:
            print(f'Item was found, count = {count}')
            found = True

    if found == False:
        print('Item was not found')

#Bubble sort O(n^2)
def bubblesort(array):
    array_len = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, array_len):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
    return array

def mergesort(array,target):
    low_index = 0
    high_index = len(array) - 1

    while low_index <= high_index:
        midpoint = low_index + (high_index - low_index) // 2
        midpoint_value = array[midpoint]
        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            high_index = midpoint - 1
        else:
           low_index = midpoint + 1
    return None

list1 = [2, 6, 7, 54, 23, 423, 43, 556, 2, 111, 322, 32, 554, 757788, 3443, 53, 59]

#test for linear search O(n)
#linearsearch(target=23, array=list1)

#test for O(1)
#addtolist(list1, 6)
#print(list1)

#test for bubble sort O(n^2)
print(bubblesort(list1))
list3 = [1,2,3,4,5,6,7,8]
print(list3)
print(mergesort(list3, 6))

