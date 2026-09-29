import socket, sys

if len(sys.argv)<2:
	addr="127.0.0.1"
else:
	addr = sys.argv[1]

#Por defecto el puerto sera 12345
puerto = 12345
#Ponemos el socket en modo broadcast
cliente=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#Variable para el timeout
tout=2

#Creamos el mensaje de broadcast y lo enviamos a todos los nodos de la red
msg_broadcast = "BUSCANDO HOLA"
checksum = cliente.sendto(msg_broadcast.encode("utf-8"),(addr, puerto))
#Comprobacion de que el datagrama es enviado con exito
if checksum > 0:
	print("---> Mensaje broadcast enviado con exito <---")
else:
	print("---> Mensaje broadcast: fallo en envio <---")

direccion_servidor= None

#Entramos en bucle infinito
while True:
	cliente.settimeout(tout)
	try:
		respuesta_servidor, origen = cliente.recvfrom(1024)
		#Recibe como tal respuesta del servidor
		#print(respuesta_servidor.decode("utf-8"))
		if respuesta_servidor.decode("utf-8") == "IMPLEMENTO HOLA":
			if direccion_servidor == None:
				direccion_servidor = origen
			print("Se ha recibido una respuesta desde", origen[0])
			#cliente.sendto(b"HOLA", origen)
		#En caso de que el servidor te responda con un hola
		#if respuesta_servidor[0:4].decode("utf-8") == "HOLA":
		#	print("Respuesta servidor: ", respuesta_servidor.decode("utf-8"))
		#	print("Servicio finalizado")
		#	sys.exit()

	except socket.timeout:
		print("Error -> No hay mas respuestas disponibles")
		break

#Respuesta de los servidores
if direccion_servidor == None:
	print("Ningun servidor ha respondido al mensaje")
	sys.exit()

cliente.sendto(b"HOLA", direccion_servidor)
respuesta_servidor, direccion_servidor=cliente.recvfrom(1024)
if respuesta_servidor[0:4].decode("utf-8") == "HOLA":
	print("Respuesta desde servidor servidor --> ", direccion_servidor[0])
	print("Mensaje del servidor recibida: ", respuesta_servidor.decode("utf-8"))
	print("Servicio finalizado")
	sys.exit()


