print("\n\n")
lista= [1,5, -2]

def agregar_una_vez(elemento):
  if elemento in lista:
    print(f"Error: Imposible añadir elementos duplicados --> {elemento}")
  else:
    lista.append(elemento)
agregar_una_vez(1)
print(lista)
    