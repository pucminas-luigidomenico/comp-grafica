from math import sqrt
from PyQt5.QtWidgets import (qApp, QDesktopWidget, QMainWindow, QActionGroup)
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt

from algorithm import (bresenham, dda, transform2d,
                       cohen_sutherland, liang_barsky,
                       flood_fill, boundary_fill,
                       bezier)
from data.lines import Lines
from data.circumferences import Circumferences
from gui.action import Action
from gui.icon import (lineIcon, circIcon, clearIcon, transformIcon,
                      clipIcon, fillIcon, bezierIcon)
from gui.toolbar import ToolBar
from gui.painter import Painter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toolButtons = {}
        self.lines = Lines(bresenham.line)
        self.circs = Circumferences(bresenham.circumference)
        self.fillPoints = []
        self.bezierControl = []
        self.printBezierControl = []
        self.bezierPoints = []
        self.bezierOk = False

        self.fillFn = flood_fill.flood4
        
        # Atalho definido para a ação de fechar o programa
        exitAct = Action(qApp.quit, self)
        exitAct.setShortcut('Ctrl+Q')
        self.addAction(exitAct)

        self.initUI()

        # Definição da área inicial de recorte
        self.clippingRect = Lines(bresenham.line)

        origin = {'x': self.toolbar.width(), 'y': self.menubar.height()}
        self.clippingRect.append(origin, {'x': self.width(), 'y': self.height()})

        
    def initUI(self):
        """ Inicializa todos os widgets relacionados a janela
        principal do programa.
        """
        
        self.resize(1024, 512)
        self.center()
        self.setWindowTitle('Py-Paint')

        self.createMenuBar()        
        self.createToolBar()
        self.show()


    def createMenuBar(self):
        """ Cria o menu superior, adicionando os devidos
        submenus e suas respectivas ações.
        """
        
        self.menubar = self.menuBar()

        menu = self.menubar.addMenu('Algoritmos')

        # Submenu referente aos algoritmos relacionados
        # a construção de retas.
        submenu = menu.addMenu('Retas')
        group  = QActionGroup(submenu)

        action = Action(lambda: self.lines.setFn(bresenham.line),
                           group, 'Bresenham', True)
        action.setChecked(True)
        submenu.addAction(action)

        action = Action(lambda: self.lines.setFn(dda.line) , group, 'DDA', True)
        submenu.addAction(action)

        # Submenu referente aos algoritmos relacionados
        # a janela de recorte 2D.
        submenu = menu.addMenu('Recorte')

        group = QActionGroup(submenu)

        action = Action(lambda: Painter.setClippingFn(cohen_sutherland.clipping),
                        group, 'Cohen-Sutherland', True)
        action.setChecked(True)
        submenu.addAction(action)
        
        action = Action(lambda: Painter.setClippingFn(liang_barsky.clipping),
                        group, 'Liang-Barsky', True)
        submenu.addAction(action)

        # Submenu referente aos algoritmos relacionados
        # a preenchimento de área.
        submenu = menu.addMenu('Preenchimento')

        group = QActionGroup(submenu)

        action = Action(lambda: self.setFillFn(flood_fill.flood4),
                        group, 'Flood-Fill', True)
        action.setChecked(True)        
        submenu.addAction(action)

        
        action = Action(lambda: self.setFillFn(boundary_fill.boundary4),
                        group, 'Boundary-Fill', True)
        submenu.addAction(action)

        
    def createToolBar(self):
        """ Cria o menu de ferramentas lateral, adicionando
        as devidas ferramentas.
        """
        
        self.toolbar = ToolBar(self)
        self.toolbar.setMovable(False)
        
        # Agrupamento de ações que apresentam como característica
        # o fato de permanecerem marcadas, para serem usadas de forma
        # contínua.
        group  = QActionGroup(self.toolbar)
        action = Action(lambda: self.toolbar.chooseAction(ToolBar.TOOLS.line),
                        group, "Linha", True, lineIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.line)

        action = Action(lambda: self.toolbar.showBezierDialog(),
                        group, "Bézier", True, bezierIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.bezier)
        
        action = Action(lambda: self.toolbar.chooseAction(ToolBar.TOOLS.circ),
                        group, "Circunferência", True, circIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.circ)

        action = Action(lambda: self.toolbar.chooseAction(ToolBar.TOOLS.fill),
                        group, "Preenchimento", True, fillIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.fill)
        
        action = Action(lambda: self.toolbar.chooseAction(ToolBar.TOOLS.clip),
                        group, "Recorte", True, clipIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.clip)

        # Demais ações, que apresentam comportamento ligado apenas
        # ao evento de clique.
        action = Action(lambda: self.toolbar.showTransformDialog(),
                        self.toolbar, "Transformações", False, transformIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.transform)

        action = Action(lambda: self.toolbar.clear(),
                        self.toolbar, "Limpar Tela", False, clearIcon())
        self.toolbar.addAction(action, ToolBar.TOOLS.clear)

        # Inclusão propriamente dita da barra de ferramentas
        # a janela principal.
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        
    def center(self):
        """ Centraliza a janela principal, em relação ao Desktop. """
        
        frame = self.frameGeometry()
        cpoint = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(cpoint)
        self.move(frame.topLeft())


    def getPixelColor(self, x, y):
        """ Recupera a cor setada para o pixel da posição (x, y). """
        
        return self.grab().toImage().pixelColor(x, y).rgb()
        

    def startBezier(self, n, ok):
        """ Inicializa a ferramente bezier com a quantidade de pontos
        de controle a ser utilizada. 
        """

        if ok:
            if self.bezierControl:
                self.bezierControl = []
            
            self.bezierN = n
        
    
    def transform(self, tdialog):
        """ Realiza as devidas transformações 2D, selecionadas
        pelo usuário.
        """
        
        translation = transform2d.identity()
        scale = transform2d.identity()
        rotate = transform2d.identity()
        reflexion = transform2d.identity()
        shear = transform2d.identity()
        
        if tdialog.checkBoxT.isChecked():
            a, b = [field.value() for field in tdialog.spinT.values()]
            translation = transform2d.translation(a, b)

        if tdialog.checkBoxS.isChecked():
            a, b = [field.value() for field in tdialog.spinS.values()]
            scale = transform2d.scale(a, b)

        if tdialog.checkBoxRT.isChecked():
            theta = tdialog.spinRT.value()
            rotate = transform2d.rotate(theta)

        if tdialog.checkBoxRF.isChecked():
            axis = tdialog.groupRF.checkedButton().text()
            reflexion = transform2d.reflexion(axis)

        if tdialog.checkBoxSH.isChecked():
            axis = tdialog.groupSH.checkedButton().text()
            value = tdialog.spinSH.value()
            shear = transform2d.shear(axis, value)
            
        M = transform2d.transformMatrix(translation, scale, rotate, reflexion, shear)
        for p1, p2 in self.lines.array:
            M = transform2d.toOrigin(M, p1)
            p1['x'], p1['y'] = transform2d.transformPoint(M, p1).values()
            p2['x'], p2['y'] = transform2d.transformPoint(M, p2).values()

        self.update()

            
    def mousePressEvent(self, event):
        """ Definição das ações a serem realizadas a partir do evento
        de clique do mouse:

        - Desenho de retas.
        - Desenho de circunferências.
        - Redefinição da janela de recorte.
        """

        # Ações realizadas a partir do clique referent ao
        # botão esquerdo do mouse.
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()

            if self.toolbar.pickedTool == ToolBar.TOOLS.bezier:
                if not self.bezierControl:
                    self.bezierOk = False
                    self.bezierControl = []

                self.bezierControl.append((x, y))
                self.printBezierControl = [p for p in self.bezierControl]
                
                if len(self.bezierControl) == self.bezierN:
                    self.bezierPoints = bezier.bezier(self.bezierControl)
                    self.bezierControl = []
                    self.bezierOk = True

                self.update()
                
            elif self.toolbar.pickedTool == ToolBar.TOOLS.line:
                p1 = {'x': x, 'y': y}
                self.lines.append(p1, p1)

            elif self.toolbar.pickedTool == ToolBar.TOOLS.circ:
                center = {'x': x, 'y': y}
                self.circs.append(center, 1)

            elif self.toolbar.pickedTool == ToolBar.TOOLS.clip:
                self.clippingRect.clear()

                p1 = {'x': x, 'y': y}
                self.clippingRect.append(p1, p1)

            elif self.toolbar.pickedTool == ToolBar.TOOLS.fill:
                newColor = QColor(Qt.green).rgb()

                if self.fillFn == boundary_fill.boundary4:
                    border = QColor(Qt.blue).rgb()
                    points = self.fillFn({'x': x, 'y': y}, border,
                                         newColor, self.getPixelColor)
                else:
                    oldColor = self.getPixelColor(x, y)
                    points = self.fillFn({'x': x, 'y': y}, oldColor,
                                         newColor, self.getPixelColor)
                    
                self.fillPoints += points

    def mouseMoveEvent(self, event):
        """ Definição das ações a serem realizadas a partir do evento
        de movimento do mouse:

        - Desenho de retas.
        - Desenho de circunferências.
        - Redefinição da janela de recorte.
        """
        
        if (self.toolbar.pickedTool == ToolBar.TOOLS.line
            and len(self.lines.array) > 0):

            pos = len(self.lines.array) - 1
            p2  = {'x': event.pos().x(), 'y': event.pos().y()}

            self.lines.update(pos, self.lines.array[pos][0], p2)
            
        elif (self.toolbar.pickedTool == ToolBar.TOOLS.circ
              and len(self.circs.array) > 0):

            pos    = len(self.circs.array) - 1
            center = self.circs.array[pos][0]
            p2     = {'x': event.pos().x(), 'y': event.pos().y()}
            
            radius = round(sqrt((center['x'] - p2['x']) ** 2 +
                                (center['y'] - p2['y']) ** 2))

            self.circs.update(pos, center, radius)

        elif self.toolbar.pickedTool == ToolBar.TOOLS.clip:
            p1 =  self.clippingRect.array[0][0]
            p2 = {'x': event.pos().x(), 'y': event.pos().y()}
                
            self.clippingRect.update(0, p1, p2)
            
        self.update()

        
    def mouseReleaseEvent(self, event):
        """ Definição das ações a serem realizadas a partir do evento
        de liberação do mouse:

        - Atualização final da área de desenhos.
        """
        
        self.update()

        
    def paintEvent(self, event):
        """ Definição das ações a serem realizadas a partir do evento
        de pintura da janela:

        - Desenho de retas.
        - Desenho de circunferências.
        - Redefinição da janela de recorte.
        """

        color = Qt.black
        pen = QPen(color)
        pen.setWidth(3)
        painter = Painter(self, self.lines, self.circs,
                          self.clippingRect, self.fillPoints)
        painter.setPen(pen)

        pen.setColor(color)
        painter.drawClippingArea()

        color = Qt.magenta
        pen.setWidth(9)
        pen.setColor(color)
        painter.setPen(pen)
        painter.drawBezierControl(self.printBezierControl)

        color = Qt.darkGreen
        pen.setColor(color)
        pen.setWidth(3)
        painter.setPen(pen)
        
        if self.bezierOk:
            painter.drawBezier(self.bezierPoints)

        color = Qt.blue
        pen.setColor(color)
        painter.setPen(pen)
                            
        painter.drawLines()
        painter.drawCircs()

        color = Qt.green
        pen.setColor(color)
        painter.setPen(pen)

        painter.fillShapes()


    def createPopupMenu(self):
        """ Impede que seja possível esconder a barra de ferramentas. """
        
        return None

        
    def setFillFn(self, fn):
        """ Seta o algoritmo a ser usado na operação de preenchimento. """
        
        self.fillFn = fn
        

