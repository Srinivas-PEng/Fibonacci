class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")

        self.n = n
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        # Handle negative case → empty iterator
        if self.n < 0:
            raise StopIteration

        # Stop condition: we return (n + 1) Fibonacci numbers
        if self.index > self.n:
            raise StopIteration

        if self.index == 0:
            self.index += 1
            return 0
        elif self.index == 1:
            self.index += 1
            return 1
        else:
            fib = self.a + self.b
            self.a, self.b = self.b, fib
            self.index += 1
            return fib