#Se escriben entre corchetes
#no se pueden cambiar sus valores
"""
Se puede recorrer los elementos de la tupla utilizando un bucle for
Para ver si un elementos especifico esta presente, se usa la palabra IN
No se pueden agregar elementos 
es posible usar el constructor tuple() para hacer una tupla

"""
miTupla = ("Manzana", "Pera", "Sandia")
print(miTupla)
print("---------")
print(miTupla[1])
print("----------")
for x in miTupla:
    print(x)
print("------------")
if "Sandia"  in miTupla:
    print("Sandia se encuentra en la tupla")
print("------------")
 
print(len(miTupla))
print("----")

# miTupla[3]="Platano"  #da error por que no se puede agregar
# print(miTupla)
