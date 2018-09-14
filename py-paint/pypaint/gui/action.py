from PyQt5.QtWidgets import QAction

class Action(QAction):
    def __init__(self, fn, parent, text='', checkable=False, icon=None):
        super().__init__(text, parent)
        self.triggered.connect(fn)
        self.setCheckable(checkable)

        if icon != None:
            self.setIcon(icon)
