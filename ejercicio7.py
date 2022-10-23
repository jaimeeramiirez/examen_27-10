print("\n\n")

def agregar_una_vez():
  lista=["1", "2", "3", "4", "5", "Hola"]

  el="6"
  el1= "10"
  el2= "-2"
  el3= "Hola"

  lista.append(el)
  lista.append(el1)
  lista.append(el2)
  lista.append(el3)
  
  print("Esta es nuestra lista original:", lista)

  print("\n")

  if len(lista)==len(set(lista)):
      lista.append(el)
      lista.append(el1)
      lista.append(el2)
      lista.append(el3)
  else:
    print("Error: Imposible añadir elemmentos duplicados =>", el)
    print("Error: Imposible añadir elemmentos duplicados =>", el1)
    print("Error: Imposible añadir elemmentos duplicados =>", el2)
    print("Error: Imposible añadir elemmentos duplicados =>", el3)
    
    lista.remove(el)
    lista.remove(el1)
    lista.remove(el2)
    lista.remove(el3)




agregar_una_vez()