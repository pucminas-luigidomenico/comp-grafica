from functools import lru_cache, reduce

@lru_cache(maxsize=None)
def pascalTriangle(n):
    """ Retorna a enésima linha do triângulo de pascal.
    
    @param n int iniciando de 0

    @return lista de inteiros contendo os valores referentes a
    enésima linha do triângulod e pascal.
    """

    # Inicializa o triângulo de acordo com a quantidade de linhas.
    # Para 2 ou mais linhas, inicializa com: [1, 1].
    triangle = [1 for _ in range(1 + 1 * (n > 0))]
    i = 2
    while i <= n:
        triangle = [1] + [sum(pair) for pair in zip(triangle, triangle[1:])] + [1]
        i += 1

    return triangle


def bernstein(u, i, n):
    """ Retorna o termo (i, n) do polinômio de bernstein de grau n.

    @param u parâmetro tal que 0 <= u <= 1.
    @param i inteiro.
    @param n inteiro (grau do polinômio).

    @return termo (i, n) do polinômio de bernstein.
    """

    triangle = pascalTriangle(n)
    return triangle[i] * (u ** i) * ((1 - u) ** (n - i))


def bezier(control):
    """ Retorna os pontos referentes a curva de bezier, de acordo
    com a quantidade de pontos de controle utilizada e os pontos
    informados.

    @param n inteiro quantidade de pontos de controle.
    @param control lista de tuplas contendo os pontos de controle

    @return lista de pontos da curva de bezier.
    """
    
    # Parâmetro u em [0, 1].
    u = 0

    # Lista contendo os pontos.
    p = []

    # Parâmetro u varia de 0 até 1, com passo definido a seguir:
    step = 0.001

    # Quantidade de pontos na curva definida de acordo com o valor máximo
    # do parâmetro u (1) e o valor do passo.
    size = int(1 / step)

    # Grau da curva de bezier definida como numero de pontos de controle - 1
    n = len(control) - 1
    
    for j in range(size):
        x = y = 0
        i = 0
        for cx, cy in control:
            bern = bernstein(u, i, n)
            x += cx * bern
            y += cy * bern
            i += 1

        p.append((x, y))
        u += step

    return p
