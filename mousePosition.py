from pynput import mouse
import dataFile

def on_click(x, y, button, pressed):
    dataFile.CordenadasMouse.cordenada_x = x
    dataFile.CordenadasMouse.cordenada_y = y
    print(x,y)
    if not pressed:
        # Stop listener
        return False
def clic_position():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    listener = mouse.Listener(on_click=on_click,)
    listener.start()
    return True
