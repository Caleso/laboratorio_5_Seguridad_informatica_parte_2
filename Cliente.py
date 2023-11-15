#LABORATORIO_3
#NOMBRES: CATALINA LEDESMA

import socket
import hashlib
from Crypto.Cipher import AES

def generate_3des_key():
    return hashlib.sha256(b'My3DesKey12345678').digest()[:24]

def generate_aes_key():
    return hashlib.sha256(b'MyAesKey12345678').digest()[:16]

def pad_message(message):
    block_size = 16
    pad_size = block_size - (len(message) % block_size)
    return message + bytes([pad_size] * pad_size)

def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad_message(message))

def send_message(client_socket, message):
    client_socket.sendall(message)

# Conexion
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

des_key = client_socket.recv(24)
aes_key = client_socket.recv(16)

with open("mensajeentrada.txt", "rb") as file:
    message = file.read()

# Encriptar mensaje con AES
encrypted_message_aes = encrypt_aes(message, aes_key)

# Enviar mensaje encriptado al servidor
send_message(client_socket, encrypted_message_aes)

client_socket.close()
