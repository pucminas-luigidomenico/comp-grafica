def line(p1, p2):
    """ Retorna a reta construída a partir de um ponto
    inicial e um ponto final.

    Tanto p1 quanto p2 devem ser um dicionário contendo
    as chaves x e y, referente as coordenadas.
    """
    
    x, y   = p1.values()
    dx     = p2['x'] - x
    dy     = p2['y'] - y

    steps  = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    line   = [p1]

    if steps == 0:
        return line
    
    xinc = dx / steps
    yinc = dy / steps

    for _ in range(steps):
        x += xinc
        y += yinc
        line.append({'x': round(x), 'y': round(y)})

    return line
