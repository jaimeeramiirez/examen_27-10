#EJERCICIO 9
#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados
#ordenar la lista de mayor a menor
#eliminar todos los números impares
#	realizar una suma de todos los números que quedan	
#añadir como primer elemento de la lista la suma realizada
#devolver la lista modificada
#finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerdan con el primer número de la lista tal que así:

lista = [17, 24, 2, 13, 5, 4, 6, 1, 89, 0, 3, 7, 55, 25, 30, 8, 68, 156]

def modificar():
  def eliminar_impares(lista):
    nueva_lista = []
    for elemento in lista:
      if elemento % 2 == 0:
          nueva_lista.append(elemento)
    return nueva_lista
      
    
  sin_impares = eliminar_impares(lista)
  print("Sin impares: " + str(sin_impares))

modificar()




#EJERCICIO 9
#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados
#ordenar la lista de mayor a menor
#eliminar todos los números impares
#	realizar una suma de todos los números que quedan	
#añadir como primer elemento de la lista la suma realizada
#devolver la lista modificada
#finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerdan con el primer número de la lista tal que así:

lista = [17, 24, 2, 13, 5, 4, 6, 1, 89, 0, 3, 7, 55, 25, 30, 8, 68, 156]
print("Esta es la lista original: ", lista)
print("\n\n")
def modificar():
  def ordenar():
    lista1=sorted(lista, reverse=True)
    print("Esta es la lista ordenada de mayor a menor:", lista1)
  return ordenar()
  
  def eliminar_impares(lista):
    nueva_lista = []
    for elemento in lista:
      if elemento % 2 == 0:
        nueva_lista.append(elemento)      
    

  
  sin_impares = eliminar_impares(lista)
  print("Esta es la lista sin impares: " + str(sin_impares))

  return eliminar_impares(lista)



modificar()