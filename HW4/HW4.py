#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Функция get_denominator(file_name): читает из файла, имя которого передано в качестве аргумента одно число. Файл должен существовать и содержать только одно число. В результате работы функция должна вернуть считанное из файла число.
Функция должна ловить три исключения (ексепшена):

    файла не существует
    файл содержит не число
    число в файле 0
"""
def get_denominator(file_name):
    try :
        f = open(file_name)
        d = f.read()        
        try:
            d = int(d)           
            if d == 0:
                print('Error: Dedominator is 0')    
            else:
                print('Success: Denominator is loaded')       
                return d
        
        except:
            print('Error: Input is not numeric')
        
    except FileNotFoundError:
        print('Error: File does not exist')
        
"""
2. Функция get_list_of_numbers(denominator): считает и возвращает список с целыми числами которые делятся на число, которое передается как аргумент функции (denominator)
"""

def get_list_of_numbers(d):
    list_of_numbers = []
    for i in range(1,101):
        if i%d == 0:
            
            list_of_numbers.append(i)        
        else:
            pass
    print('get_list_of_numbers calculated')
    return list_of_numbers

"""
3. Функция get_sum (list_of_numbers): считает и возвращает сумму всех чисел в переданном в качестве аргумента списке (list_of_numbers)
"""

def get_sum(list_of_numbers): 
    sum = 0
    for a in list_of_numbers:
        sum += a
    print('Sum calculated')
    return sum


"""
4. Функция write_result (number, name_of_result_file): 
    функция записывает переданное в качестве первого аргумента число (number) в файл, 
    имя которого передано во втором аргументе (name_of_result_file)
"""
def write_result(number, name_of_result_file):
    try:
        fp = open(name_of_result_file)
        fp.write(str(number))
        fp.close()
    except IOError:
        # If not exists, create the file
        fp = open(name_of_result_file, 'w+')
        fp.write(str(number))
        fp.close()
        
    print('Done, resulting file: '+ name_of_result_file)

"""
RESULT
"""

file_name = 'd.txt'
    
d = get_denominator('d.txt')
    
list_of_numbers = get_list_of_numbers(d)    
    
sum1 = get_sum(list_of_numbers)    
    
write_result(sum1,'output.txt')

