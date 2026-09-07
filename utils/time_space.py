import tracemalloc, time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Время: {end_time - start_time:.4f} сек.")
        return res
    return wrapper

def measure_space(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        res = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Текущая память: {current / 10**6:.2f} МБ")
        print(f"Пиковая память:  {peak / 10**6:.2f} МБ")
        return res
    return wrapper