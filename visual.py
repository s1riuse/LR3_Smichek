import matplotlib.pyplot as plt
import pandas as pd
import os

def show_chart(logs):
    """Простая визуализация результатов"""
    if not logs:
        print("Нет данных для отображения")
        return
    
    # Создаём папку для графиков
    os.makedirs('logs', exist_ok=True)
    
    # Преобразуем в DataFrame
    df = pd.DataFrame(logs)
    
    # Подсчитываем количество разрешённых и заблокированных
    allowed_count = len(df[df['status'] == 'allowed'])
    blocked_count = len(df[df['status'] == 'blocked'])
    
    # Создаём круговую диаграмму
    plt.figure(figsize=(8, 6))
    labels = ['Разрешено', 'Заблокировано']
    sizes = [allowed_count, blocked_count]
    colors = ['#2ecc71', '#e74c3c']
    explode = (0.05, 0.05)
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title(f'Статистика запросов на создание ВМ\nВсего запросов: {len(df)}', fontsize=14)
    
    # Сохраняем график
    plt.savefig('logs/stats_pie.png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Создаём столбчатую диаграмму
    plt.figure(figsize=(6, 5))
    bars = plt.bar(['Разрешено', 'Заблокировано'], [allowed_count, blocked_count], 
                   color=['#2ecc71', '#e74c3c'], alpha=0.7)
    
    # Добавляем значения на столбцы
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=12)
    
    plt.title('Количество запросов', fontsize=14)
    plt.ylabel('Число запросов')
    plt.grid(axis='y', alpha=0.3)
    
    # Сохраняем график
    plt.savefig('logs/stats_bar.png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Выводим статистику в консоль
    print("\n" + "="*40)
    print(" СТАТИСТИКА ЗАПРОСОВ")
    print("="*40)
    print(f" Всего запросов: {len(df)}")
    print(f" Разрешено: {allowed_count}")
    print(f"❌ Заблокировано: {blocked_count}")
    if blocked_count > 0:
        print(f"  Процент блокировок: {(blocked_count/len(df)*100):.1f}%")
    print("="*40)
    print("\n📁 Графики сохранены в папке logs/")
    print("   - stats_pie.png (круговая диаграмма)")
    print("   - stats_bar.png (столбчатая диаграмма)")



# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    test_logs = [
        {"timestamp": "2024-01-01 10:00:00", "status": "allowed", "reason": "OK"},
        {"timestamp": "2024-01-01 10:01:00", "status": "allowed", "reason": "OK"},
        {"timestamp": "2024-01-01 10:02:00", "status": "blocked", "reason": "Слишком много запросов"},
        {"timestamp": "2024-01-01 10:03:00", "status": "blocked", "reason": "Диск заполнен"},
        {"timestamp": "2024-01-01 10:04:00", "status": "allowed", "reason": "OK"},
        {"timestamp": "2024-01-01 10:05:00", "status": "blocked", "reason": "Rate limit"},
    ]
    
    show_chart(test_logs)
    show_timeline(test_logs)