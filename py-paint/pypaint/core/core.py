import sys

from PyQt5.QtWidgets import QApplication
from gui.window import Window 

def init():
    """ Inicializa a aplicação, criando a janela principal. """
    
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
