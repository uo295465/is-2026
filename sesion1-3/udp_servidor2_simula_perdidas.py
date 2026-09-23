#ejercicio2 
import sys
import socket
import random
#leo la cantidad de argumentos 
if len(sys.argv) < 2:
	puerto = 9999
else:
	puerto= int(sys.argv[1], 10)#convierto argumernto en base 10
print("el puerto establecido es", puerto)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#creo socke udp
socket.bind(("",puerto))# lo asocio a todas las interfaces
while True:
	datagrama ,origen = socket.recvfrom(1024)
	probabilidad= random.randint(0,10)
	if(probabilidad<=5):
		print("paquete perdido")
		socket.sendto(datagrama, origen)
	else:	
		print("Origen: ", origen)
		print("Informacion: ", datagrama.decode("utf-8"))
		socket.sendto(datagrama, origen)
