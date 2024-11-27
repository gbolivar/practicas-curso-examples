from cryptography.fernet import Fernet

# Generar una clave y cifrar un mensaje
key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Este es un mensaje confidencial."
encrypted_message = cipher.encrypt(message)
decrypted_message = cipher.decrypt(encrypted_message)

print("Mensaje original:", message.decode())
print("Mensaje cifrado:", encrypted_message)
print("Mensaje descifrado:", decrypted_message.decode())