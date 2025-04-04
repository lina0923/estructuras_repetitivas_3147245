# Ejercicio 1
# Imprimir la tabla de multiplicar del
# numero que un usuario ingrese
# por teclado, utilizando un ciclo
# while

numero = int(input("Ingrese un numero:"))
i=10
while i >= 1: 
    print(numero, " x " , i, " = ", numero * i)
    #instrucccion de incremento
    i = i - 1