class fabonacci:

    def __init__(self,n):
        self.n = n
    def fib(self):
        """Write Fibonacci series up to n."""
        a, b = 0, 1
        while a < self.n:
            print(a, end=' ')
            a, b = b, a+b
        print()
    def fib2(self):
        """Return Fibonacci series up to n."""
        result = []
        a, b = 0, 1
        while a < self.n:
            result.append(a)
            a, b = b, a+b
        return result


if __name__ == "__main__":
    print("Hello world")