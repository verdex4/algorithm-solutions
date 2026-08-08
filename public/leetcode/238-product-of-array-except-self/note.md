## Задача

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Объяснение

Мой подход.
Операцию деления использовать нельзя, нужно умножение. Я построил наглядную таблицу, где на диагонали получились крестики, т.к. этот элемент мы не учитываем. Посмотрев на структуру, можно увидеть: под диагональю количество элементов увеличивается на один, если смотреть сверху вниз. А над диагональю, если смотреть снизу вверх, происходит то же самое.
Поэтому создаем список left и right.

По умному.
Используем [[Prefix and suffix|Prefix и Suffix product]]. 
`result[i] = prefix[i] * suffix[i]`
Можно оптимизировать по памяти. Нам не важно, что мы идем в разных направлениях. Мы можем не сразу вычислять значение элемента, а сначала умножить на prefix, и только потом умножить на suffix. 

## Сложность

- Время: O(n)
- Память: O(1)