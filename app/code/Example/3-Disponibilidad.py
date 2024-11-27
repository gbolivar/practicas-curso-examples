import time

def check_system_availability():
    # Simulación de un recurso siempre disponible
    try:
        # Aquí podrías verificar un servicio real, como un servidor web
        print("Sistema disponible")
        return True
    except Exception as e:
        print("Sistema no disponible:", e)
        return False

# Simulación de chequeo periódico
for _ in range(3):
    is_available = check_system_availability()
    print("Disponibilidad:", is_available)
    time.sleep(2)  # Espera de 2 segundos