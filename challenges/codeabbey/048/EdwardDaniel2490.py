a = [29, 115, 380, 334, 20, 798, 16914, 9684, 15, 25, 63, 204, 232, 43, 1152, 22086, 21, 2773, 49, 17, 49, 92, 170, 166, 188]
for i in range(len(a)):
    contador = 0
    while a[i] != 1:
        contador += 1
        if a[i] % 2:
            a[i] = 3 * a[i] + 1
        else:
            a[i] /= 2
    print(contador)
