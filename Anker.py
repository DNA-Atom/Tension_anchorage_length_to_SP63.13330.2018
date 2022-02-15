from command_again import compute_again
from dictionaries_and_functions_for_anker import tension_anchorage_length
import time
import sys

# Функция As_check проверяет условие, после введения значение пользователем, 
# при котором если площадь сечения арматуры введена корректно, то выводится L0an = n или L0an = 0 (при площади арматуры равной 0)
# если нет, то тогда программа выдает сообщение пользователю о неккоректном вводе и перезапускает цикл для введения корректого значения. 

def As_check():
    while True:
        As_cal = input("\nВведите площадь требуемую по расчету, см2/1м    ")
        As_ef = input("\nВведите площадь фактически установленную, см2/1м    ")
        try:
            if L0an != 0 and As_cal != '0' and As_ef != '0':
                Lan = float(α1) * L0an * (float(As_cal) / float(As_ef))
                print("\nНеобходимая длина анкеровки равна = ", round(Lan, 2), "мм")
                break 
            elif As_cal == '0' or As_ef == '0':
                print("\nНеобходимая длина анкеровки равна = 0.0 мм")
                break
        except ValueError:
            time.sleep(1)
            print("Неккоректно ведено значение площадей арматуры, введите корректное значение")
            continue    

print("Программа для расчета необходимой длины анкеровки по СП 63.13330.2018 (с Изменением N 1) \nВерсия программы V2.2 \n© Строков Михаил")
time.sleep(2)
print("\nДля правильной работы программы необходимо использовать заглавные латинские буквы, \nа также корректные классы бетона и арматуры.")
time.sleep(2)
while True:
    print("\nФормула анкеровки: Lan = α1 * L0an * (As,cal / As,ef)")
    time.sleep(1)
    α1 = input("\nВведите коэффициент α1"
                     "\nПримечания: для растянутых стержней принимают = 1; "
                     "\nдля сжатых стержней = 0.75; для напрягаемой арматуры = 1.    ")
    if α1 == "0.75" or α1 == "1": 
        L0an = tension_anchorage_length()
        As = As_check()
        if not compute_again():
            break      
    else:
        time.sleep(1)
        print("Неверно веден коэффинцент, введите корректное значение")
        continue
time.sleep(1)
print("\nЕсли у вас возникли проблемы, вопросы или предложения по работе программы - "
      "сообщите по электронной почте strokov.atomproject@gmail.com")
time.sleep(2)
off = input("\nДля выхода нажмите Enter ")
sys.exit(0)