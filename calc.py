import os
import time
import psutil
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

# Получаем переменные с значениями по умолчанию
RATE_LIMIT = int(os.getenv("RATE_LIMIT_THRESHOLD", 3))  # по умолчанию 3
DISK_CRITICAL = int(os.getenv("DISK_CRITICAL_PERCENT", 90))  # по умолчанию 90

# Проверка, что переменные загрузились
print(f"RATE_LIMIT = {RATE_LIMIT}")
print(f"DISK_CRITICAL = {DISK_CRITICAL}")

# счётчик запросов 
user_requests = {}  # {user_id: [время_последнего_запроса, количество]}

def check_vm_creation(user_id: str):
    """Проверка, можно ли создать ВМ"""
    now = time.time()
    
    if user_id not in user_requests:
        user_requests[user_id] = [now, 1]
    else:
        last_time, count = user_requests[user_id]
        if now - last_time < 60:  # в пределах минуты
            count += 1
            if count > RATE_LIMIT:
                return {"status": "blocked", "reason": f"Слишком много запросов за минуту (лимит: {RATE_LIMIT})"}
        else:
            count = 1  # новая минута
        user_requests[user_id] = [now, count]
    
    # Проверка диска
    try:
        disk = psutil.disk_usage('/')
        if disk.percent > DISK_CRITICAL:
            return {"status": "blocked", "reason": f"Диск заполнен на {disk.percent}%"}
    except Exception as e:
        return {"status": "blocked", "reason": f"Ошибка проверки диска: {e}"}
    
    return {"status": "allowed", "reason": "OK"}

if __name__ == "__main__":
    result = check_vm_creation("user123")
    print(result)
    

