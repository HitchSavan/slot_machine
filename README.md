# slot_machine

Теоретические и практические параметры различаются на ~6%. Первоначальные расчеты и подстройка набора символов на барабане проводятся в `calculations.py`.

Для уменьшения процента возврата было принято решение добавлять символы с низкооплачиваемыми комбинациями на левые барабаны (для уменьшения вероятности выпадения высокооплачиваемых комбинаций и выпадения длинных комбинаций) до достижения требуемого показателя МО процента возврата. При его достижении прочие показатели соответствуют требуемым.

## Расчеты

Расчеты проводятся в программах (и перенесены в Excel) с учетом того, что:

- Символ Wild не входит в набор из 8 и не имеет цену своего комбо. Для предотвращения сбора комбо из пяти Wild символов на первом барабане он отсутствует.
- Несмотря на расхождение с теоретически подобранной моделью, используется та, что даёт необходимые результаты в симуляторе.
- СКО считается как треть от разницы между фактическим средним и требуемым значением процента возврата (так как при пересчете на каждую игру разброс значений слишком велик).
- Параметры модели, вычисляемые практически путем множества испытаний, получены только с помощью симулятора из-за сложности проверки выигрыша (копия результатов в Excel, без расчетов).
- Предварительное формирование набора символов на барабане проводится с помощью Python-скрипта `calculations.py`, перенести расчет в Excel не смог из-за усложненности обеспечения требуемых параметров при подборе.

## Использование симулятора

В конструктор автомата передается название конфигурационного файла, формата:

```cpp
W // символ wild
1 2 3 W 2 3 5 2 4 5 1 4 6 1 3 2 4 1 3 2 1 3 7 6 // первый барабан
2 W 3 2 4 3 2 4 3 7 4 3 2 5 4 2 1 3 2 5 1 2 4 1 5 4 1 6 4 5 6 4 1 2 6 5 4 6 5 4 3 1 4 3 // второй барабан
5 2 1 5 2 4 6 2 5 3 4 2 3 W 5 3 1 5 2 4 3 2 5 3 2 1 6 7 5 6 4 5 3 2 5 6 4 5 2 3 // третий барабан
5 3 2 5 3 7 5 3 4 6 3 4 6 3 2 5 3 2 5 W 2 6 1 // четвертый барабан
4 2 5 6 7 W 3 1 // пятый барабан
win_table // разделитель для таблицы выигрышей
1 2 3 4 5 6 7 W // символы
3 3 5 7 9 12 15 20 30 // первое число - необходимое количество символов в линии, далее - соответствующие символам выигрыши
4 15 30 50 60 75 90 120 150 
5 45 75 150 250 350 500 750 1000 
lines // разделитель для участвующих линий
1 0 1 1 1 2 1 3 1 4 // линия в формате [[x1,y1],[x2,y2],..] - координаты на матрице видимых частей барабанов (в коде предусмотрена более наглядная визуализация)
0 0 0 1 0 2 0 3 0 4 
2 0 2 1 2 2 2 3 2 4 
0 0 1 1 2 2 1 3 0 4 
2 0 1 1 0 2 1 3 2 4 
trials // разделитель для количества спинов
1 // количество спинов
```
