import socket, sys
if len(sys.argv)<3:
	puerto=9999
	addr="127.0.0.1"
else:
	puerto= int(sys.argv[2],10)
	addr = sys.argv[1]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((addr,puerto))

var = 1
mensaje = str(var) + ": " + input("")

while not "FIN" in mensaje:
	s.sendto(mensaje.encode("utf-8"),(addr,puerto))
	s.settimeout(1)
	try:
		respuesta_servidor, origen =s.recvfrom(1024)
		print(respuesta_servidor.decode("utf-8"))
		#print("Datagrama recibido")
	except  socket.timeout:
		print("ERROR")
	var += 1
	mensaje = str(var) + ": " +  input("")

