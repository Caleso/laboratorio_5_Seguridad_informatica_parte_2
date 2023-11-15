#LABORATORIO_3
#NOMBRES: CATALINA LEDESMA

import socket
from Crypto.Cipher import DES3, AES
from Crypto.Random import get_random_bytes
# instalar pip install pycryptodome

def generate_aes_key():
    return get_random_bytes(16)

def encrypt_3des(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(data)

def decrypt_aes(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def save_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print('Esperando conexión...')
    client_socket, client_address = server_socket.accept()
    print('Conexión establecida desde:', client_address)

    # Generar clave AES y enviar al cliente
    aes_key = generate_aes_key()
    client_socket.sendall(aes_key)

    # Recibir mensaje cifrado por 3DES y desencriptar
    encrypted_message = client_socket.recv(1024)
    decrypted_message = decrypt_aes(aes_key, encrypted_message)


    save_to_file(decrypted_message, 'mensajerecibido.txt')
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
