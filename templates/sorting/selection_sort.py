def selection_sort(arr: list[int]):
    """Base implementation"""
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    
    return arr

def selection_sort_stable_swaps(arr: list[dict]):
    """My own stable implementation with swaps (using O(n^2) swaps instead of 0 swaps in main version, but with correct math)"""
    n = len(arr)
    for i in range(n - 1):
        mini = i

        for j in range(i + 1, n):
            if arr[j]["val"] < arr[mini]["val"]:
                mini = j

        for j in range(i + 1, mini):
            if arr[j]["val"] == arr[i]["val"]:
                arr[i], arr[j] = arr[j], arr[i]

        arr[i], arr[mini] = arr[mini], arr[i]
    
    return arr

def selection_sort_stable_shift(arr: list[dict]):
    """Stable implementation based on shifting elements to the right"""
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j]["val"] < arr[mini]["val"]:
                mini = j

        if mini != i:
            arr[i : mini + 1] = arr[mini : mini + 1] + arr[i : mini]

    return arr

# --- TESTS FOR MY IMPLEMENTATION ---

def test_empty():
    data = []
    expected = []
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_one_element():
    data = [{"val": 5, "sub": "a"}]
    expected = [{"val": 5, "sub": "a"}]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_two_elements():
    data = [{"val": 5, "sub": "a"}, {"val": 3, "sub": "a"}]
    expected = [{"val": 3, "sub": "a"}, {"val": 5, "sub": "a"}]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_three_elements():
    data = [{"val": 2, "sub": "a"}, {"val": 2, "sub": "b"}, {"val": 1, "sub": "a"}]
    expected = [{"val": 1, "sub": "a"}, {"val": 2, "sub": "a"}, {"val": 2, "sub": "b"}]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_sorted():
    data = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 5, "sub": "a"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 5, "sub": "a"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_sorted_relative():
    data = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 2, "sub": "b"},
        {"val": 2, "sub": "c"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 4, "sub": "b"},
        {"val": 5, "sub": "a"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 2, "sub": "b"},
        {"val": 2, "sub": "c"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 4, "sub": "b"},
        {"val": 5, "sub": "a"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_reverse_sorted():
    data = [
        {"val": 5, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 3, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 1, "sub": "a"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 5, "sub": "a"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_reverse_sorted_relative():
    data = [
        {"val": 5, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 4, "sub": "b"},
        {"val": 3, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 2, "sub": "b"},
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 2, "sub": "a"},
        {"val": 2, "sub": "b"},
        {"val": 3, "sub": "a"},
        {"val": 4, "sub": "a"},
        {"val": 4, "sub": "b"},
        {"val": 5, "sub": "a"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_only_one_element():
    data = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 1, "sub": "d"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 1, "sub": "d"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_many_minimums():
    data = [
        {"val": 1, "sub": "a"},
        {"val": 2, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 3, "sub": "a"},
        {"val": 1, "sub": "c"},
        {"val": 2, "sub": "b"},
        {"val": 1, "sub": "d"},
        {"val": 1, "sub": "e"}
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 1, "sub": "d"},
        {"val": 1, "sub": "e"},
        {"val": 2, "sub": "a"},
        {"val": 2, "sub": "b"},
        {"val": 3, "sub": "a"}
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_negatives():
    data = [
        {"val": -2, "sub": "a"},
        {"val": 0, "sub": "a"},
        {"val": -1, "sub": "a"},
        {"val": -5, "sub": "a"},
        {"val": -2, "sub": "b"},
        {"val": 3, "sub": "a"},
        {"val": -1, "sub": "b"},
    ]
    expected = [
        {"val": -5, "sub": "a"},
        {"val": -2, "sub": "a"},
        {"val": -2, "sub": "b"},
        {"val": -1, "sub": "a"},
        {"val": -1, "sub": "b"},
        {"val": 0, "sub": "a"},
        {"val": 3, "sub": "a"},
        
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_minimums_with_one_another():
    data = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 3, "sub": "a"},
        {"val": 1, "sub": "d"},
        {"val": 1, "sub": "e"},
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 1, "sub": "b"},
        {"val": 1, "sub": "c"},
        {"val": 1, "sub": "d"},
        {"val": 1, "sub": "e"},
        {"val": 3, "sub": "a"},
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

def test_minimums_with_three_another():
    data = [
        {"val": 10, "sub": "a"},
        {"val": 1, "sub": "a"},
        {"val": 10, "sub": "b"},
        {"val": 5, "sub": "a"},
        {"val": 10, "sub": "c"},
        {"val": 7, "sub": "a"},
    ]
    expected = [
        {"val": 1, "sub": "a"},
        {"val": 5, "sub": "a"},
        {"val": 7, "sub": "a"},
        {"val": 10, "sub": "a"},
        {"val": 10, "sub": "b"},
        {"val": 10, "sub": "c"},
    ]
    actual = selection_sort_stable_swaps(data)
    actual2 = selection_sort_stable_shift(data)

    assert actual == expected
    assert actual2 == expected

test_empty()
test_one_element()
test_two_elements()
test_three_elements()
test_sorted()
test_sorted_relative()
test_reverse_sorted()
test_reverse_sorted_relative()
test_only_one_element()
test_many_minimums()
test_negatives()
test_minimums_with_one_another()
test_minimums_with_three_another()
print("TESTS PASSED")