time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделяем строку по запятой, чтобы получить отдельные временные значения
time_entries = time_string.split(',')

total_minutes = 0

for entry in time_entries:
    # Удаляем лишние пробелы и делим подстроку по пробелам, чтобы получить отдельные компоненты
    parts = entry.strip().split()
    for part in parts:
        if 'h' in part:
            total_minutes += int(part.replace('h', '')) * 60
        elif 'm' in part:
            total_minutes += int(part.replace('m', ''))
        elif 's' in part:
            total_minutes += int(part.replace('s', '')) // 60

print("Общее количество минут:", total_minutes)
