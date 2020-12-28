
def fib_1000_digits():
    a, b, c = 1, 0, 0
    i = 1
    while len(str(a)) < 1000:
        i += 1
        c = a
        a += b
        b = c
    return i

if __name__ == "__main__":
    print(fib_1000_digits())
