from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

from data.lines import Lines
from algorithm import bresenham
from algorithm import cohen_sutherland

class Painter(QPainter):
    clippingFn = cohen_sutherland.clipping
    fillFn = None
    
    def __init__(self, parent, lines, circs, clippingRect, fillPoints):
        """ Construtor da classe Painter.

        - lines deve ser uma instância da classe Lines.
        - circs deve ser uma instância da classe Circumferences.
        - clippingRect deve ser uma instância da classe Lines.
        """
        
        super().__init__(parent)

        self.lines = Lines(bresenham.line)
        self.circs = circs
        self.clippingRect = clippingRect
        self.fillPoints = fillPoints

        # Atualiza os pontos das retas de acordo com a área de recorte.
        p1, p2 = self.clippingRect.array[0]

        xmin, ymin = p1.values()
        xmax, ymax = p2.values()

        # Mantém o xmin como sempre sendo o referente a fronteira esquerda
        if xmin >= xmax:
            xmin, xmax = xmax, xmin

        # Mantém o ymin como sempre sendo o referente a fronteira inferior
        if ymin >= ymax:
            ymin, ymax = ymax, ymin

        boundaries = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}

        for line in lines.array:
            p1, p2 = line
            clippedLine = Painter.clippingFn(p1, p2, boundaries)

            if clippedLine:
                p1, p2 = clippedLine
                self.lines.append(p1, p2)


    def fillShapes(self):
        """ Preenche as regiões internas dos polígonos existentes
        na tela, a partir de um ponto inicial. """

        for p in self.fillPoints:
            colors = [Qt.White]
            newColor = Qt.Red
            shapePoints = self.fillFn(p['x'], p['y'], colors,
                                      newColor, parent.pixelColor)
        
    def drawClippingArea(self):
        """ Desenha o retângulo referente a área de recorte. """
        
        p1, p2 = self.clippingRect.array[0]

        x1, y1 = p1.values()
        x2, y2 = p2.values()
        
        # Reta superior do retângulo
        line = self.clippingRect.fn(p1, {'x': p2['x'], 'y': p1['y']})
        for i in range(0, len(line), self.pen().width() * 2):
                self.drawPoint(line[i]['x'], line[i]['y'])

        # Reta inferior do retângulo
        line = self.clippingRect.fn({'x': p1['x'], 'y': p2['y']}, p2)
        for i in range(0, len(line), self.pen().width() * 2):
                self.drawPoint(line[i]['x'], line[i]['y'])

        # Reta lateral esquerda do retângulo
        line = self.clippingRect.fn(p1, {'x': p1['x'], 'y': p2['y']})
        for i in range(0, len(line), self.pen().width() * 2):
                self.drawPoint(line[i]['x'], line[i]['y'])

        # Reta lateral direita do retângulo
        line = self.clippingRect.fn({'x': p2['x'], 'y': p1['y']}, p2)
        for i in range(0, len(line), self.pen().width() * 2):
                self.drawPoint(line[i]['x'], line[i]['y'])
                
    def drawLines(self):
        """ Desenha todas as retas passadas por parâmetro. """

        for p1, p2 in self.lines.array:
            for point in self.lines.fn(p1, p2):
                self.drawPoint(point['x'], point['y'])

                
    def drawCircs(self):
        """ Desenha todas as circunferências passadas por parâmetro. """

        for center, p in self.circs.array:
            for point in self.circs.fn(center, p):
                self.drawPoint(point['x'], point['y'])

                
    def setClippingFn(fn):
        """ Seta o algoritmo a ser usado na operação de recorte. """
        Painter.clippingFn = fn
        

    def setFillFn(fn):
        """ Seta o algoritmo a ser usado na operação de preenchimento. """
        Painter.fillFn = fn
        
