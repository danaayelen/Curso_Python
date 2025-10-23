#Operadores de identidad 
x=["manzana","pera"]
y=["manzana","pera"]
z=x
print("1. x es z")
print(x is z)
print("2. x es y")
#is apunta al objeto en memoria, no compara 
print(x is y)
print("3. x es igual y")
print(x==y)

#operadores de pertenencia
print("fresa se encunentra en x?")
print("fresa" in x)

print("manzana se encunentra en x?")
print("manzana" in x)


