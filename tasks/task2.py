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

    def get_values(self, n : int):
        gen = self.generator()
        result = []
        for _ in range(n):
            sides = gen[_]
            result.append((sides, self.triangle(sides)))
        return result
task2 = Task2(2, 21)
res = task2.get_values(20)
cnt = 1
for r in res:
    print(f"{cnt} - ",r)
    cnt+=1

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

    def get_values(self, n : int):
        gen = self.generator()
        result = []
        for _ in range(n):
            sides = gen[_]
            result.append((sides, self.triangle(sides)))
        return result

    def parallel_execution(self, n: int):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_values, n)
            return future.result()
print("ВТОРОЙ КЛАСС")
task2_p = Task2_parall(2, 21)
res = task2_p.parallel_execution(20)
cnt = 1
for r in res:
    print(f"{cnt} - ", r)
    cnt += 1
