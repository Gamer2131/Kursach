# client.py
import psutil
import requests
import time

SERVER_URL = 'http://localhost:5000/api/monitoring'

def send_data():
    data = {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent
    }
    response = requests.post(SERVER_URL, json=data)
    print(response.status_code)

while True:
    send_data()
    time.sleep(6)  # Отправляем данные каждую минуту
