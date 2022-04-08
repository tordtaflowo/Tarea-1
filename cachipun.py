J1 = int(input("Jugador 1, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))

J2 = int(input("Jugador 2, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))

if J1 == J2 :
    print("Fue un empate")
elif J1 == 1:
    if J2 == 2:
        print("El jugador 2 gana")
    elif J2 == 3:
        print("El jugador 1 gana")
elif J1 == 2:
    if J2 == 1:
        print("El jugador 1 gana")
    elif J2 == 3:
        print("El jugador 2 gana")
elif J1 == 3:
    if J2 == 1:
        print("El jugador 2 gana")
    elif J2 == 2:
        print("El jugador 1 gana")
else:
    print("Eliga una opcion valida")
