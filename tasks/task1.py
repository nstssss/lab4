import concurrent.futures
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
        x = self.start + i * STEP
        if x > self.end:
            return None
        return 0.5 * x - 2

    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            values = list(executor.map(self.calculate_value, range(n)))
            return values


