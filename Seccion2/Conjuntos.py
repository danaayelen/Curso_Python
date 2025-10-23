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
