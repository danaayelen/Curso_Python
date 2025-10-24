"""
If 
elif - para encadenar condiciones (else if)
else - atrapa lo que no este en las condiciones anteriores 
si solo se tiene una sola instruccion se puede poner en la linea de if
AND
OR
"""
x=10
y=50
z=100
if y>x:
    print("y es mayor que x")
elif x<y:
    print("y es menor que x")
else:
    print("x es igual a y")
print("----------------")
if x<y: print("x es menor que y")
print("----------------")
print("X") if x>y else print("Y")
print("----------------")
if x < y and z > x:
    print("Ambas condiciones son verdaderas")

print("----------------")
if x > y or z > x:
    print("Al menos una de las condiciones son verdaderas")