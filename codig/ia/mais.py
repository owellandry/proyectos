import pyautogui
import time
import random

# Mueve el cursor a la posición deseada y lo mantiene allí
x, y = 1780, 160
pyautogui.moveTo(x, y)
pyautogui.FAILSAFE = False  # Desactiva la función de seguridad

while True:
    # Hace clic en el botón tres veces con un intervalo de 3 a 5 segundos entre cada clic
    for i in range(3):
        pyautogui.click(button='left')
        time.sleep(random.uniform(3, 5))  # Espera entre 3 y 5 segundos antes de hacer el siguiente clic
