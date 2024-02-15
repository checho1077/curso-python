import random

user_winn = 0
computer_winn = 0
ronda = 0
print("Bienvenido al juego de piedra, papel o tijera")
options = ["piedra", "papel", "tijera"]
partida = input("¿Cuántas partidas quieres jugar?  ")
partida = int(partida)

Name = input("¿Cuál es tu nombre?.....")

while ronda < partida:
    print("*" * 10)
    print("Ronda", ronda + 1, "de", partida)
    print("*" * 10)

    user = input("Elija => piedra, papel o tijera ==>   ")

    user = user.lower()
    computer = random.choice(options)
    print("Compu eligió => ", computer)

    if user not in options:
        print("Esa opción no es válida")
        continue

    if user == "papel" and computer == "piedra":
        user_winn += 1
        print("!Ganaste¡", Name, ":", user_winn, "Compu:", computer_winn)
    elif user == "piedra" and computer == "tijera":
        user_winn += 1
        print("!Ganaste¡", Name, ":", user_winn, "Compu:", computer_winn)
    elif user == "tijera" and computer == "papel":
        user_winn += 1
        print("!Ganaste¡", Name, ":", user_winn, "Compu:", computer_winn)
    else:
        computer_winn += 1
        print("!Perdiste¡", "Compu:", computer_winn, Name, ":", user_winn)

    if user == computer:
        print("Empate", Name, ":", user_winn, "Compu:", computer_winn)

    ronda += 1

print("Puntaje final:", Name, ":", user_winn, "Compu:", computer_winn)
print("Los resultados son:", user_winn, "para", Name, "y", computer_winn, "para la Compu")

if user_winn > computer_winn:
    print("¡LE GANAS A CUALQUIER MAQUINA!")
else:
    print("¡COMPU... HASTA LA VISTA BABY!")

print("*" * 10)
