"""
It allows us to return elements from an iterable one at the time.
"""


def generator_function(num):
    for i in range(num):
        yield i


def performance(func):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result

    return wrapper


@performance
def long_time():
    print("long time: ", end="")
    for i in range(10000000):  # range is a generator
        i * 5


@performance
def long_time2():
    print("long time 2: ", end="")
    for i in list(range(10000000)):
        i * 5


def fib(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b


def main():
    for item in generator_function(1000):
        # print(item)  # We get one by one
        pass

    g = generator_function(100)
    print(next(g))
    print(next(g))
    print(next(g))

    long_time()
    long_time2()

    for n in fib(9):
        print(n)


if __name__ == '__main__':
    main()
