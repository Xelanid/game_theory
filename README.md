# Реализация алгоритмов для исследования операций
## Структура проекта
 - Simplex-method задачи линейного программирования
 - CMA-ES+Rastrigin
## Simplex-method
### Описание метода
Задача линейного программирования (далее - ЛП) - это задача нахождения наибольшего (наименьшего) значения линейной функции многих переменных при линейных ограничениях - равенствах или неравенствах - когда на переменные есть (или нет) ограничения на знак.
Канонической называется такая задача ЛП, для которой все ограничения являются равенствами, а на все переменные наложено ограничение на знак >=0.
Собственно, это и является первым условием для применения прямого симплекс-метода: чтобы его было возможно применить, задача ЛП должна быть представлена в канонической форме.
#### Краткий алгоритм прямого-симплекс метода:
1. Построение симплекс-таблицы по исходным данным
2. Итерация:
   - Проверка оптимальности, иначе - нахождение ведущего столбца симплекс-таблицы;
   - Проверка условия неограниченности решения задачи ЛП и нахождение ведущей строки симплекс-таблицы;
   - Преобразование симплекс-таблицы с помощью метода Гаусса.

### Правила ввода
- Ввод может осуществляться с помощью консоли или файла типа .txt
- 1. правила для переменной:
         записана с коэффициентом
         через "_" должен быть прописан ее номер
  2. используются только одиночные пробелы, между коэффициентом и переменной пробела нет
- Пример: ['1x_1 + 7x_2 + 2x_3 <= 9', '2x_2 + 4x_1 >= 5', 'x_3 + 2x_2 = 3']
- Пример оформления можно посмотреть в 'Simplex method/text.txt'

### Запуск программы
Осуществляется посредством запуска simplex.py.
Есть возможность ввода как с консоли, так и из файла типа .txt.

### Литература
1. Зенкевич Н. А., Губар Е. А. (2007) Практикум по исследованию операций. СПб. с. 7 - 25

## CMA-ES+Rastrygin
