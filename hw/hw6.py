#Задание 1

def log_execution(func):
    def wrapper(*args):
        print(f"Функция {func.__name__} вызвана с аргументами {args}")
        
        result = func(*args)     
        print(f"Результат: {result}")
        print("Функция завершена")
        print()
        return result
    return wrapper
@log_execution
def add(a, b):
    return a + b

add(5, 3)
print("#Второе задание")
print()
#Задание 2

def require_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else:
            print("Доступ запрещён")
    return wrapper

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

@require_admin
def delete_database(user):
    print("База данных удалена")

# Проверка работы
admin_user = User("Alice", "admin")
regular_user = User("Bob", "user")

print("Тест с администратором:")
delete_database(admin_user) 

print("\nТест с обычным пользователем:")
delete_database(regular_user) 