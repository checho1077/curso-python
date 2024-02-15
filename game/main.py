import random

user_winn = 0
computer_winn= 0
ronda=0
print("bienvenido al juego de piedra, papel o tijera")
options = ["piedra",  "papel" , "tijera" ]
partida= input("¿estas Listo? partida de 3 o 5?  ")
partida= int(partida) 

Name= input("¿cual es tu nombre?.....")

while ronda<partida:
  print("*"*10)
  print("Ronda", ronda, "de", partida , )
  print("*"*10)
  ronda+=1


  user= input("elija=> piedra,papel o tijera==>   ")

  user = user.lower()
  computer = random.choice (options)
  print("Compu eligio=> ", computer)
  puntaje= 0
  

  
  if  user not in options:
   print("esa opcion no es valida")
  elif user == "papel" and computer == "piedra":
   user_winn+=1
   print("!ganaste¡",Name, user_winn,"Compu",computer_winn)
  elif user == "piedra"and computer =="tijera":
   user_winn+=1
   print("!ganaste¡",Name, user_winn+1,"Compu",computer_winn+0)
  elif user=="tijera" and computer=="papel":
   user_winn+=1
   print("!ganaste¡",Name, user_winn+1,"Compu",computer_winn+0)
  else:
   computer_winn+=1
   print(f"!perdiste¡","Compu", computer_winn+1,Name, user_winn+0)
  
  if user == computer:
   print("empate",Name ,user_winn, computer_winn)

print("puntaje",user_winn,computer_winn )
print("los resultados son",user_winn, computer_winn)
print ("!El ganador final es¡...." )
print("*"*10)

if user_winn > computer_winn:
 print("LE GANAS A CUALQUIER MAQUINA")
else: 
 print("COMPU...:HASTA LA VISTA BABY")
print("*"*10)
