from command_again import compute_again
from wordlist_to_anker import tension_anchorage_length
import time
import sys

print("Программа для расчета необходимой длины анкеровки по СП 63.13330.2018 (с Изменением N 1) \nВерсия программы V2.0 \n© Строков Михаил")
time.sleep(2)
print("\nДля правильной работы программы необходимо использовать заглавные латинские буквы, "
      "иначе программа автоматически примет длину равной 0 мм!")
time.sleep(2)
while True:
    print("\nФормула анкеровки: Lan = α1 * L0an * (As,cal / As,ef)")
    α1 = float(input("Введите коэффициент α1"
                     "\nПримечания: для растянутых стержней принимают = 1.0; "
                     "\nдля сжатых стержней = 0.75; для напрягаемой арматуры = 1.    "))
    L0an = tension_anchorage_length()
    As_cal = float(input("Введите площадь требуемую по расчету, см2/1м    "))
    As_ef = float(input("Введите площадь фактически установленную, см2/1м    "))
    if α1 != 0 and L0an != 0 and As_cal != 0 and As_ef != 0:
        Lan = α1 * L0an * (As_cal / As_ef)
        print("Необходимая длина анкеровки равна = ", round(Lan, 2), "мм")
        if not compute_again():
            break
    elif α1 == 0 or L0an == 0 or As_cal == 0 or As_ef == 0:
        print("Необходимая длина анкеровки равна = 0.0 мм")
        if not compute_again():
            break
time.sleep(2)
print("\nЕсли у вас возникли проблемы, вопросы или предложения по работе программы - "
      "сообщите по электронной почте strokov.atomproject@gmail.com")
off = input("\nДля выхода нажмите Enter ")
sys.exit(0)
