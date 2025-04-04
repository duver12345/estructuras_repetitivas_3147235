#Ejercicio 1
#Imprimir la tabla de multiplicar del
#numero que un usuario ingrese
#por teclado, utlizando un ciclo
#while

numero = int(input("Ingrese un numero: "))
i=1
while i <= 10:
    print(numero, "X" , i, "=",numero * i)
    ##Instrucion de incremento 
    i = i + 1