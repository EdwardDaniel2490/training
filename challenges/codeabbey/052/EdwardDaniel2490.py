import math
a = [216, 405, 446]
b = [465, 248, 527]
c = [40, 30, 56]
d = [162, 216, 244]
e = [1320, 385, 1428]
f = [984, 287, 1065]
g = [1632, 476, 1679]
h = [405, 972, 1045]
i = [231, 792, 848]
j = [1128, 329, 1150]
k = [1920, 560, 1924]
l = [264, 77, 275]
m = [1164, 485, 1188]
n = [32, 60, 64]
o = [705, 376, 728]
p = [768, 320, 791]
q = [240, 180, 300]
r = [552, 161, 587]
s = [445, 1068, 1080]
t = [504, 210, 546]
u = [195, 260, 337]
def triangulos(en):
  triangulo = en[0] ** 2 + en[1] ** 2 - en[2] ** 2
  if triangulo == 0:
    print("R")
  elif triangulo < 0:
    print("O")
  elif triangulo > 0:
    print("A")
triangulos(a)
triangulos(b)
triangulos(c)
triangulos(d)
triangulos(e)
triangulos(f)
triangulos(g)
triangulos(h)
triangulos(i)
triangulos(j)
triangulos(k)
triangulos(l)
triangulos(m)
triangulos(n)
triangulos(o)
triangulos(p)
triangulos(q)
triangulos(r)
triangulos(s)
triangulos(t)
triangulos(u)
