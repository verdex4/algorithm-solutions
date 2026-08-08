## Задача

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return _the array_ `ans`.

## Решение

### Ручные подходы

Можно
```python
ans = []
for i in range(2):
	for j in range(n):
		ans.append(nums[i])
```

А можно
```python
ans = [0] * (2 * n)
for i in range(n):
	ans[i] = ans[i + n] = nums[i]
```

Но эти 2 способа не очень хороши.
Первый - потому что мы делаем 2 прохода по nums
Второй - потому что мы тоже делаем 2 прохода: сначала выделяем память, потом заполняем значениями

### Быстрый и эффективный

`return nums + nums`
Это одна инструкция, которая выполнится быстро и сразу с выделением нужного количества памяти.