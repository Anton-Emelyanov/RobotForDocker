from datetime import datetime

# Получаем текущее время
current_time = datetime.now()

# Выводим текущее время в формате ЧЧ:ММ:СС
print("Текущее время:", current_time.strftime("%H:%M:%S"))
