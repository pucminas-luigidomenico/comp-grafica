def line(p1, p2):
    """ Retorna a reta construída a partir de um ponto
    inicial e um ponto final.

    Tanto p1 quanto p2 devem ser um dicionário contendo
    as chaves x e y, referente as coordenadas.
    """

    line = [p1]
    
    x, y = p1.values()

    dx = p2['x'] - x
    dy = p2['y'] - y

    xinc = 1
    yinc = 1
    
    if dx < 0:
        dx = -dx
        xinc = -xinc

    if dy < 0:
        dy = -dy
        yinc = -yinc
        
    if dx > dy:
        p = 2 * dy - dx
        const1 = 2 * dy
        const2 = 2 * (dy - dx)

        for _ in range(dx):
            x += xinc

            if p < 0:
                p += const1
            else:
                p += const2
                y += yinc

            line.append({'x': x, 'y': y})
            
    else:
        p = 2 * dx - dy
        const1 = 2 * dx
        const2 = 2 * (dx - dy)
        
        for _ in range(dy):
            y += yinc

            if p < 0:
                p += const1
            else:
                p += const2
                x += xinc

            line.append({'x': x, 'y': y})

    return line


def circumference(center, radius):
    """ Retorna a circumferência construída a partir de
    um ponto central e o raio.

    center deve ser um dicionário contendo as chaves x e y,
    referente as coordenadas do ponto central.
    """
    
    x = 0
    y = radius
    p = 3 - 2 * radius
    
    circ = _symmetricPoints(center, x, y)

    while x < y:
        if p < 0:
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1

        circ += _symmetricPoints(center, x, y)

    return circ

def _symmetricPoints(center, x, y):
    """ Retorna os pontos simétricos, incluindo o ponto (x, y). """
    
    points = []
    points.append({'x': center['x'] + x, 'y': center['y'] + y})
    points.append({'x': center['x'] + x, 'y': center['y'] - y})
    points.append({'x': center['x'] - x, 'y': center['y'] + y})
    points.append({'x': center['x'] - x, 'y': center['y'] - y})
    points.append({'x': center['x'] + y, 'y': center['y'] + x})
    points.append({'x': center['x'] + y, 'y': center['y'] - x})
    points.append({'x': center['x'] - y, 'y': center['y'] + x})
    points.append({'x': center['x'] - y, 'y': center['y'] - x})
    return points
