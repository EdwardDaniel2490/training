p1=[15317,6741,458,12447,6595,7395,13254,14273,3803,11794]
p2=[5883,5667,3685,6283,8118,7911,7813,919,2224,2840,985,7065,779,6499,57]
p3=[3885,5641,5685,7255,5870,3716,2361,1375,2151,1305,3276,8048]
p4=[359,407,321,240,402,303]
p5=[14143,12577,273,11889,14134,13269,12001,9165,9321]
p6=[135,48,494,367,195,68,502]
p7=[1969,1314,1451,1355,891,686,264,449,1897,1127]
p8=[2601,1083,4220,1475,7717,2028]
p9=[931,2022,1585,1120,1949,1004,1899,172,961,956,1261,881,222]
p10=[139,169,57,196,150,198,225,96]
p11=[228,69,244,36,2]
p12=[4073,966,564,3875,2972,265,122,796,2177,2644]
p13=[3971,2933,746,2572,3835,3866,871,2894,3363,2404,3253]
p14=[127,1601,1256,142,500,418,130,982,700,19,420,832,80,818]
def calcularPromedio(prom):
    promedio=0
    for i in range(len(prom)):
        promedio=promedio+prom[i]
    return round(promedio/len(prom))

print(calcularPromedio(p1))
print(calcularPromedio(p2))
print(calcularPromedio(p3))
print(calcularPromedio(p4))
print(calcularPromedio(p5))
print(calcularPromedio(p6))
print(calcularPromedio(p7))
print(calcularPromedio(p8))
print(calcularPromedio(p9))
print(calcularPromedio(p10))
print(calcularPromedio(p11))
print(calcularPromedio(p12))
print(calcularPromedio(p13))
print(calcularPromedio(p14))
