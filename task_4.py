new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенос task_005 из new_tasks в completed_tasks
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# Удаление task_007 из new_tasks
new_tasks.remove('task_007')

# Вывод последней задачи из new_tasks
print("Следующая задача в приоритете:", new_tasks[-1])
