import concurrent.futures

class Task2:
    def __init__(self, start: int, end: int, n: int):
        self.start = start
        self.end = end
        self.n = n

    def generator(self):
        g = [(i, j, k) for i in range(self.start, self.end) for j in range(self.start, self.end) for k in range(self.start, self.end)]
        return g
    def triangle(self, sides):
        a, b, c = sides
        if (a < b + c and b < a + c and c < a + b):
            return True
        else: return False

    def get_values(self):
        gen = self.generator()
        result = []
        for _ in range(self.n):
            sides = gen[_]
            result.append((sides, self.triangle(sides)))
        return result

class Task2_parall:
    def __init__(self, start: int, end: int, n: int):
        self.start = start
        self.end = end
        self.n = n

    def check_triangle(self, i):
        range_size = self.end - self.start

        a = self.start + (i // (range_size * range_size))
        b = self.start + ((i // range_size) % range_size)
        c = self.start + (i % range_size)

        if any(side >= self.end for side in (a, b, c)):
            return None

        sides = (a, b, c)
        is_triangle = all([a < b + c, b < a + c, c < a + b])
        return (sides, is_triangle)

    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self.check_triangle, range(self.n)))
        return results

