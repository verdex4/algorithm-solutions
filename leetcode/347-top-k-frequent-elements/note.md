## Задача

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

## Решение

Считаем [[freq|словарь частот]].
Нужно **сгруппировать элементы по значениям** (то есть частотам) и реализовать [[Bucket Sort]]. 
Зачем? Тогда мы за O(n) создадим упорядоченную структуру данных. Нам останется пройти k элементов с конца. Это тоже O(n), потому что кол-во корзин не более n.