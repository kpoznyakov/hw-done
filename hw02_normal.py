# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
import random


print()

l = [2, -5, 8, 9, -25, 25, 4]
l_new = []

for i in l:
    if i > 0:
        if math.sqrt(i).is_integer():
            l_new.append(int(math.sqrt(i)))
print(l_new)

print('#########################################################')
print()

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date_str = '02.11.2013'
day = date_str[:2]
month = date_str[3:5]
year = date_str[-4:]
print(day, month, year)
dict_day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое'}
dict_month = {'10': 'октября', '11': 'ноября', '12': 'декабря'}
dt = []

if day in dict_day.keys():
    dt.append(dict_day[day])
if month in dict_month.keys():
    dt.append(dict_month[month])
dt.append(year)
dt_str = dt
print(dt_str)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print('#########################################################')
print()

ln = 0
list_r = []
while ln < 10:
    list_r.append(random.randint(-100, 100))
    ln += 1
print(list_r)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('#########################################################')
print()
lst = [1, 2, 4, 5, 6, 2, 5, 2]
print('a', list(set(lst)))  # потеряется порядок рано или поздно, да(

res = []
for i in lst:
    # print(i)
    # print('count = ', lst.count(i))
    if lst.count(i) == 1:
        res.append(i)
print('b', res)
