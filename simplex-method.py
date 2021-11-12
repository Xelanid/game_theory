import numpy as np
from fractions import Fraction


def coeff_matrix(n_x_vars, equations, function):
    """
    :param n_x_vars: Число переменных в задаче ЛП

    :param equations: Список элементов типа string
    
    :param function: Тип list с двумя параметрами:
                            1. min или max
                            2. функция, с которой работаем
    """
    
    n_s_vars = 0
    total_vars = n_x_vars
    
    # добавление слабых переменных в ограничения
    for equation in equations:
        if '>=' in equation or '<=' in equation:
            n_s_vars += 1
            total_vars += 1
        
    coeff_matrix = [[Fraction("0/1") for i in range(total_vars+1)] for j in range(len(equations)+1)]        
    s_index = n_x_vars # индекс, начиная с которого будут располагаться значения s в матрице
    
    for i in range(1, len(equations)+1):
        equation = equations[i - 1].split(' ') # разбиваем ограничение по пробелам, чтобы уметь доставать любую переменную, коэффициент или операцию
        
        for j in range(len(equation)):
            if 'x_' in equation[j]:
                coeff, index = equation[j].split('x_') # т.к. переменные у нас вида ax_i, то разделяя по x_, вытаскиваем коэффициент и индекс переменной
                
                if equation[j - 1] == '-':
                    coeff_matrix[i][int(index) - 1] = Fraction("-" + coeff + "/1")
                else:
                    coeff_matrix[i][int(index) - 1] = Fraction(coeff + "/1")
            
            elif equation[j] == '<=':
                coeff_matrix[i][s_index] = Fraction("1/1")
                s_index += 1
                
            elif equation[j] == '>=':
                coeff_matrix[i][s_index] = Fraction("-1/1") 
                s_index += 1
                
    return coeff_matrix


def simplex(n_x_vars, equations, function):
    """
    :param vars: Число переменных в задаче ЛП

    :param equations: Список элементов типа string со всеми ограничениями:
                        1. правила для переменной:
                            записана с коэффициентом
                            через "_" должен быть прописан ее номер
                        2. используются только одиночные пробелы, между коэффициентом
                            и переменной пробела нет
                        Пример:
                            ['1x_1 + 7x_2 + 2x_3 <= 9', '2x_2 + 4x_1 >= 5', 'x_3 + 2x_2 = 3']

    :param function: Тип list с двумя параметрами:
                            1. min или max
                            2. функция, с которой работаем
    """
    coeff_matrix(n_x_vars, equations, function)


def input_file():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите название файла")
    file = input()
    
    f = open(file, "r", encoding='utf-8')
    equations = []
    k = 0
    for line in f:
        if k == 0:
            n_vars = line.replace('\n', '')
        elif k == 1:
            function = line.replace('\n', '')
        else:
            equations.append(line.replace('\n', ''))
        k += 1
        
    print(function, equations, n_vars)
    
    return function, equations, n_vars
    

def input_console():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите функцию и цель исследования - min/max - через запятую и пробел после нее")
    function = input().split(', ')
    print(function)
    
    print("Введите количество переменных:")
    n_vars = int(input())
    
    print("Введите количество ограничений:")
    n = int(input())
    
    print(f"На каждой строке через enter введите {n} ограничений:")
    equations = []
    for i in range(n):
        equations.append(input())
        
    return function, equations, n_vars


def input_file():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите название файла")
    file = input()
    
    f = open(file, "r", encoding='utf-8')
    equations = []
    k = 0
    for line in f:
        if k == 0:
            n_vars = line.replace('\n', '')
        elif k == 1:
            function = line.replace('\n', '')
        else:
            equations.append(line.replace('\n', ''))
        k += 1
        
    print(function, equations, n_vars)
    
    return function, equations, n_vars
    

def input_console():
    print("Для корректного ввода прочитайте правила оформления в файле README.md")
    print("Введите функцию и цель исследования - min/max - через запятую и пробел после нее")
    function = input().split(', ')
    print(function)
    
    print("Введите количество переменных:")
    n_vars = int(input())
    
    print("Введите количество ограничений:")
    n = int(input())
    
    print(f"На каждой строке через enter введите {n} ограничений:")
    equations = []
    for i in range(n):
        equations.append(input())
        
    return function, equations, n_vars


if __name__ == '__main__':
    print("Укажите как хотите вводить исходные данные: консоль/файл")
    type_input = input().lower()
    
    assert type_input in ['консоль', 'console', 'file', 'файл'], 'Такой тип не поддерживается'
    
    if type_input in ['консоль', 'console']:
        function, equations, n_vars = input_console()
    
    elif type_input in ['file', 'файл']:
        function, equations, n_vars = input_file()
    
    simplex(n_vars, equations, function)