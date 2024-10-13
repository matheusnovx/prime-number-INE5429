import random

def is_prime(n, quantidade_iteracoes):
    # Trata os números de 1 a 4 e verifica se são pares
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False

    # m = (n - 1) / 2^k
    m = n - 1
    # Divide por 2 até chegar em um número ímpar
    while m % 2 == 0:
        m //= 2

    # "a" é um número aleatório gerado e 1 < a < n-1
    a = random.randint(2, n - 1)

    # b = a^m mod n
    b = pow(a, m, n)

    # b ≡ 1 (mod n)
    if b % n == 1:
        return True

    # Realiza esse teste quantidade_iteracoes vezes
    for _ in range(quantidade_iteracoes):
        # b ≡ -1 (mod n)
        if b % n == n - 1:
            return True
        else:
            # b = b^2 mod n
            b = pow(b, 2, n)

    return False
