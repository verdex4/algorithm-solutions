## Задача

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

**Example 1:**

**Input**
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
**Output**
[null, null, null, true, false, null, true, null, false]

**Explanation**
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

**Constraints:**

- `0 <= key <= 106`
- At most `104` calls will be made to `add`, `remove`, and `contains`.

## Объяснение

Сначала быстро реализовал решение Brute Force с O(n) сложностью для каждой операции: обычный список без добавления дубликатов.

Потом быстро вспомнил про [[Direct Address Table]]. Он хорошо подходил, т.к. диапазон значений фиксированный, разве что данные могут быть разреженные. Но так можно получить O(1) по времени. Каждая ячейка списка хранит булево значение, обозначающие наличие элемента с индексом, равным значению элемента.
В начале сделал плохую реализацию, т.к. я делал список, состоящий из None, и ещё инициализировал его как `[None for _ in range(n)]`, а как оказалось, это очень медленно. Для неизменяемых типов данных надо использовать копирование ссылок через `[val] * n`.

Есть решение, которое я уже подсмотрел, это с [[Linked List]]. Я понял идею, но пока отложил реализацию на потом. Идея такая: мы создаём k (`k < n`, `n % k = 0` для удобства) цепочек в списке. Их индекс будет остатком от деления числа на k. Если мы возьмем в этой задаче `k = 10000` (а `0 <= key <= 10^6`), то всего у нас будет 100 цепочек. Найти цепочку мы можем за O(1). А затем обращаемся к следующему элементу (`cur.next`) в цепочке и ищем там наличие элемента для реализации методов.
Этот алгоритм занимает меньше памяти, т.к. хранит только реально добавленные значения, но занимает больше времени на операции.
Время: O(n / k), где n - количество допустимых чисел, k - количество цепочек
Память: O(k + m), где m - количество элементов в множестве (они уникальны)

## Сложность

- Время: O(1)
- Память: O(10^6)

## Необходимые темы перед изучением

- [[Direct Address Table]]