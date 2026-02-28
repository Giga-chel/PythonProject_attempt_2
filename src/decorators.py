from functools import wraps


def log(filename=None):
    """Декоратор"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"Функция {func.__name__} выполнилась успешно. Результат: {result}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
            except Exception as e:
                message = f"Функция {func.__name__} упала с ошибкой {type(e).__name__}. Аргументы: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise
            return result

        return wrapper

    return decorator
