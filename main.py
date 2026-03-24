from calc import check_vm_creation
from visual import show_chart
import json, os
from datetime import datetime

# Журнал событий
logs = []
os.makedirs("logs", exist_ok=True)

print(" Защищённый контейнер запущен")

# Симулируем 10 запросов от разных пользователей
for i in range(10):
    user = f"user_{i % 3}"  # 3 разных пользователя
    result = check_vm_creation(user)
    
    log = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user,
        "status": result["status"],
        "reason": result["reason"]
    }
    logs.append(log)
    
    print(f"Запрос от {user} → {result['status']} ({result['reason']})")

show_chart(logs)

# Сохраняем журнал
with open("logs/events.json", "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print("\n Работа завершена! Проверь папку logs")