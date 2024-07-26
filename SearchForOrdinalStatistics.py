"""
SerchMinMax - searching min and max for 3n/2 compare operations
because standart algorithms can searc it for 2n-2 compare operations

SearchForOrdinalStatistics - mathematical expectation time is linear

"""


def SearchMinMax(mas):
    if len(mas)%2!=0:
        min, max = mas[0], mas[0]
        for i in range(2, len(mas),2):
            if mas[i-1] > mas[i]:
                if max < mas[i-1]:
                    max = mas[i-1]
                if min > mas[i]:
                    min = mas[i]
            else:
                if max < mas[i]:
                    max = mas[i]
                if min > mas[i-1]:
                    min = mas[-1]
    else:
        if mas[0] > mas[1]:
            min = mas[1]
            max = mas[0]
        else:
            min = mas[0]

            max = mas[1]

        for i in range(3, len(mas),2):
            if mas[i-1] > mas[i]:
                if max < mas[i-1]:
                    max = mas[i-1]
                if min > mas[i]:
                    min = mas[i]
            else:
                if max < mas[i]:
                    max = mas[i]
                if min > mas[i-1]:
                    min = mas[-1]

    return min, max


def Partition(mas, p, r):
    i=p-1
    x = mas[r]
    for j in range(p, r):
        if mas[j] <= x:
            i+=1
            mas[i], mas[j] = mas[j], mas[i]
    i+=1
    mas[i], mas[r] = mas[r], mas[i]
    return i


def SearchForOrdinalStatistics(mas, p, r, i):
    if len(mas)==1:
        return mas[0]
    q = Partition(mas, p, r)
    k = q-p+1
    if k==i:
        return mas[q]
    elif k > i:
        return SearchForOrdinalStatistics(mas, p, q-1, i)
    else:
        return SearchForOrdinalStatistics(mas, q+1, r, i-k)


mas = [1,2,345,32,-10]
print(SearchMinMax(mas))