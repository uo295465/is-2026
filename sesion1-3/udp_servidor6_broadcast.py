import socket, sys, random

#Por defecto, el puerto es 12345
puerto = 12345
print("Puerto por defecto:", puerto)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("" , puerto)) #Tambien podria ser "" -> socket.INADDR_ANY
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

while True:
	datagrama, origen = servidor.recvfrom(1024)
	msg_broadcast = datagrama.decode("utf-8")
	#probabilidad = random.randint(0,10)
	#if probabilidad  > 11: #Solo en caso de simular paquetes perdidos, volvemos
		#activar esta opcion cambiando el condicional
	#	print("Simulacion de paquete perdido")
	if msg_broadcast == "BUSCANDO HOLA":
		servidor.sendto(b"IMPLEMENTO HOLA", origen)
	elif msg_broadcast == "HOLA":
		mensaje_servidor = "HOLA: " + origen[0]
		print(mensaje_servidor)
		servidor.sendto(mensaje_servidor.encode("utf-8"), origen)

