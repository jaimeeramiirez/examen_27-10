#EJERCICIO 7


def agregar_una_vez(lista, el): #Función que añade un elemento a una lista si no está ya en ella.
    if el in lista: #Si el elemento está en la lista...
        raise ValueError(f"Error: Imposible añadir elmentos duplicados --> {el}") #...lanzamos una excepción.
    else: #Si el elemento no está en la lista...
        lista.append(el) #...lo añadimos a la lista.
    return lista #Devolvemos la lista.

if __name__ == "__main__": 
    lista = [1,5,-2] #Lista de números.
    el = -2 #Elemento a añadir a la lista.
    try: #Intentamos añadir el elemento a la lista.
        lista = agregar_una_vez(lista, el) #Llamamos a la función agregar_una_vez.
    except ValueError as error: #Si se produce una excepción...
        print(error) #...la imprimimos.
    else: #Si no se produce ninguna excepción...
        print(lista) #...imprimimos la lista.