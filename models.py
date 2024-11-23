# models.py

tasks = {}
next_id = 1

def get_next_id():
    global next_id
    next_id += 1
    return next_id - 1

def get_all_tasks():
    return tasks.values()

def get_task(task_id):
    return tasks.get(task_id)

def create_task(title, description):
    task_id = get_next_id()
    tasks[task_id] = {'id': task_id, 'title': title, 'description': description, 'completed': False}
    return tasks[task_id]

def update_task(task_id, title, description, completed):
    if task_id in tasks:
        tasks[task_id].update({'title': title, 'description': description, 'completed': completed})
        return tasks[task_id]
    return None

def delete_task(task_id):
    return tasks.pop(task_id, None)