# Tension_anchorage_length_to_SP63.13330.2018
Программа для расчета необходимой длины анкеровки по СП 63.13330.2018 (с Изменением N 1) 
Версия программы V2.2

Программа расчитывает расчетную длину анкеровки согласно пункту 10.3.25 СП 63.13330.2018 (с Изменением N 1), которая учитывает базовую длину анкеровки, коэффициент, учитывающий влияние на длину анкеровки напряженного состояния бетона и арматуры и конструктивного решения элемента в зоне анкеровки, а также площади поперечного сечения арматуры, требуемая по расчету и фактически установленная соответственно.
При помощи данного расчета возможно уменьшить длину анкеровки необходимую для передачи усилия в арматуре с полным расчетным значением сопротивления Rs на бетон.
В данной программе расчет выполняется для классов бетона от B3.5 до B100, классов арматуры A240, A400, A500 и до 40∅ арматуры включительо, остальные классы бетона, арматуры и диаметр арматуры не учитываются и возможно будут добавлены при необходимости, т.к. в СП 63.13330.2018 остальные диамтеры не не нормируются и в современном строительстве редко встречаются.
Для правильной работы программы необходимо использовать заглавные латинские буквы, точки для разделения десятичных чисел, а также корректные классы бетона и арматуры, иначе программа будет выводить ошибку о неккореректном вводе, что в свою очередь защищает пользователя от возможности допустить ошибку в расчете. Все расчеты базовой длины анкеровки производятся автоматически до того момента, как пользователю необходимо ввести расчетную и фактическую площадь арматуры.

Вспомогательная информация:
Rbond = η1 * n2 * Rt
η1 - для ненапрягаемой арматуры: 1,5 - для гладкой арматуры;
2,0 - для холоднодеформируемой арматуры периодического профиля;
2,5 - для горячекатаной и горячекатаной упрочненной арматуры периодического профиля;
η2 - для ненапрягаемой арматуры:
1,0 - при диаметре арматуры мм;
0,9 - при диаметре арматуры 36 и 40 мм;

Rs: A240 = 210 МПа; A400: = 340 МПа; A500 = 435 МПа.

B3.5 = 0,26; B5 = 0,37; В7,5 = 0,48; В10 = 0,56; В15 = 0,75; В20 = 0,9; В25 = 1,05; В30 = 1,15; В35 = 1,3; В40 = 1,4; В45 = 1,5; В50 = 1,6;
В55 = 1,7; В60 = 1,8; В70	= 1,9; В80 = 2,1; В90 = 2,15; В100 = 2,2.

Если у вас возникли проблемы, вопросы или предложения по работе программы - сообщите по электронной почте strokov.atomproject@gmail.com

The program for calculation of necessary length of anchoring for the joint venture 63.13330.2018 (with Change N 1) 
Version of the V2.2 program

The program counts the rated length of anchoring according to Paragraph 10.3.25 of the joint venture 63.13330.2018 (with Change N 1) which considers the basic length of anchoring, the coefficient considering influence on length of anchoring of stress of concrete and fittings and the constructive solution of element in anchoring zone and also fittings cross-sectional area, demanded by calculation and actually established respectively.
By means of this calculation it is possible to reduce anchoring length necessary for transfer of effort in fittings with full calculated value of resistance of Rs by concrete.
In this program calculation is carried out for concrete classes from B3.5 to B100, classes of fittings A240, A400, A500 and up to 40 ∅ fittings vklyuchitelyo, other classes of concrete, fittings and diameter of fittings are not considered and will be perhaps added if necessary since in the joint venture 63.13330.2018 other diamter are normalized and in modern construction seldom meet.
For the correct work of the program it is necessary to use capital Latin letters, points for division of decimal numbers and also correct classes of concrete and fittings, otherwise the program will remove mistake about nekkorerektny input that in turn protects the user from opportunity to make mistake in calculation. All calculations of basic length of anchoring are made automatically until as the user needs to enter the rated and actual area of fittings.

Auxiliary information:
Rbond = η1 * n2 * Rt
η1 - for not strained fittings: 1.5 - for smooth fittings;
2.0 - for holodnodeformiruyemy fittings of periodic profile;
2.5 - for the hot-rolled and hot-rolled strengthened fittings of periodic profile;
η2 - for not strained fittings:
1.0 - with diameter of fittings of mm;
0.9 - with diameter of fittings of 36 and 40 mm;

Rs: A240 = 210 МПа; A400: = 340 МПа; A500 = 435 МПа.

B3.5 = 0,26; B5 = 0,37; В7,5 = 0,48; В10 = 0,56; В15 = 0,75; В20 = 0,9; В25 = 1,05; В30 = 1,15; В35 = 1,3; В40 = 1,4; В45 = 1,5; В50 = 1,6;
В55 = 1,7; В60 = 1,8; В70	= 1,9; В80 = 2,1; В90 = 2,15; В100 = 2,2.

If you had had problems, questions or sentences on work of the program - report by e-mail strokov.atomproject@gmail.com
