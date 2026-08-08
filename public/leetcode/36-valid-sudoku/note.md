## Задача

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Объяснение

Мой подход
Использовал паттерн [[seen]]. Создал множества `seen` для каждой строки, столбца и квадрата 3x3. Хранил в списках. За один проход по доске пополнял эти множества и проверял, есть ли элемент в увиденных. Если да, то ответ `False`, если все проверили `True`.
Но это не очень по памяти, потому что это O(n^2). Хотя для доски 9x9 это пустяк.

Brute Forse neetcode
Идея: проверять каждую строку, столбец и квадрат. Тогда нам не нужно хранить все значения, достаточно текущих девяти. Это O(n) по памяти. Однако каждая клетка попадает под проверки 3 раза, поэтому хоть и сложность по времени остается O(n^2), но это в 3 раза медленнее.

Bit mask
Решение с паттерном [[Bit mask]]. Я его буду изучать сильно позже. Пока хватит идеи: вместо множества мы используем биты и сохраняем O(n) по памяти и используем 1 проход.

## Сложность

Мой подход
- Время: O(n^2)
- Память: O(n^2)

Brute Forse neetcode
- Время: O(n^2). На деле в 3 раза медленнее
- Память: O(n). Лучше, чем у меня

## Необходимые темы перед изучением

- [[seen]]