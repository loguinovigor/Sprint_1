types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# Функция удаления дубликатов (приоритет — более высокий уровень)
def remove_duplicates(tickets_dict):
    seen = set()
    cleaned = {}

    for level in sorted(tickets_dict):  # сортировка от 1 к 5
        unique_tickets = []
        for ticket in tickets_dict[level]:
            if ticket not in seen:
                unique_tickets.append(ticket)
                seen.add(ticket)
        cleaned[level] = unique_tickets
    return cleaned

# Функция связывания названия критичности и тикетов
def assign_ticket_types(types_dict, tickets_dict):
    unique_tickets = remove_duplicates(tickets_dict)
    result = {}

    for level, tickets_list in unique_tickets.items():
        severity = types_dict[level]
        result[severity] = tickets_list

    return result


# Результат
tickets_by_type = assign_ticket_types(types, tickets)

# Печать результата (по желанию)
print(tickets_by_type)
