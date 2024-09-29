import queue
import uuid
import time
import random

queue = queue.Queue()

def generate_requests(num_requests):
  """Генерує задану кількість заявок і додає їх до черги."""
  for _ in range(num_requests):
    request_id = uuid.uuid4()
    time.sleep(1)# Імітація часу обробки
    queue.put(request_id)
    time.sleep(1)
    print(f"Створена заявка: {request_id}")

def process_request():
  """Обробляє одну заявку з черги, якщо вона не пуста."""
  if not queue.empty():
    request_id = queue.get()
    print(f"Обробка заявки: {request_id}")
    time.sleep(2)  # Імітація часу обробки
  else:
    print("Черга пуста")

while True:
  # Генеруємо випадкову кількість заявок від 1 до 5
  num_requests = random.randint(1, 5)
  generate_requests(num_requests)

  # Обробляємо заявки, поки черга не стане пустою
  while not queue.empty():
    process_request()

  time.sleep(2)  # Пауза між генерацією заявок

  if input("Введіть 'q' для виходу: ") == 'q':
    break
