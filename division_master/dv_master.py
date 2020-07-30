# Модуль dv_master.py
# 1) проверка числа на простоту
def is_Number_Prime(n):
    if type(n) == str:
        if n.isdigit():
            n = int(n)
        else:
            return 'Функция принимает на вход целые числа от 1 до 1000'
    if type(n) == float:
        return 'Функция принимает на вход целые числа'
    if (n >= 1 and n <= 1000):
        pr_num = [] # создаем пустой список для простых чисел
        for i in range(2, n+1):
            if n%i == 0: # узнаем все делители, начиная с 2, заканчивая самим числом n
                pr_num.append(i)

        if len(pr_num) == 1: # если делитель только один, то это n. И, значит, число простое
            return True
        else:
            return False # если делителей несколько, значит, число не простое
    else:
        return 'Функция принимает на вход числа от 1 до 1000'

# 2) выводит список всех делителей числа

def print_All_Divisors(n):
    if type(n) == str:
        if n.isdigit():
            n = int(n)
        else:
            return 'Функция принимает на вход натуральные числа'
    if type(n) == float:
        return 'Функция принимает на вход целые числа'
    if n >= 1:
        list_divisor = [] # пустой список делителей
        for i in range(1, n+1):
            if n%i == 0: #если число делится на i без остатка, то это делитель
                list_divisor.append(i)
        return list_divisor
    else:
        return 'Функция принимает на вход целые числа'

# 3) выводит самый большой простой делитель числа.
def the_Biggest_Prime_Divisor(n):
    if type(n) == str:
        if n.isdigit():
            n = int(n)
        else:
            return 'Функция принимает на вход числа'
    if type(n) == float:
        return 'Функция принимает на вход целые числа'
    max_divisor = 1 # создаем переменную, обозначающую самый большой простой делитель
    for i in range(1, n): # не включая само число n, оперделяем:
        if is_Number_Prime(i): # простое ли число (используем уже написанную функцию)
            if n % i == 0: # делится ли число на i без остатка
                max_divisor = i # присваиваем переменной последний делитель
    return max_divisor


# 5)функция выводит самый большой делитель (не обязательно простой) числа.
def the_Biggest_Devisor(n):  # действуем, как в функции на опредедение самого большого простого делителя
    if type(n) == str:
        if n.isdigit():
            n = int(n)
        else:
            return 'Функция принимает на вход числа'
    if type(n) == float:
        return 'Функция принимает на вход целые числа'
    the_biggest_div = 1 # но не создаем условие, простое ли число
    for i in range(1, n):
        if n%i == 0:
            the_biggest_div = i
    return the_biggest_div

# 4) функция выводит каноническое разложение числа
def prime_Multipliers_Canonical(n):
    if type(n) == str:
        if n.isdigit():
            n = int(n)
        else:
            return 'Функция принимает на вход числа'
    if type(n) == float:
        return 'Функция принимает на вход целые числа'

    if n <= 1000 and is_Number_Prime(n): # если число на входе простое до 1000
        return 'Вы ввели простое число'
    if type(n) == int and n>0:
        prime_mult = [] # пустой список простых множителей
        for a in range(1,n): # от 1 до n (не включая n):
            if is_Number_Prime(a) and n%a == 0: # проверяем, простое ли число и делится ли без остатка
                prime_mult.append(a) # получаем список простых множителей
        pow = [] # создаем пустой список, обозначающий степень числа (то есть 5*5*5 представим как 5**3)
        for j in prime_mult: # делим число на каждый простой множитель из списка
            while n%j == 0: # до тех пор, пока делится без остатка
                pow.append(j)
                n = n/j # при этом число n изменяеся (с каждым циклом делится на множитель)

        mult_dict = {b: pow.count(b) for b in pow} # считаем, сколько у нас одинаковых чисел.
        # ключ - число, значение - кол-во упоминаний, то есть степень

        for keys, values in mult_dict.items(): # выводим через обозначение степени
            print(keys, '^', values)

        return list(mult_dict.items())
    else:
        return False