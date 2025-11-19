import concurrent.futures

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