#LABORATORIO_5
#NOMBRES: CATALINA LEDESMA Y DENISSE TORRES

import socket
import pyDes

MensajeEntrada = open('mensajeentrada.txt','r') #Se abre el txt
Textito = MensajeEntrada.readlines()[0] #Extrae el texto ingresado
MensajeEntrada.close()

#Encriptado DES
DES = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
Encriptado_DES = DES.encrypt(Textito)

#Asignacion de valores
Valor_P = 173
Valor_Q = 50
Valor_A = int(input("Ingrese valor A secreto: "))
Valor_Ax = str((Valor_Q**Valor_A)%Valor_P)

#Conexion
Host = "LocalHost"
Puerto = 8000
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
print("Servidor en espera")
Conexion, Addr = Server.accept()

for i in range(1):
    Conexion.send(Valor_Ax.encode(encoding="ascii", errors="ignore"))
    Bx = Conexion.recv(1024)
    Bx = int(Bx.decode(encoding = "ascii", errors = "ignore"))
    KeyA = (Bx**(Valor_A)) % Valor_P
    KeyB = Conexion.recv(1024)
    KeyB = int(KeyB.decode(encoding = "ascii", errors = "ignore"))
    Recibido = open('mensajerecibido.txt','w')
    
    #Si las llaves son iguales procede al desencriptado
    if KeyA == KeyB:
        Desencriptado_DES = DES.decrypt(Encriptado_DES)
        Envio = str(Desencriptado_DES)
        Conexion.send(Envio.encode(encoding = "ascii", errors = "ignore"))
        print ("Decrypted ", Desencriptado_DES)
        Recibido.write("Decrypted: %r" %Desencriptado_DES)

    #Si no son iguales procede al encriptado
    else:
        print ("Encrypted:", Encriptado_DES)
        Recibido.write("Encrypted: %r" %Encriptado_DES)
