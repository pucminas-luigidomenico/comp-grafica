from PyQt5.QtWidgets import QToolBar
from enum import IntEnum

from gui.dialog import TransformDialog

class ToolBar(QToolBar):
    TOOLS = IntEnum('tools', 'none line circ clear transform clip')
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.actions = {}
        self.pickedTool = ToolBar.TOOLS.none

        
    def addAction(self, action, key):
        """ Adiciona uma ação a barra de ferramentas e ao
        vetor que guarda todas as ações definidas.
        """
        
        super().addAction(action)
        self.actions[key] = action


    def chooseAction(self, key):
        """ Define a ação atual. """
        
        if key == ToolBar.TOOLS.clear:
            self.actions[self.pickedTool].setChecked(False)
        self.pickedTool = key
        

    def showTransformDialog(self):
        """ Cria uma nova caixa de diálogo referente as transformações 2d. """
        
        TransformDialog(self.parent).show()
        
    def clear(self):
        """ Limpa a área de desenhos janela associada a barra de ferramentas. """
        
        self.parent.lines.clear()
        self.parent.circs.clear()
        self.parent.update()
        