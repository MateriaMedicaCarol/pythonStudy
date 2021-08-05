import time


def display_time(func):
    def wrapper():
        t1 = time.time()
        result=func()
        t2 = time.time()
        print(('Total time :{} s').format(t2 - t1))
        return result
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


@display_time
def count_prime_nums():
    count = 0
    for i in range(2, 1000):
        if is_prime(i):
            count += 1
    print(count)
    return count


print(count_prime_nums())
