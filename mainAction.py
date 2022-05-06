import pyautogui as pg
import time

def play (cordenadaDialogo, cordenadaEnvia, texto, xpmim):
    while True:
        pg.click(cordenadaDialogo)
        time.sleep(0.25)
        pg.write(texto)
        time.sleep(0.25)
        pg.click(cordenadaEnvia)
        time.sleep(60/int(xpmim))


