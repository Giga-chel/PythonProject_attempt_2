# Проект: Banking Utils: Утилиты для обработки банковских данных

## Содержание

* Установка
* Использование 
+ Модуль masks
+ Модуль widget
+ Модуль decorators
+ Модуль processing
* Тестирование

## Установка

1. Клонируйте репозиторий:
2. Создайте виртуальное окружение:
``
python -m venv venv
``
3. Установите зависимости
``
pip install pytest pytest-cov
``

## Использование

#### Модуль masks
``
get_mask_card_number(card_number)
``

Маскирует номер карты (16 цифр)

```
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
# Вывод: 7000 79** **** 6361
```

``
get_mask_account(acc_number)
``

Маскирует номер счета (20 цифр)

```
from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))
# Вывод: ** 4305
```
###### Важно: Функции выбрасывают ValueError, если длина входной строки не совпадает с ожидаемой (16 для карт, 20 для счетов)

#### Модуль widget
Функции для работы с пользовательским вводом

``
mask_account_card(mask_info)
``

Принимает строку вида "Тип Номер" и применяет маскировку

```
from src.widget import mask_account_card

# Для карт
print(mask_account_card("Visa Classic 1234567890123456"))
#Вывод: Visa Classic 1234 56** **** 3456

#Для счетов
print(mask_account_card("Счет 73654108430135874305"))
#Вывод: Счет ** 4305
```

`get_date(date_string)`
Преобразует строку с датой в формат ДД.ММ.ГГГГ

```
from src.widget import get_date

print(get_date("2009-06-14T07:12:53.213425"))
# Вывод: 14.06.2009
```

###### Важно: Функция ожидает строгий формат ISO с микросекундами: %Y-%m-%dT%H:%M:%S.%f


#### Модуль decorators

`
log(filename=None)
`

##### Логирование в консоль

Автоматически логирует начало и конец выполнения функции, а также результаты или возникшие ошибки.

```
from src.decorators import log

@log()def sum_numbers(a, b): 
    return a + b

sum_numbers(10, 20)

# Вывод в консоль: Функция sum_numbers выполнилась успешно. Результат: 30
```

##### Логирование в файл

```
@log(filename="my_log.txt")def divide(a, b): return a / b

try: 
    divide(10, 0)
except ZeroDivisionError: 
    pass
    
# Содержимое my_log.txt: Функция divide упала с ошибкой ZeroDivisionError. Аргументы: (10, 0)
```
###### Важно: Если происходит ошибка, декоратор записывает информацию в лог и пробрасывает исключение дальше (raise).

#### Модуль processing
Функции для работы со списками транзакций (словарей)

`
filter_by_state(operations, state)
`

Фильтрует список по ключу state

```
from src.processing import filter_by_state

data = [{"id":1, "state": "EXECUTED"}, {"id":2, "state": "CANCELED"}]
result = filter_by_state(data, state="EXECUTED")
# result: [{"id": 1, "state": "EXECUTED"}]
```

`
sort_by_date(data, reverse)
`

Сортирует список по ключу date

```
from src.processing inport sort_by_date

data = [{"id": 1, "date": "2015-01-15"}, {"id": 2, "date": "2024-02-10"}]
#
result = sort_by_date(data)
# result: [{"id":2, ...}, {"id": 1, ...}]
```

## Тестирование
Проект покрыт тестами с использованием библиотеки pytest. Тесты проверяют корректность работы функций, граничные случаи и обработку ошибок

#### Запуск тестов

```
pytest
```

#### Запуск с отчетом о покрытии 

```
pytest --cov=src tests/
```
Целевое покрытие: **Не менее 80%**

### Особенности тестов
* **Параметризация**: Используются декораторы @pytest.mark.parametrize для проверки функций на множестве входных данных без дублирования кода
* **Фикстуры**: Тестовые данные вынесены в фикстуры pytest
* **Проверка исключений**: Тесты проверяют, что функции выбрасывают ValueError при некорректных входных данных (например, неверная длина номера карты)