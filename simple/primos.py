'''''
Entre com um limite de uma
sequência de número inteiros
positivos e retorne a quantidade de
números primos presentes na
sequência.
 Entre com o limite: 6
 Números primos: 2, 3, 5
'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

limit = int(input("Entre com o limite: "))
prime_numbers = count_primes(limit)
print("Números primos:", ', '.join(map(str, prime_numbers)))
print("Quantidade de números primos:", len(prime_numbers))
