def cliptest(p, q, u1, u2):
    """ Retorna uma tupla contendo o resultado
    da verificação (se a reta está completamente fora
    da janela ou não), e os valores de u1 e u2, modificados
    ou não.
    """

    ok = True

    if p < 0:
        r = q / p
        if r > u2:
            ok = False    # Fora da janela
        elif r > u1:
            u1 = r
    elif p > 0:
        r = q / p
        if r < u1:
            ok = False    # Fora da janela
        elif r < u2:
            u2 = r
    elif q < 0:
        ok = False        # Fora da janela

    return (u1, u2, ok)

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

    line = ()
    
    x1, y1 = p1.values()
    x2, y2 = p2.values()
    xmin, ymin, xmax, ymax = boundaries.values()

    u1, u2 = 0, 1
    dx = x2 - x1
    dy = y2 - y1
    
    u1, u2, ok = cliptest(-dx, x1 - xmin, u1, u2)       # Fronteira da esquerda
    if ok:
        u1, u2, ok = cliptest(dx, xmax - x1, u1, u2)    # Fronteira da direita
        
        if ok:
            u1, u2, ok = cliptest(-dy, y1 - ymin, u1, u2)    # Fronteira inferior

            if ok:
                u1, u2, ok = cliptest(dy, ymax - y1, u1, u2) # Fronteira superior

                if ok:
                    
                    # Se u2 < 1, deve-se atualizar o ponto final
                    if u2 < 1:
                        x2 = x1 + dx * u2
                        y2 = y1 + dy * u2

                    # Se u1 > 0, deve-se atualizar o ponto inicial
                    if u1 > 0:
                        x1 = x1 + dx * u1
                        y1 = y1 + dy * u1

                    p1 = {'x': round(x1), 'y': round(y1)}
                    p2 = {'x': round(x2), 'y': round(y2)}
                    line = (p1, p2)

    return line
