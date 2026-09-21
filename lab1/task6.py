from datetime import datetime


now = datetime.now()


today_date = now.strftime("%d.%m.%Y")
current_time = now.strftime("%H:%M:%S")


day_of_week = now.weekday()

target_date = datetime(2026, 7, 1)

days_left = (target_date.date() - now.date()).days

print("Сегодняшняя дата:", today_date)
print("Текущее время:", current_time)
print("Номер дня недели (0 = Пн):", day_of_week)
print("Дней до 1 июля 2026 года:", days_left)