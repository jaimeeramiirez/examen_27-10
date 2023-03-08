#EJERCICIO 5
#Crea un script llamado descomposicion.py que realice las siguientes tareas:

#Debe tomar 1 argumento que será un número entero positivo. En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script. El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647

print("\n\n")

num = float(input("INGRESE UN NÚMERO DE 4 CIFRAS: "))

mil = (num - (num % 1000)) / 1000 * 1000
resto = num % 1000
centena = (resto - (resto % 100)) / 100
resto = num % 100
decena = (resto - (resto % 10)) / 10
unidad = resto % 10
print("\n")

print("UNIDADES:", '%04d' % unidad)
print("DECENAS:", '%03d' % decena)
print("CENTENAS:", '%02d' % centena)
print("MIL:", '%01d' % mil)

x = str(12).ljust(4, "0")
print(x)
