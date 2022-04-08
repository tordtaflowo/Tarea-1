import random
usuario = random.randint(1,25)
print("El numero del usuario es: ",usuario)
computador = random.randint(1,25)
print("El numero del computador es: ",computador)
if usuario > computador:
    print("el usuario gana")
elif usuario < computador:
    print("el computador gana")
elif usuario == computador:
    print("empate")
