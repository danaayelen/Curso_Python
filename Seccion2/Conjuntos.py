"""
No esta ordenada ni indexada, se escriben con llaves
Se usa len para el tamaño de elementos
S agrega varios elementos usando el metodo update()
Se agrega un elemento a un conjunto, usando el metodo add()
NO SE PUEDE CAMBIAR SUS ELEMENTOS PERO SI SE PUEDEN AGREGAR
"""
miset = {"manzana", "pera", "sandia"}
#cuando se ejecuta me puede cambiar el orden
print(miset)
print("---------------")

print(len(miset))
print("----------")
for x in miset:
    print(x)
print("------------")
print("Buscamos Sandia")
print("sandia" in miset)
print("Buscamos Platano")
print("Platano" in miset)
print("------------")

#agregar elementos
miset.update(["platano", "mango", "guayaba"])
for x in miset:
    print(x)
print("------------")
miset.add("cereza")
for x in miset:
    print(x)
print("------------")

miset.remove("platano")
miset.discard("cereza")
for x in miset:
    print(x)
print("------------")
x= miset.pop()
#lo que hace es que saca un elemento de miset y ese lo guarda en x
#el valor que saca es aleatorio de mi set
print(x)
print("------------")
for x in miset:
    print(x)
print("------------")

#clear limpiamos el set
miset.clear()
print(len(miset))
print("------------")
#del borramos del set
del miset
print("con del eliminamos el objeto set")
print("------------")