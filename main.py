from divisor_master import divisor_master as dv

# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
num1 = input('Enter int from 1 to 1000: ')
num1 = int(num1)
print('{} is simple? - {}'.format(num1, dv.is_simple(num1)))
num2 = input('Enter one more int from 1 to 1000: ')
num2 = int(num2)
print('{} is simple? - {}\n'.format(num2, dv.is_simple(num2)))

# 2) выводит список всех делителей числа
dv.print_dividers(num1)

# 3) выводит самый большой простой делитель числа
max_simple_div = dv.max_simple_divider(num1)
print('The maximum simple divider of {} is {}\n'.format(num1, max_simple_div))

# 4) функция выводит каноническое разложение числа
canonical_list_nums = dv.get_canonical_form(num1)
mltp = dv.multiple(canonical_list_nums)
print_str = ''
for i in range(0, len(canonical_list_nums)):
    if i != len(canonical_list_nums) -1:
        print_str = '{}{}{}'.format(print_str, canonical_list_nums[i], '*')
    else:
        print_str = '{}{}'.format(print_str, canonical_list_nums[i])
print('Canonical form of {} = {}\n'.format(num1, print_str))

# 5) функция выводит самый большой делитель (не обязательно простой) числа
max_div = dv.max_divider(num1)
print('The maximum devider of {} is {}'.format(num1, max_div))