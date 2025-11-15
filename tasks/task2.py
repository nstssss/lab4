import concurrent.futures

class Task2():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def generator(self):
        g = [(i, j, k) for i in range(self.start, self.end) for j in range(self.start, self.end) for k in range(self.start, self.end)]
        return g
    def triangle(self, sides):
        a, b, c = sides
        if (a < b + c and b < a + c and c < a + b):
            return True
        else: return False

# task2 = Task2(2, 21)
# gen = task2.generator()
# for sides in gen:
#     print(sides)
#     if task2.triangle(sides):
#         print("Образует")
#     else:
#         print("Не образует")
class Task2_parall():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def generator(self):
        g = [(i, j, k) for i in range(self.start, self.end) for j in range(self.start, self.end) for k in
             range(self.start, self.end)]
        return g

    def triangle(self, sides):
        a, b, c = sides
        if (a < b + c and b < a + c and c < a + b):
            return True
        else:
            return False

    def parallel_execution(self):
        gen = self.generator()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = {executor.submit(self.triangle, sides): sides for sides in gen}
            results = []
            for f in concurrent.futures.as_completed(future):
                sides = future[f]
                is_triangle = f.result()
                results.append((sides, is_triangle))

            return results

# task2_p = Task2_parall(2, 21)
# res = task2_p.parallel_execution()
# for r in res:
#     print(r)
