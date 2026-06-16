import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from colorama import Fore, init
init()

# Argumentos CLI
parser = argparse.ArgumentParser(description="Port Scanner Profesional")
parser.add_argument("-t", "--target", required=True, help="Objetivo (IP o dominio)")
parser.add_argument("-p", "--ports", default="1-1024", help="Rango de puertos (ej: 1-1000)")
parser.add_argument("-th", "--threads", type=int, default=50, help="Número de hilos")

args = parser.parse_args()

target = args.target
port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])
threads = args.threads

print("-" * 50)
print(f"Escaneando: {target}")
print(f"Puertos: {start_port}-{end_port}")
print(f"Hilos: {threads}")
print(f"Inicio: {datetime.now()}")
print("-" * 50)

open_ports = []

# Función de escaneo
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.GREEN + f"[+] Puerto abierto: {port}")
            open_ports.append(port)

        sock.close()

    except:
        pass

# Multithreading (clave pro)
with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\n" + "-" * 50)
print("Escaneo finalizado")
print(f"Puertos abiertos: {open_ports}")
print(f"Fin: {datetime.now()}")
print("-" * 50)

with open("resultados.txt", "w") as f:
    for port in open_ports:
        f.write(f"{port}\n")
