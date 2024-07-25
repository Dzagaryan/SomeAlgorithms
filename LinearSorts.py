"""
1)CountingSort - input data should be integer numbers and in (0, k), k - some integer number
so mas[i] <= k for all i and it should be integer.

2)RadixSort - input data is some numbers with d digits.
Example: d=3, input = [733,834,535,646]

3)BucketSort - input data should have uniform distribution law and input data in (0;1)
"""


def CountingSort(mas, k):
    C = [0 for _ in range(k+1)]
    B = [0 for _ in range(0, len(mas))]
    for j in range(0,len(mas)):
        C[mas[j]]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for j in range(len(mas)-1, -1,-1):
        B[C[mas[j]]-1] = mas[j]
        C[mas[j]]-=1
    return B


mas = [5,13,12,5]
print(CountingSort(mas, 13))


def CountingSortForRadix(mas, digit):
    k=9
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(0, len(mas))]
    for j in range(0, len(mas)):
        C[int(str(mas[j])[::-1][digit-1])] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for j in range(len(mas) - 1, -1, -1):
        B[C[int(str(mas[j])[::-1][digit-1])] - 1] = mas[j]
        C[int(str(mas[j])[::-1][digit-1])] -= 1
    return B


def RadixSort(mas, digits):
    for i in range(1, digits+1):
        mas = CountingSortForRadix(mas, i)
    return mas


mas = [13,23,53,10,23]
print(RadixSort(mas, 2))


def BucketSort(mas):
    Bucket = []
    n = len(mas)
    for i in range(n):
        Bucket.append([])
    for j in range(n):
        Bucket[int(mas[j]*n)].append(mas[j])
    for i in range(n):
        Bucket[i].sort()

    return sum(Bucket)
