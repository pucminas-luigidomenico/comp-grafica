def flood4(init, oldColor, newColor, getColor):
    """ Algoritmo de preechimento Flood-Fill, feito com uma
    abordagem iterativa (tomando como base o algoritmo recursivo,
    subtituiu-se a chamada recursiva por uma pilha contendo os pontos
    vizinhos.

    - init é o ponto inicial (dicionário contendo as chaves 'x' e 'y').
    - oldColor é a cor antiga.
    - newColor é a cor de preenchimento.
    - getColor é a função a ser utilizada para recuperar a cor atual do pixel.
    """
    
    stack = [init]
    points = []

    # Dicionário onde a chave é uma string composta por x e y,
    # que armazena a cor de um ponto já analisado.
    helper = {}

    while stack:
        p = stack.pop()
        x, y = p.values()
        key = '{},{}'.format(x, y)

        if key in helper:
            currentColor = helper[key]
        else:
            currentColor = getColor(x, y)
            helper[key] = currentColor

        if currentColor == oldColor:
            helper[key] = newColor
            points.append(p)

            stack.append({'x': x, 'y': y - 1})
            stack.append({'x': x, 'y': y + 1})
            stack.append({'x': x - 1, 'y': y})
            stack.append({'x': x + 1, 'y': y})

    return points
