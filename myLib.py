import math


# 素数判定
def is_prime(n):
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True


# 素数列挙
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2 * i, n + 1, i):
                prime[j] = False
    return prime


'''
@notice: 素数列挙 (区間指定)
@param a: 区間の最初
@param b: 区間の最後
@return: [a, b]の素数のリスト
'''


def segment_sieve(a, b):
    sqrt_b = math.ceil(math.sqrt(b))
    prime_small = [True for i in range(sqrt_b)]
    prime = [True for i in range(b - a + 1)]

    for i in range(2, sqrt_b):
        if prime_small[i]:
            for j in range(2 * i, sqrt_b, i):
                prime_small[j] = False
            for j in range((a + i - 1) // i * i, b + 1, i):
                print('j: ', j)
                prime[j - a] = False
    return prime
