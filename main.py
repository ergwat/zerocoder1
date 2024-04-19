class Task:
    def __init__(self, description, deadline, done = False):
        self.description = description
        self.deadline = deadline
        self.done = done

    def check_done(self):
        self.done = True

tasklist = []


print("Добро пожаловать в учебный планировщик задач.")

while True:
    print("Для добавления новой задачи напишите 'новая'")
    print("Для отображения списка текущих задач введите 'список'")
    print("Для отметки о выполнении задачи напишите 'закрыть'")

    user_input = input()
    match user_input.lower():
        case "новая":
            description = input("Введите описание задачи")
            deadline = input ("Введите крайний срок в формате ДД.ММ.ГГГГ")
            new_task = Task(description, deadline)
            tasklist.append(new_task)
            print(new_task)
            print(tasklist)

        case "список":
            for i in range(len(tasklist)):
                task = tasklist[i]
                print(f"{i + 1}: Задача: {task.description}, Срок: {task.deadline}, Выполнено: {task.done}")
        case "закрыть":
            for i in range(len(tasklist)):
                task = tasklist[i]
                print(f"{i + 1}: Задача: {task.description}, Срок: {task.deadline}, Выполнено: {task.done}")
            task_to_close = int(input("введите номер задачи, которую хотите закрыть")) - 1
            tasklist[task_to_close].done = True
        case __:
            print("Введите команду повторно\n")