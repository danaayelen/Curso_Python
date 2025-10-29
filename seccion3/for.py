"""
Se usa para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena)
Se puede ejecutar un conjunto de sentencia, una vez para cada elemento en una list, tupla, conjunto.
"""
fruta=["manzana","pera","naranja","guayaba"]
for x in fruta:
    print(x)
print("-------------")
for x in "El agua clara": #imprime cada caracter
    print(x)
print("-------------")

#con BREAK se puede usar para detener el ciclo antes de que haya pasado por todos los elementos.
#Existe un ELSE especifica un bloque de codigo que se ejecutara al finalizar el codigo.
fruta2=["manzana","guayaba","naranja","platano"]

for x in fruta2:
  if x == "naranja":
    continue
  print(x)
print("---------------")

for x in fruta2:
   print(x)
else:
   print("son todas")
print("---------------")

fruta3=["manzana","guayaba","naranja","platano"]
for x in fruta3:
  if x == "guayaba":
    print(x)
    break
    
print("---------------")

