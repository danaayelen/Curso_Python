"""
Un diccionario es una coleccion que no esta ordenada, que se puede
cambiar e indexar.
Se escriben entre corchetes y tienen claves y valores, puedes acceder a los elementos de un diccionario haciendo referencia a su nombre clave entre corchetes.
Hay un metodo llamado get() que le dara el mismo resultado.
se puede recorrer el diccionario mediante un ciclo for
Cuando se recorre un diccionario, el valor de retorno son las claves del diccionario, pero tambien hay metodos para devolver los valores.
"""
persona={
    "nombre":"pedro",
    "apellidos":"picapiedra",
    "empleo":"Conductor de gruas"
}
print(persona)
print("------------------------")
#acceder mediante el nombre 
print(persona["nombre"])
#usando get
print(persona.get("apellidos"))
print("------------------")
persona["empleo"]="chofer dinosaurios"
print(persona.get("empleo"))
print("----------------")
for x in persona:
    print(x) #imprime solo las llaves
    print(persona[x])
print("----------------")
for clave, valor in persona.items():
    print(clave, ":", valor)
