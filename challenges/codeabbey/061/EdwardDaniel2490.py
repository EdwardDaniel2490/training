a = [144824, 164343, 199128, 150437, 158384, 138094, 150203, 190946, 160196, 146366, 124514]
def primos(n):
  return ([2] + [x for x in range(3, n + 1, 2) if not [y for y in range(3, int(x ** 0.5) + 1, 2) if (float(x) / y).is_integer()]]) if n >= 2 else []
def imprimir(a):
  c =primos(2750200)
  print(len(c))
  print(c[a[0]-1])
  print(c[a[1]-1])
  print(c[a[2]-1])
  print(c[a[3]-1])
  print(c[a[4]-1])
  print(c[a[5]-1])
  print(c[a[6]-1])
  print(c[a[7]-1])
  print(c[a[8]-1])
  print(c[a[9]-1])
  print(c[a[10]-1])
imprimir(a)
