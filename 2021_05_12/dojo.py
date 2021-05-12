import time

def main():
    cells = 50000

    func1(cells)
    # Function func1 finished in 12.51378083
    func2(cells)
    # Function func2 finished in 0.20699382
    func3(cells)
    # Function func3 finished in 0.00020552
    func4(cells)
    #Function func4 finished in 0.00004649
    func5(cells)
    #Function func5 finished in 0.00002432

    return True

def time_decorator(func):
    def wrapper(arg):
        start = time.time()
        result = func(arg)
        finish = time.time()
        print(f"Function {func.__name__} finished in {finish - start:.8f}")
        return result
    return wrapper

@time_decorator
def func1(cells):
    su = 0
    for i in range(cells):
        su += 2**i
    return su//12//1000

    for i in range(cells):
        su += 1<<i
    return su//12//1000

# shift bits
# 1: 0001
# 2: 0010 <-
# 4: 0100
# 8: 1000 # 2^3
# 
#     def func2(cells):
#         su = 0
@time_decorator
def func2(cells):
    su = 0
    for i in range(cells):
        su += 1<<i
    return su//12//1000

@time_decorator
def func3(cells):
    su = 2 ** cells -1 
    return su//12//1000

@time_decorator
def func4(cells):
    su = (1 << cells) - 1 
    return su//12//1000

@time_decorator
def func5(cells):
    su = (1 << cells) - 1 
    return su//12000

if __name__ == "__main__":
    main()