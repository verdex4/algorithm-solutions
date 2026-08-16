---
status: Solved
platform: LeetCode
time_complexity: O(n)
space_complexity: O(n)
source_link: https://leetcode.com/problems/two-sum/description/
code_link: vscode://file/C:/Users/verdex/projects/algorithm-solutions/public/leetcode/1-two-sum/sol.py
created_at: 2026-08-16 19:38
---
## Условие

Дан `list[int]` и число `target`. Нужно найти индексы двух чисел, которые в сумме дают `target`.
Считать, что решение всегда одно и каждый элемент можно использовать 1 раз.

## "Ага!"

Типичный паттерн seen. Логика:
$n_{i}+n_{j}=t\iff n_{i}=t-n_{j}$
Тогда:
- t нам дано
- n_i мы можем хранить в словаре
- n_j - итерируемая переменная