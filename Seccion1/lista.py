milista=["Manzana", "pera", "uvas", "naranja"]
print(milista[0])
print(milista[3])
milista[1]="sandia"
print(milista)
for x in milista:
    print(x)

if "uvas" in milista:
    print("si existe uvas en la lista")
    print(len(milista))
    
