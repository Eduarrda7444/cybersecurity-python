import sys 
import socket 
from datetime import datetime

# usuario coloca a host que quer scannear
if len(sys.argv) != 2:
    print("Use: python3 scanner.py (host)")
    sys.exit(1)

# confere o alvo
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("\nHostname não pode ser resolvido!")
    sys.exit(1)

# inicia o scan
print("-" * 50)
print("Alvo do scan: " + target)
print("Scan iniciado em: " + str(datetime.now()))
print("-" * 50)

# imprime todas as portas da porta determina que estão abertas
try:
    for port in range(1, 65536):            
        arg1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        arg1.settimeout(1)                     
        try:
            resultado = arg1.connect_ex((target, port))
            if resultado == 0:
                print(f"Porta {port} está aberta")
        finally:
            arg1.close()

# interferencia por teclado
except KeyboardInterrupt:
    print("\nSaindo do programa!")
    sys.exit()

# confere se o servidor está respondendo
except socket.error:
    print("\nServidor não está respondendo")
    sys.exit()

