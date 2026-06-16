import socket
from datetime import datetime

target = input("Objetivo (IP o dominio): ")

print("-" * 50)
print(f"Escaneando: {target}")
print(f"Hora inicio: {datetime.now()}")
print("-" * 50)

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[ABIERTO] Puerto {port}")

        sock.close()

except KeyboardInterrupt:
    print("\nEscaneo detenido por el usuario")

except socket.gaierror:
    print("Hostname no válido")

except socket.error:
    print("No se pudo conectar al servidor")