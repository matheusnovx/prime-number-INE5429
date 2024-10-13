import random

def is_prime(n, quantidade_iteracoes):
    # Trata os números de 1 a 4 e verifica se é par
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False

    # m = n - 1
    m = n - 1

    # Quanto maior a quantidadeIteracoes, maior a precisão.
    for _ in range(quantidade_iteracoes):
        # Gera um "a" aleatório.
        a = random.randint(2, n - 2)

        # Teorema de Fermat: a^(n-1) ≡ 1 (mod n)
        # Se essa congruência não for verdadeira, n é composto.
        if pow(a, m, n) != 1:
            return False

    # Depois de fazer o teste para quantidadeIteracoes "a"s diferentes, "n" é provavelmente primo.
    return True