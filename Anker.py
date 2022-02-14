from command_again import compute_again
from dictionaries_and_functions_for_anker import tension_anchorage_length
import time
import sys

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
        As_cal = float(input("\nВведите площадь требуемую по расчету, см2/1м    "))
        As_ef = float(input("\nВведите площадь фактически установленную, см2/1м    "))
        if L0an != 0 and As_cal != 0 and As_ef != 0:
            Lan = float(α1) * L0an * (As_cal / As_ef)
            print("\nНеобходимая длина анкеровки равна = ", round(Lan, 2), "мм")
            if not compute_again():
                break
        elif L0an == 0 or As_cal == 0 or As_ef == 0:
            print("\nНеобходимая длина анкеровки равна = 0.0 мм")
            if not compute_again():
                break
    else:
        print("\nНеверно веден коэффинцент, введите корректное значение")
        continue
time.sleep(1)
print("\nЕсли у вас возникли проблемы, вопросы или предложения по работе программы - "
      "сообщите по электронной почте strokov.atomproject@gmail.com")
time.sleep(2)
off = input("\nДля выхода нажмите Enter ")
sys.exit(0)