import requests
import os

# Встановлення змінної середовища EXAM
os.environ["EXAM"] = "2024"

# Друк значення змінної середовища EXAM
print(f"Змінна середовища EXAM: {os.environ['EXAM']}")

# Встановлення та друк інших змінних середовища
os.environ["ENV_NAME"] = "production"
os.environ["CPU"] = "4"
os.environ["COLORTERM"] = "truecolor"

print(os.environ["COLORTERM"])

payload = {'name': os.environ.get("ENV_NAME"), 'cpu': os.environ.get("CPU")}
r = requests.get('https://httpbin.org/get', params=payload)
print(f"Звертаємось до URL: {r.url} та отримуємо відповідь: {r.status_code} та {r.json()}")