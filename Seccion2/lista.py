milista=["Manzana", "Pera", "Uvas", "naranja"]
print(milista[0])
print(milista[3])

milista[2]="Sandia" #cambia elemento 2 por sandia
print(milista)

for x in milista:
    print(x)

if "Uvas" in milista:
    print("SI existe Uvas en la lista")

print(len(milista)) #si se pone justo abajo de if uvas no nos dara nada
#es importante el orde de las lineas de codigo

milista.append("Platano") #egregar elemento
#for en python crea las variables automaticamente en este caso X
#para este caso x va sobreescribiendo los valores conforme recorre los elementos 
for x in milista:
    print(x)

milista.remove("Sandia") #remover elemento
for x in milista:
    print(x)

print("-----------")
miSegundaLista = milista.copy()
for x in miSegundaLista:
    print(x)


