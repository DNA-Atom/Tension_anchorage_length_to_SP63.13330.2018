import math
import dictionaries_for_work_on_concrete_calculation

coefficient_one = {"A240": 1.5, "A400": 2.5, "A500": 2.5}
coefficient_two = {"ø <= 32": 1, "36 and 40": 0.9}

# Rbond = η1 * n2 * Rt
# η1 - для ненапрягаемой арматуры: 1,5 - для гладкой арматуры;
# 2,0 - для холоднодеформируемой арматуры периодического профиля;
# 2,5 - для горячекатаной и горячекатаной упрочненной арматуры периодического профиля;
# η2 - для ненапрягаемой арматуры:
# 1,0 - при диаметре арматуры мм;
# 0,9 - при диаметре арматуры 36 и 40 мм;

# Rs: A240 = 210 МПа; A400: = 340 МПа; A500 = 435 МПа
# В7,5 = 0,48; В10 = 0,56; В15 = 0,75; В20 = 0,9; В25 = 1,05; В30 = 1,15; В35 = 1,3; В40 = 1,4; В45 = 1,5; В50 = 1,6;
# В55 = 1,7; В60 = 1,8; В70	= 1,9; В80 = 2,1; В90 = 2,15; В100 = 2,2.

# Функция concrete_class_check проверяет, что значение класса бетона введенное пользователем истино (существует ли в словаре) 
# и возвращает значение для ключа, которое необходимо для расчета анкеровки, 
# в случае если значение ложное, просит повторить действие, до тех пор, пока значение не будет истинным

def concrete_class_check():
    while True:
        concrete_class_input = input("\nВведите класс бетона (от B3.5 до B100)    ")
        if concrete_class_input in dictionaries_for_work_on_concrete_calculation.concrete_class_Rt:
            return dictionaries_for_work_on_concrete_calculation.concrete_class_Rt.get(concrete_class_input)
        else:
            print('Неверно веден класс бетона, введите корректное значение')
            continue

# Функция reinforcement_class_check проверяет, что значение класса арматуры введенное пользователем истино (существует ли в словаре) 
# и возвращает значение для ключа, которое необходимо для расчета анкеровки, 
# в случае если значение ложное, просит повторить действие, до тех пор, пока значение не будет истинным. 

def reinforcement_class_check():
    while True:
        reinforcement_class_input = input("\nВведите класс арматуры (только A240, А400, А500)    ")
        if reinforcement_class_input in dictionaries_for_work_on_concrete_calculation.reinforcement_class:
            return dictionaries_for_work_on_concrete_calculation.reinforcement_class.get(reinforcement_class_input), reinforcement_class_input
        else:
            print('\nНеверно веден класс арматуры, введите корректное значение')
            continue

# Функция tension_anchorage_length делает расчет базовой длины анкеровки, небходимой для расчетной анкеровки, которая вложена в программу Anker.py 

def tension_anchorage_length():
    concrete = concrete_class_check()
    reinforcement, reinforcement_class_input = reinforcement_class_check()
    while True:
        rebar_diameter = input("\nВведите диаметр арматуры (до 40Ø)    ")
        if rebar_diameter in str(list(range(1, 41))):
            As = round(((math.pi * int(rebar_diameter) ** 2) / 4), 2)
            μs = round((math.pi * int(rebar_diameter)), 2)
            if int(rebar_diameter) <= 32:
                Rbond = coefficient_one[reinforcement_class_input] * coefficient_two["ø <= 32"] * concrete
                L0an = (reinforcement * As)/(Rbond * μs)
                return L0an
            elif 36 <= int(rebar_diameter) <= 40:
                Rbond = coefficient_one[reinforcement_class_input] * coefficient_two["36 and 40"] * concrete
                L0an = (reinforcement * As)/(Rbond * μs)
                return L0an
        else:
            print ('\nНеверно веден диаметр арматуры, введите корректное значение')
            continue