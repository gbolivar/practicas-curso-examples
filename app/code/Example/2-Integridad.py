import hashlib

data = "Este es un mensaje importante."
# Crear un hash del mensaje
hash_original = hashlib.sha256(data.encode()).hexdigest()

# Simulamos una modificación del mensaje
data_modified = "Este es un mensaje modificado."
hash_modified = hashlib.sha256(data_modified.encode()).hexdigest()

print("Hash original:", hash_original)
print("Hash modificado:", hash_modified)
print("¿El mensaje es íntegro?", hash_original == hash_modified)