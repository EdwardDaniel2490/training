a = [3, 8, 89]
b = [7, 20, 57]
c = [14, 2, 29]
d = [5, 10, 28]
e = [9, 3, 99]
f = [10, 6, 51]
g = [29, 13, 23]
h = [11, 15, 49]
def progres(entrada):
    total = 0
    result = entrada[0]
    for i in range(entrada[2] - 1):
        result = result + entrada[1]
        total = result + total
    print(total + entrada[0])
progres(a)
progres(b)
progres(c)
progres(d)
progres(e)
progres(f)
progres(g)
progres(h)
