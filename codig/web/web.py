import pyautogui
import time
import random

# Mueve el cursor a la posición deseada y lo mantiene allí
x, y = 1780, 160
pyautogui.moveTo(x, y)
pyautogui.FAILSAFE = False  # Desactiva la función de seguridad
d=1
while True:
    # Hace clic en el botón tres veces con un intervalo de 5 a 20 minutos entre cada clic
    for i in range(3):
        pyautogui.click(button='left')
        a=random.randint(3, 5)
        b=random.randint(3, 5)
        while d==1:
            if (b>a and a!=b):
                d=0
            else:
                b=random.randint(3, 5)
        print(a, ",", b)
        time.sleep(random.uniform(a,b ))  # Espera entre 5 y 20 minutos antes de hacer el siguiente clic
