def code(point, boundaries):
    """ Retorna o código calculado para o ponto,
    baseado nos limites da janela de recorte.

    - point deve ser um dicionário contendo as chaves
    x e y, referentes as coordenadas do ponto.
    
    - boundaries deve ser um dicionário contendo as chaves
    xmin, xmax, ymin, ymax, referentes aos limites da janela
    de recorte.
    """

    code = 0
    xmin, ymin, xmax, ymax = boundaries.values()
    x, y = point.values()

    if x < xmin:     # Ponto está antes da fronteira da esquerda.
        code += 1
    elif x > xmax:   # Ponto está após a fronteira da direita.
        code += 2

    if y < ymin:     # Ponto está abaixo da fronteira inferior.
        code += 4
    elif y > ymax:   # Ponto está acima da fronteira superior
        code += 8

    return code


def clipping(p1, p2, boundaries):
    """ Retorna uma tupla contendo o novo p1
    (ponto inicial da reta) e o novo p2 (ponto final da reta),
    ou uma tupla vazia caso a reta esteja fora da janela.

    - p1 deve ser um dicionário contendo as chaves
    x e y, referentes as coordenadas do ponto.

    - p2 deve ser um dicionário contendo as chaves
    x e y, referentes as coordenadas do ponto.
    
    - boundaries deve ser um dicionário contendo as chaves
    xmin, xmax, ymin, ymax, referentes aos limites da janela
    de recorte.
    """

    xmin, ymin, xmax, ymax = boundaries.values()

    accepted = False
    done = False

    while not done:
        x1, y1 = p1.values()
        x2, y2 = p2.values()
        
        code1 = code(p1, boundaries)
        code2 = code(p2, boundaries)

        if code1 == 0 and code2 == 0:    # Reta completamente dentro da janela
            accepted = True
            done = True
        elif code1 & code2 != 0:         # Reta completamente fora da janela
            done = True
        else:
            if code1 != 0:
                cout = code1
            else:
                cout = code2
                
            if cout & 1 == 1:        # Se bit 0 está setado
                xint = xmin
                yint = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            elif cout & 2 == 2:      # Se bit 1 está setado
                xint = xmax
                yint = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            elif cout & 4 == 4:      # Se bit 2 está setado
                yint = ymin
                xint = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            elif cout & 8 == 8:      # Se bit 3 está setado
                yint = ymax
                xint = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

            if cout == code1:       # Atualiza ponto inicial da reta
                p1 = {'x': xint, 'y': yint}
            else:                    # Atualiza ponto final da reta
                p2 = {'x': xint, 'y': yint}

    if accepted:
        x1, y1 = p1.values()
        x2, y2 = p2.values()
        
        return ({'x': round(x1), 'y': round(y1)}, {'x': round(x2), 'y': round(y2)})
    else:
        return ()
