
def bubbles(l):
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - i - 1):
            if l[j + 1] < l[j]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print (bubbles(l))