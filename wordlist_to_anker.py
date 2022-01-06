import math

concrete_class_Rt = {"B3.5": 0.26, "B5": 0.37, "B7.5": 0.48, "B10": 0.56, "B12.5": 0.66, "B15": 0.75, "B20": 0.9, "B25": 1.05,
                     "B30": 1.15, "B35": 1.3, "B40": 1.4, "B45": 1.5, "B50": 1.6, "B55": 1.7, "B60": 1.8, "B70": 1.9,
                     "B80": 2.1, "B90": 2.15, "B100": 2.2} # в МПа
reinforcement_class = {"A240": 210, "A400": 340, "A500": 435} # в МПа
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

def tension_anchorage_length():
    concrete_class_input = input("Введите класс бетона (от B3.5 до B100)    ")
    reinforcement_class_input = input("Введите класс арматуры (только A240, А400, А500)    ")
    rebar_diameter = int(input("Введите диаметр арматуры (до 40Ø)    "))
    if rebar_diameter <= 32 and reinforcement_class_input == "A240":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A240"] * coefficient_two["ø <= 32"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A240"] * As)/(Rbond * μs)
        return L0an
    elif rebar_diameter <= 32 and reinforcement_class_input == "A400":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A400"] * coefficient_two["ø <= 32"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A400"] * As)/(Rbond * μs)
        return L0an
    elif rebar_diameter <= 32 and reinforcement_class_input == "A500":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A500"] * coefficient_two["ø <= 32"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A500"] * As)/(Rbond * μs)
        return L0an
    elif (36 <= rebar_diameter <= 40) and reinforcement_class_input == "A240":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A240"] * coefficient_two["36 and 40"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A240"] * As)/(Rbond * μs)
        return L0an
    elif (36 <= rebar_diameter <= 40) and reinforcement_class_input == "A400":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A400"] * coefficient_two["36 and 40"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A400"] * As)/(Rbond * μs)
        return L0an
    elif (36 <= rebar_diameter <= 40) and reinforcement_class_input == "A500":
        As = round(((math.pi * rebar_diameter**2)/4), 2)
        μs = round((math.pi * rebar_diameter), 2)
        Rbond = coefficient_one["A500"] * coefficient_two["36 and 40"] * concrete_class_Rt[concrete_class_input]
        L0an = (reinforcement_class["A500"] * As)/(Rbond * μs)
        return L0an
    else:
        L0an = 0
        return L0an