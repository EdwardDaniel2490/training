a=[265,211,109]
b=[356,243,156]
c=[184,246,186]
d=[95,261,65]
e=[274,15,123]
f=[179,77,28]
g=[271,12,21]
h=[51,7,36]
i=[275,217,62]
j=[180,174,137]

def suma(arreglo):
    res=0
    total=0    
    res=arreglo[0]*arreglo[1]+arreglo[2]
    convertir=str(res)
    for i in convertir:
        total=total+int(i)
    return total
    
print(suma(a))
print(suma(b))
print(suma(c))
print(suma(d))
print(suma(e))
print(suma(f))
print(suma(g))
print(suma(h))
print(suma(i))
print(suma(j))
