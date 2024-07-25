def Partition(mas, p, r):
    x = mas[r]
    i=p-1
    for j in range(p, r):
        if mas[j] <= x:
            i+=1
            mas[j], mas[i] = mas[i], mas[j]
    mas[i+1], mas[r] = mas[r], mas[i+1]
    return i+1


def QuickSort(mas, p, r):
    if p < r:
        q = Partition(mas, p, r)
        QuickSort(mas, p, q-1)
        QuickSort(mas, q+1, r)


mas = [345,32,135,124,45,24,63]
QuickSort(mas,0, len(mas)-1)
print(*mas)