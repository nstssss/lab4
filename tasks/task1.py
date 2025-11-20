import concurrent.futures
import time
STEP = 0.01

class Task1:
    def __init__(self, start, end, n):
        self.start = start
        self.end = end
        self.n = n

    def generator(self):
        x = self.start
        while x <= self.end:
            yield 0.5 * x - 2
            x += STEP

    def get_values(self):
        g = self.generator()
        return [next(g) for _ in range(self.n)]

class Task1_parall:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def calculate_value(self, i):
        x = self.start + i * STEP
        if x > self.end:
            return None
        return 0.5 * x - 2

    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            values = list(executor.map(self.calculate_value, range(n)))
            return values


def main():
    start_value = 0
    end_value = 50000
    n = int((end_value - start_value) / STEP)

    print(f"Количество вычислений: {n}")

    start = time.perf_counter()
    Task1(start_value, end_value, n).get_values()
    exec_time_base = time.perf_counter() - start

    start = time.perf_counter()
    Task1_parall(start_value, end_value).parallel_execution(n)
    exec_time_parallel = time.perf_counter() - start

    print(f"Task1 (вычисление f(x) = 0.5x - 2):")
    print(f"  Обычный:      {exec_time_base:.6f} сек")
    print(f"  Параллельный: {exec_time_parallel:.6f} сек")
    print(f"  Быстрее в {exec_time_base / exec_time_parallel:.6f} раз\n")
if __name__ == "__main__":
    main()