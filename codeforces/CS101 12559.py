#CS101 12559
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j]+array[j+1] > array[j+1]+array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

n=int(input())
l=input().split()
sortl=bubble_sort(l)
print(''.join([str(x) for x in reversed(sortl)]),''.join([str(x) for x in sortl]))