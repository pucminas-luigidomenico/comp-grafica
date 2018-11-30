import sys

from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow 

if __name__ == '__main__':
    """ Inicializa a aplicação, criando a janela principal. """
    
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
