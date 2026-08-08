## Задача

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Решение

Используем множество увиденных элементов `seen`
Оно позволяет за O(1) проверить наличие элемента, что позволяет 1 раз пройти по списку и не делать лишних операций