from division_master import dv_master as dv

# тест функции проверки числа на простоту
def test_function_is_Number_Prime():
    #тест 1 - простое число от 1 до 1000
    n = 193 # True
    n_out = dv.is_Number_Prime(n)
    if n_out == True:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2 - простое число от 1 до 1000
    n = 997  # True
    n_out = dv.is_Number_Prime(n)
    if n_out == True:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    #тест 3 - отрицательное число
    n = -193  # 'Функция принимает на вход целые числа от 1 до 1000'
    n_out = dv.is_Number_Prime(n)
    if n_out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4 - float
    n = 1.8  # False
    n_out = dv.is_Number_Prime(n)
    if n_out == 'Функция принимает на вход целые числа':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 5 - больше 1000
    n = 1001  # False
    n_out = dv.is_Number_Prime(n)
    if n_out == 'Функция принимает на вход числа от 1 до 1000':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')
    # тест 6 - str с цифрой
    n = '881'  # True
    n_out = dv.is_Number_Prime(n)
    if n_out == True:
        print('Test 6 is OK')
    else:
        print('Test 6 is failed')
    # тест 7 - str с буквами
    n = 'abc'  # False
    n_out = dv.is_Number_Prime(n)
    if n_out == 'Функция принимает на вход целые числа от 1 до 1000':
        print('Test 7 is OK')
    else:
        print('Test 7 is failed')

def test_function_print_All_Divisors():
    # тест 1
    n = 10
    n_out = dv.print_All_Divisors(n) # [1,2,5,10]
    if n_out == [1,2,5,10]:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    n = 40
    n_out = dv.print_All_Divisors(n) #[1, 2, 4, 5, 8, 10, 20, 40]
    if n_out == [1, 2, 4, 5, 8, 10, 20, 40]:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    # тест 3
    n = -10
    n_out = dv.print_All_Divisors(n) #'Функция принимает на вход целые числа'
    if n_out == 'Функция принимает на вход целые числа':
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4
    n = 190.01
    n_out = dv.print_All_Divisors(n)  # 'Функция принимает на вход целые числа'
    if n_out == 'Функция принимает на вход целые числа':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 5
    n = 'abc'
    n_out = dv.print_All_Divisors(n)  # 'Функция принимает на вход целые числа'
    if n_out == 'Функция принимает на вход натуральные числа':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')
    # тест 6
    n = '273801'
    n_out = dv.print_All_Divisors(n)  # [1, 3, 11, 33, 8297, 24891, 91267, 273801]
    if n_out == [1, 3, 11, 33, 8297, 24891, 91267, 273801]:
        print('Test 6 is OK')
    else:
        print('Test 6 is failed')

def test_function_the_Biggest_Prime_Divisor():
    # тест 1
    n = 10
    n_out = dv.the_Biggest_Prime_Divisor(n)
    if n_out == 5:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    n = 777
    n_out = dv.the_Biggest_Prime_Divisor(n) #37
    if n_out == 37:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    #тест 3
    n = '08984' #4492
    n_out = dv.the_Biggest_Prime_Divisor(n)
    if n_out == 4492:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    #тест 4
    n = 'abc'
    n_out = dv.the_Biggest_Prime_Divisor(n)
    if n_out == 'Функция принимает на вход числа':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    #тест 5
    n = 0.763
    n_out = dv.the_Biggest_Prime_Divisor(n)
    if n_out == 'Функция принимает на вход целые числа':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')

def test_function_the_Biggest_Devisor():
    # тест 1
    n = 1000
    n_out = dv.the_Biggest_Devisor(n) #500
    if n_out == 500:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')
    # тест 2
    n = 273801
    n_out = dv.the_Biggest_Devisor(n)  # 91267
    if n_out == 91267:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')
    # тест 3
    n = '78393'  # 26131
    n_out = dv.the_Biggest_Devisor(n)
    if n_out == 26131:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4
    n = 'abc'
    n_out = dv.the_Biggest_Devisor(n)
    if n_out == 'Функция принимает на вход числа':
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 5
    n = 0.763
    n_out = dv.the_Biggest_Devisor(n)
    if n_out == 'Функция принимает на вход целые числа':
        print('Test 5 is OK')
    else:
        print('Test 5 is failed')

def test_function_prime_Multipliers_Canonical():
    # тест 1
    n = 273801
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == [(3, 1), (11, 1), (8297, 1)]:
        print('Test 1 is Ok')
    else:
        print('Test 1 is failed')
    # тест 2
    n = 1000
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == [(2, 3), (5, 3)]:
        print('Test 2 is Ok')
    else:
        print('Test 2 is failed')
    #тест 3 - отрицательное число
    n = -193  # False
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == False:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed')
    # тест 4 - float
    n = 1.8  # False
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == False:
        print('Test 4 is OK')
    else:
        print('Test 4 is failed')
    # тест 6 - str с цифрой
    n = '881'  # True
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == False:
        print('Test 6 is OK')
    else:
        print('Test 6 is failed')
    # тест 7 - str с буквами
    n = 'abc'  # False
    n_out = dv.prime_Multipliers_Canonical(n)
    if n_out == False:
        print('Test 7 is OK')
    else:
        print('Test 7 is failed')