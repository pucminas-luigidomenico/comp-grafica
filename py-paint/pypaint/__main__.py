import sys

from PyQt5.QtWidgets import QApplication
from gui.window import Window 

if __name__ == '__main__':
    """ Inicializa a aplicação, criando a janela principal. """
    
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
