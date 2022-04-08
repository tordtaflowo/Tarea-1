base = int(input("Ingrese ancho de la base: "))

simbolo = "*"

if  base > 8 :
    print("El numero ingresado debe ser menor a 9")
else:
    contador = 0
    while contador < base:
        triangulo = simbolo*(contador+1)
        print(triangulo)
        contador += 1

