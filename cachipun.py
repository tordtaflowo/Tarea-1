J1 = int(input("Jugador 1, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))

if J1 > 3 :
    print("Eliga una opcion valida")
    
else :
    J2 = int(input("Jugador 2, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))

    if J2 > 3 :
        print("Eliga una opcion valida")


if J1 == 1:
    if J2 == 1:
        print("Es un empate")
    elif J2 == 2:
        print("El jugador 2 gana")
    elif J2 == 3:
        print("El jugador 1 gana")
elif J1 == 2:
    if J2 == 1:
        print("El jugador 1 gana")
    elif J2 == 2:
        print("Es un empate")
    elif J2 == 3:
        print("El jugador 2 gana")
elif J1 == 3:
    if J2 == 1:
        print("El jugador 2 gana")
    elif J2 == 2:
        print("El jugador 1 gana")
    elif J2 == 3:
         print("Es un empate")

