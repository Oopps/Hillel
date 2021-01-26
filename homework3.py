import random
import string
import math
from datetime import datetime



def generate_password(length: int) -> str:
    """
    generate password with given length
    Homework
    функция должна возвращать строку из случайных символов заданной длины.
    """
    password = ''
    for _ in range(length):
        password += random.choice(string.ascii_letters)
    return password


def encrypt_message(message: str) -> str:
    """
    encrypt message
    зашифровать сообщение по алгоритму.
    Сместить каждый символ по ASCII таблице на заданное рассояние.
    """
    key = 2
    new_message = ''
    for char in message:
        new_ord_char = ord(char) + key
        new_message += (chr(new_ord_char))
    return new_message


def lucky_number(ticket: str) -> bool:
    """
    lucky number (tram ticket)
    667766 - is lucky (6 + 6 + 7 == 7 + 6 + 6)
    сумма первых трех числе должна равняться сумме последних трех чисел
    """
    l_num = list(ticket)
    count_1st = 0  # sum of 1st half of the ticket
    count_2nd = 0  # sum of 2nd half of the ticket
    if len(l_num) % 2 != 0:
        return False
    for index in range(len(l_num)):
        if index < len(l_num) / 2:
            count_1st += int(l_num[index])
        else:
            count_2nd += int(l_num[index])
    if count_1st - count_2nd != 0:
        return False
    else:
        return True


def fizz_buzz(num: int) -> str:
    """
    fizz buzz
    усли число, кратно трем, программа должна выводить слово «Fizz»,
    а вместо чисел, кратных пяти — слово «Buzz».
    Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
    в остальных случаях число как строку
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


def password_is_strong(password: str) -> bool:
    """
    is password is strong
    (has number, char, lowercase, uppercase, at least length is 10)
    вернуть True если пароль надежный
    Праметры:
        1. Пароль должен содержать как минимум одну цифру
        2. Пароль должен содержать как минимум один сивол в нижнем регистре
        3. Пароль должен содержать как минимум один сивол в верхнем регистре
        4. Пароль должен быть как минимум 10 символов

    """
    if (len(password) >= 10 and
            any(char in string.ascii_lowercase for char in password) and
            any(char in string.ascii_uppercase for char in password) and
            any(char.isdigit() for char in password)):
        return True
    else:
        return False


def number_is_prime(num: int) -> bool:
    """
    number is prime
    на вход принимаем число
    вернуть True если число является простым
    https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE#:~:text=2%2C%203%2C%205%2C%207,%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%BC%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D1%82%D0%BE%D0%B9.
    """
    if num > 1:
        if num == 2:
            return True
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False


def decrypt_message(message: str) -> str:
    """
    decrypt message
    функция обратная encrypt_message
    Расшифровать сообщение по заданному ключу
    """
    key = 2
    new_message = ''
    for char in message:
        new_ord_char = ord(char) - key
        new_message += (chr(new_ord_char))
    return new_message


def volume_of_sphere(radius: float) -> float:
    """
    Volume of a Sphere
    на вход принимаем радиус сферы.
    Необходимо рассчитать объем сферы и округлить результат до двух знаков после точки
    round to 2 places
    """
    volume = round(4 / 3 * math.pi * radius ** 3, 2)
    return volume


def days_diff(start_date: ..., end_date: ...) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    end_date = datetime.strptime(end_date, '%d/%m/%Y')
    d_diff = end_date - start_date
    return d_diff.days


def prs(client_choice: str) -> bool:
    """
    paper rock scissors
    принимаем значение от клиента из списка значений (например ['p', 'r', 's'])
    сгенерировать случайный выбор на сервере
    реализовать игру в камень-ножницы-бумага между клиент-сервер
    """
    all_choices = ['p', 'r', 's']
    server_choice = random.choice(all_choices)
    player_win_cond = ['pr', 'rs', 'sp']
    round_result = client_choice + server_choice
    if client_choice == server_choice:
        return 'Draw'
    if round_result in player_win_cond:
        return 'Win'  # or True
    else:
        return 'Lose'  # or False




def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    вывести значение в виде римского числа
    """
    arab_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_num = ''

    i = 0
    while integer > 0:
        for _ in range(integer // arab_num[i]):
            roman_num += roman_syb[i]
            integer -= arab_num[i]
        i += 1
    return roman_num


if __name__ == '__main__':
    assert encrypt_message('Dima') == 'Fkoc'

# print(number_is_prime(2))

# print(encrypt_message('Anton'))
# print(decrypt_message('Cpvqp'))
# print(volume_of_sphere(10))
print(days_diff('10/10/2000', '04/10/2000'))
# print(prs('p'))
# print(integer_as_roman(25))
# print(password_is_strong('aasDF3'))
