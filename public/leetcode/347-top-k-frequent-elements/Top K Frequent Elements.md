---
status: Review Needed
platform: LeetCode
time_complexity: O(2n)
space_complexity: O(2n)
source_link: https://leetcode.com/problems/top-k-frequent-elements/description/
code_link: vscode://file/C:/Users/verdex/projects/algorithm-solutions/public/leetcode/347-top-k-frequent-elements/sol.py
created_at: 2026-08-16 21:52
---
## Условие

Дан список целых чисел и число `k`. Нужно найти `k` самых часто встречающихся элементов в списке.
Если решений несколько, брать любое.

## "Ага!"

Используем [[Bucket Sort]], потому что:
- корзины - возможные частоты, а частота любого элемента не больше `n`, значит корзин не больше `n`
- несколько элементов могут быть с одной частотой: нужны корзины в виде списков

## Связанные темы

1. [[Bucket Sort]]