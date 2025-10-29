"""
Con  el ciclo while podemos ejecutar un conjunto de sentencias siempre que una condición sea verdadera.
INCREMENTAR "I" sino se continuara en un ciclo infinito
*con la instruccion BREAK, podemos detener el ciclo incluso si la condicion while es verdadera
*con la instruccion CONTINUE podmeos detener la iteracion actual y continuar con la siguiente
"""
i = 1
while i<6:
    print(i)
    i+=1
    if i==4:
     continue
print("Despues del ciclo", i)