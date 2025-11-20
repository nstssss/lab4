import concurrent.futures
import time
import random

class Task3:
    def __init__(self, _list, n):
        self.list = _list
        self.n = n
    def write_max(self):
        numbers = set(list(map(int, self.list.split())))
        sorted_numbers = sorted(numbers, reverse=True)
        return sorted_numbers[:self.n]
# task3 = Task3()
# res = task3.write_max("4 6 2 7 9 1 1")
# print(res)
class Task3_parall:
    def __init__(self, _list, n):
        self.list = _list
        self.n = n
    def process_number(self, num_str):
        return int(num_str.strip())

    def parallel_execution(self):
        numbers_list = self.list.split()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            numbers = list(executor.map(self.process_number, numbers_list))

        unique_numbers = set(numbers)
        sorted_numbers = sorted(unique_numbers, reverse=True)
        return sorted_numbers[:self.n]

# task3_p = Task3_parall(" 54 2 256 7 43  13456 23245")
# res = task3_p.parallel_execution()
# print(res)
def main():
    data = " ".join(str(random.randint(-50000, 50000)) for _ in range(200000))
    n = 10

    start = time.perf_counter()
    Task3(data, n).write_max()
    exec_time_base = time.perf_counter() - start

    start = time.perf_counter()
    Task3_parall(data, n).parallel_execution()
    exec_time_parallel = time.perf_counter() - start

    print(f"Task3 (поиск {n} максимальных):")
    print(f"  Обычный:      {exec_time_base:.6f} сек")
    print(f"  Параллельный: {exec_time_parallel:.6f} сек")
    print(f"  Быстрее в {exec_time_base / exec_time_parallel:.6f} раз\n")

if __name__ == "__main__":
    main()