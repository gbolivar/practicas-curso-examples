# Roles y permisos
permissions = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"],
}

# Base de datos simulada con usuarios y roles
users_roles = {
    "user1": "admin",
    "user2": "editor",
    "user3": "viewer",
}


def authorize(username, action):
    role = users_roles.get(username)
    if not role:
        print(f"Usuario '{username}' no encontrado.")
        return False

    if action in permissions.get(role, []):
        print(f"Autorización concedida: {username} puede realizar '{action}'.")
        return True
    else:
        print(f"Autorización denegada: {username} no tiene permiso para '{action}'.")
        return False


# Simulación
username = input("Usuario: ")
action = input("Acción deseada (read, write, delete): ")
authorize(username, action)
