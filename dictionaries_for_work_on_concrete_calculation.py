# Расчетное сопротивление бетона для предельных состояний первой группы при классе бетона по прочности на сжатие, МПа
concrete_class_Rb = {"B3.5": 2.1, "B5": 2.8, "B7.5": 4.5, "B10": 6.0, "B12.5": 7.5, "B15": 8.5, "B20": 11.5, "B25": 14.5,
                     "B30": 17.0, "B35": 19.5, "B40": 22.0, "B45": 25.0, "B50": 27.5, "B55": 30.0, "B60": 33.0, "B70": 37.0,
                     "B80": 41.0, "B90": 44.0, "B100": 47.5}

# Расчетное сопротивление бетона растяжению для предельных состояний первой группы при классе бетона по прочности на осевое растяжение, МПа
concrete_class_Rbt = {"B3.5": 0.26, "B5": 0.37, "B7.5": 0.48, "B10": 0.56, "B12.5": 0.66, "B15": 0.75, "B20": 0.9, "B25": 1.05,
                     "B30": 1.15, "B35": 1.3, "B40": 1.4, "B45": 1.5, "B50": 1.6, "B55": 1.7, "B60": 1.8, "B70": 1.9,
                     "B80": 2.1, "B90": 2.15, "B100": 2.2}

# Расчетное сопротивление арматуры для предельных состояний первой группы на растяжение продольных стержней, МПа                     
reinforcement_class = {"A240": 210, "A400": 340, "A500": 435}

# Коэффициент, учитывающий влияние вида поверхности арматуры
coefficient_one = {"A240": 1.5, "A400": 2.5, "A500": 2.5}

# Коэффициент, учитывающий влияние размера диаметра арматуры
coefficient_two = {"ø <= 32": 1, "36 and 40": 0.9}