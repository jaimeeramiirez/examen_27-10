print("\n\n")
lista= [1,5, -2]

def agregar_una_vez(elemento):
  if elemento in lista:
    print(f"Error: Imposible añadir elementos duplicados --> {elemento}\n")
  else:
    lista.append(elemento)
agregar_una_vez(5)
print(lista)
    