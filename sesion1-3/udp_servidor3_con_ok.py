import socket, sys, random


if len(sys.argv) < 2:
	puerto = 9999
else:
	puerto = int(sys.argv[1], 10)

print("Puerto establecido: ", puerto)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("" , puerto)) #Tambien podria ser "" -> socket.INADDR_ANY
while True:
	datagrama, origen = socket.recvfrom(1024)
	probabilidad = random.randint(0,10)
	if probabilidad <= 5:
		print("Simulacion de paquete perdido")
	else:
		print("Origen: ", origen)
		print("Informacion cliente -> ", datagrama.decode("utf-8"))
		#socket.sendto(datagrama, origen)
		socket.sendto(b"OK", origen)
