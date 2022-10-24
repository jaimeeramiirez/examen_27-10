#EJERCICIO 3
#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista3=[]

for letra in lista_1:
  if letra in lista_2 and letra not in lista3:
    lista3.append(letra)

print(lista3)