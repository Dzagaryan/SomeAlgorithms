import random

def Parent(i):
    return i//2


def Left(i):
    return 2*i


def Right(i):
    return 2*i+1


def MaxHeapify(mas, i, HeapSize):
    l = Left(i)
    r = Right(i)
    if l <= HeapSize and mas[l] > mas[i]:
        largest = l
    else: largest = i
    if r <= HeapSize and mas[r] > mas[largest]:
        largest = r
    if largest != i:
        mas[largest], mas[i] = mas[i], mas[largest]
        MaxHeapify(mas, largest, HeapSize)


def BuildMAxHeap(mas, HeapSize):
    for i in range(len(mas)//2,0,-1):
        MaxHeapify(mas, i, HeapSize)


def HeapSort(mas):
    BuildMAxHeap(mas, len(mas)-1)
    HeapSize = len(mas)-1
    for i in range(len(mas)-1, 1,-1):
        mas[i], mas[1] = mas[1], mas[i]
        HeapSize-=1
        MaxHeapify(mas, 1, HeapSize)


mas = [random.randrange(10,100) for i in range(10)]
print(mas)
mas2 = [-100]+mas
HeapSort(mas2)
mas2.pop(0)
print(mas2)