a = 120631536
b = 56998
c = 58080
d = 917795379
e = 11
f = 167
g = 5334
h = 25750
i = 216
j = 17
k = 74
l = 1
m = 234594
n = 1740
o = 3592
p = 16
q = 10778297
r = 8
s = 11933
t = 26
u = 6
v = 31
w = 8
x = 21338
y = 10
z = 37158281
aa = 128
bb = 1544
cc = 89062599
dd = 136841
ee = 97810
ff = 20723
gg = 5137
def wsumdigit(entero):    
    convertir = str(entero)
    lst = []
    res = 0
    result = 0
    for i in convertir:
        lst.append(int(i))
    if len(lst) > 0:
        for j in range(len(lst)):
             res = lst[j] * (j + 1)
             result = result + res
        print(result)
    else:
        print(entero)
wsumdigit(a)
wsumdigit(b)
wsumdigit(c)
wsumdigit(d)
wsumdigit(e)
wsumdigit(f)
wsumdigit(g)
wsumdigit(h)
wsumdigit(i)
wsumdigit(j)
wsumdigit(k)
wsumdigit(l)
wsumdigit(m)
wsumdigit(n)
wsumdigit(o)
wsumdigit(p)
wsumdigit(q)
wsumdigit(r)
wsumdigit(s)
wsumdigit(t)
wsumdigit(u)
wsumdigit(v)
wsumdigit(w)
wsumdigit(x)
wsumdigit(y)
wsumdigit(z)
wsumdigit(aa)
wsumdigit(bb)
wsumdigit(cc)
wsumdigit(dd)
wsumdigit(ee)
wsumdigit(ff)
wsumdigit(gg)
