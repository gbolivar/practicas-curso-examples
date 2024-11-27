import hashlib

# Base de datos simulada con usuarios y contraseñas almacenadas como hashes
users_db = {
    "gbolivar": hashlib.sha256("#T13rr4D3Fu3g0..*".encode()).hexdigest(),
    "rmiranda": hashlib.sha256("#T13rr4D3Fu3g0..*".encode()).hexdigest(),
}

def authenticate(username, password):
    # Hash de la contraseña ingresada
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # Verificar si el usuario existe y la contraseña coincide
    if username in users_db and users_db[username] == password_hash:
        print("Autenticación exitosa.")
        return True
    else:
        print("Autenticación fallida.")
        return False

# Simulación
username = input("Usuario: ")
password = input("Contraseña: ", )
authenticate(username, password)
