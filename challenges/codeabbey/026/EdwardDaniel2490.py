a = [1746, 1674]
b = [90, 2]
c = [87, 615]
d = [7452, 91]
e = [2262, 2288]
f = [921, 5472]
g = [2304, 1692]
h = [2379, 1647]
i = [4, 1]
j = [7, 78]
k = [43, 56]
l = [43, 85]
m = [1575, 2275]
n = [259, 5558]
o = [1248, 1488]
p = [601, 753]
q = [1615, 1539]
def mini(en):
  while en[0] != en[1]:
    if en[0] > en[1]:
      en[0] -= en[1]
    else:
      en[1] -= en[0]
  return en[0]
def maxi(en):
  lcm = (en[0] * en[1]) / mini(en)
  print("(" + str(mini(en)) + " " + str(lcm) + ")")
maxi(a)
maxi(b)
maxi(c)
maxi(d)
maxi(e)
maxi(f)
maxi(g)
maxi(h)
maxi(i)
maxi(j)
maxi(k)
maxi(l)
maxi(m)
maxi(n)
maxi(o)
maxi(p)
maxi(q)
