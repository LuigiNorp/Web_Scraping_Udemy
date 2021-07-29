var1 = 20
var2 = 30
var3 = 40

res1 = (not (var1 > 30))
res2 = not var2 > -30
res3 = ((var3 == 50 or var2 > 10) and var1 < 90)

resultado = ((res1 != res2) and (var1 > res2 + res1))
# Suma: falso + verdadero = 1
# resultado = (verdadero) and (20 > 1)
# resultado = verdadero and verdadero
# resultado = verdadero

print (resultado)


l = [10, 30, 50, 70]
l += l[-1:-3]
print (l)   #No es posible hacer slicing a la derecha

cadena = "anita lava la tina"
tmp = []
for c in cadena:
    tmp.append(c)
tmp.reverse()
nuevaCadena = "".join(tmp)
print (nuevaCadena)