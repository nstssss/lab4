import concurrent.futures
STEP = 0.01

class Task1:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def generator(self):
        x = self.start
        while x <= self.end:
            yield 0.5 * x - 2
            x += STEP

    def get_values(self, n : int):
        g = self.generator()
        numbers = (next(g) for _ in range(n))
        return numbers

    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.get_values, n)
            return future.result()

task1 = Task1(1, 101)
res = task1.parallel_execution(50)
cnt = 1
for r in res:
    print(f"{cnt} - ",r)
    cnt+= 1

