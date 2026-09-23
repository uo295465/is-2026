import socket, sys
if len(sys.argv)<3:
	puerto=9999
	addr="127.0.0.1"
else:
	puerto= int(sys.argv[2],10)
	addr = sys.argv[1]
socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.connect((addr,puerto))
var=1
mensaje=str(var) +": " + input("")
mensaje1=input("-> ")

# CAMBIE HASTA QUE NO ENCUENTRE FIN DEBIDO A LA CADENA QUE ENVIA 
while not "FIN" in mensaje:
	datagrama = socket.sendto(mensaje.encode("utf-8"),(addr,puerto))
	var+=1
	mensaje=str(var) +": " + input("")
