## Задача

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
[!] An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Решение

### Словарь частот

Нам нужны 2 словаря для вычисления частот букв для двух строк.
Одним проходом мы их заполняем (важный момент: если длины строк разные, то они не анаграммы).
В конце просто сравниваем 2 словаря (нюанс: всего букв 26, значит сравнение займет не более 26 операций -> O(1))
```python
for i in range(len(s)):
	counter_s[s[i]] += 1
	counter_t[t[i]] += 1
return counter_s == counter_t
```

### Хранение в списках

Можно вместо словаря хранить список (это про [[Direct Address Table]]), ведь индекс любой буквы мы можем вычислить через `ord(letter) - ord('a')`
Создаем список из 26 нулей
Прибавляем значение для букв первой строки
Вычитаем значение для букв второй строки
В конце убеждаемся, что все нули (O(1))

## Необходимые темы перед изучением

- [[Direct Address Table]]