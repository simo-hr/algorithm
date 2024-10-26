from typing import List, Generator


# My answer
def find_primes(number: int) -> List[int]:
    result = []
    for n in range(2, number + 1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(n)
    return result


# Example answer1
def generate_primes_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes


# Example answer2
def generate_primes_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False

    return primes


def generate_primes_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False


if __name__ == "__main__":

    # (order_change_by_indexes("23"))
    # (order_change_by_indexes("568-379-8466"))
    # print(order_change_by_indexes("568-379-8466"))
    # print(find_primes(50))
    # print(generate_primes_v1(50))
    # print(generate_primes_v2(50))
    print([i for i in generate_primes_v3(50)])
