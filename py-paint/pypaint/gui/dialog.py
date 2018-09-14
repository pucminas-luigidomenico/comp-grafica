from PyQt5.QtWidgets import (QButtonGroup,
                             QDialog,
                             QDialogButtonBox,
                             QCheckBox,
                             QGridLayout,
                             QHBoxLayout,
                             QLabel,
                             QLayout,
                             QPushButton,
                             QRadioButton,
                             QSpinBox,
                             QDoubleSpinBox,
                             QWidget)
from PyQt5.QtCore import Qt

class TransformDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.initUI()

    def initUI(self):
        """ Cria todos os componentes referentes as transformações. """

        translation = self.initTranslation()
        scale = self.initScale()
        rotation = self.initRotate()
        reflexion = self.initReflexion()
        shear = self.initShear()

        okButton = QPushButton('OK')
        okButton.setDefault(True)
        okButton.clicked \
                .connect(lambda: self.parent.transform(self))

        cancelButton = QPushButton('Cancelar')
        cancelButton.setShortcut('Ctrl+Q')
        cancelButton.clicked \
                    .connect(lambda: self.close())

        buttonBox = QDialogButtonBox(Qt.Horizontal)
        buttonBox.addButton(okButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(cancelButton, QDialogButtonBox.ActionRole)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(translation, 0, 0)
        mainLayout.addWidget(scale, 1, 0)
        mainLayout.addWidget(rotation, 2, 0)
        mainLayout.addWidget(reflexion, 3, 0)
        mainLayout.addWidget(shear, 4, 0)
        mainLayout.addWidget(buttonBox, 5, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle('Transformações 2D')
        

    def initTranslation(self):
        """ Cria todos os componentes referentes a translação e
        retorna o widget referente a translação.
        """

        label = QLabel('Translação')

        self.spinT = {'a': None, 'b': None}
        self.spinT['a'] = QSpinBox()
        self.spinT['a'].setRange(-10000, 10000)
        self.spinT['a'].setSingleStep(1)
        self.spinT['a'].setValue(0)
        self.spinT['a'].setEnabled(False)

        self.spinT['b'] = QSpinBox()
        self.spinT['b'].setRange(-10000, 10000)
        self.spinT['b'].setSingleStep(1)
        self.spinT['b'].setValue(0)
        self.spinT['b'].setEnabled(False)

        self.checkBoxT = QCheckBox()
        self.checkBoxT.setChecked(False)
        self.checkBoxT.stateChanged \
                       .connect(lambda state:
                                (self.spinT['a'].setEnabled(state),
                                 self.spinT['b'].setEnabled(state)))

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.spinT['a'])
        layout.addWidget(self.spinT['b'])
        layout.addWidget(self.checkBoxT)

        translation = QWidget()
        translation.setLayout(layout)

        return translation
        

    def initScale(self):
        """ Cria todos os componentes referentes a escala e
        retorna o widget referente a escala.
        """

        label = QLabel('Escala')

        self.spinS = {'a': None, 'b': None}
        self.spinS['a'] = QDoubleSpinBox()
        self.spinS['a'].setRange(-10000, 10000)
        self.spinS['a'].setSingleStep(1)
        self.spinS['a'].setValue(1)
        self.spinS['a'].setEnabled(False)

        self.spinS['b'] = QDoubleSpinBox()
        self.spinS['b'].setRange(-10000, 10000)
        self.spinS['b'].setSingleStep(1)
        self.spinS['b'].setValue(1)
        self.spinS['b'].setEnabled(False)

        self.checkBoxS = QCheckBox()
        self.checkBoxS.setChecked(False)
        self.checkBoxS.stateChanged \
                       .connect(lambda state:
                                (self.spinS['a'].setEnabled(state),
                                 self.spinS['b'].setEnabled(state)))

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.spinS['a'])
        layout.addWidget(self.spinS['b'])
        layout.addWidget(self.checkBoxS)

        scale = QWidget()
        scale.setLayout(layout)

        return scale
        

    def initRotate(self):
        """ Cria todos os componentes referentes a rotação e
        retorna o widget referente a rotação.
        """
        
        label = QLabel('Rotação')

        self.spinRT = QSpinBox()
        self.spinRT.setRange(-360, 360)
        self.spinRT.setSingleStep(1)
        self.spinRT.setValue(0)
        self.spinRT.setEnabled(False)
        
        self.checkBoxRT = QCheckBox()
        self.checkBoxRT.setChecked(False)
        self.checkBoxRT.stateChanged \
                       .connect(lambda state: self.spinRT.setEnabled(state))

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.spinRT)
        layout.addWidget(self.checkBoxRT)

        rotation = QWidget()
        rotation.setLayout(layout)

        return rotation


    def initReflexion(self):
        """ Cria todos os componentes referentes a reflexão  e
        retorna o widget referente a reflexao.
        """

        label = QLabel('Reflexão')

        btnRF = {}
        btnRF['x'] = QRadioButton('x')
        btnRF['y'] = QRadioButton('y')
        btnRF['o'] = QRadioButton('origem')

        btnRF['x'].setChecked(True)
        for btn in btnRF.values():
            btn.setEnabled(False)
        
        self.groupRF = QButtonGroup(self)
        self.groupRF.addButton(btnRF['x'])
        self.groupRF.addButton(btnRF['y'])
        self.groupRF.addButton(btnRF['o'])

        self.checkBoxRF = QCheckBox()
        self.checkBoxRF.setChecked(False)
        self.checkBoxRF.stateChanged \
                       .connect(lambda state: (btnRF['x'].setEnabled(state),
                                               btnRF['y'].setEnabled(state),
                                               btnRF['o'].setEnabled(state)))
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(btnRF['x'])
        layout.addWidget(btnRF['y'])
        layout.addWidget(btnRF['o'])
        layout.addWidget(self.checkBoxRF)

        reflexion = QWidget()
        reflexion.setLayout(layout)

        return reflexion


    def initShear(self):
        """ Cria todos os componentes referentes a cisalhamento e
        retorna o widget referente ao cisalhamento.
        """

        label = QLabel('Cisalhamento')
        
        self.spinSH = QSpinBox()
        self.spinSH.setRange(-10000, 10000)
        self.spinSH.setSingleStep(1)
        self.spinSH.setValue(0)
        self.spinSH.setEnabled(False)

        btnSH = {}
        btnSH['x'] = QRadioButton('x')
        btnSH['y'] = QRadioButton('y')

        btnSH['x'].setChecked(True)
        for btn in btnSH.values():
            btn.setEnabled(False)

        self.groupSH = QButtonGroup(self)
        self.groupSH.addButton(btnSH['x'])
        self.groupSH.addButton(btnSH['y'])

        self.checkBoxSH = QCheckBox()
        self.checkBoxSH.setChecked(False)
        self.checkBoxSH.stateChanged \
                       .connect(lambda state: (self.spinSH.setEnabled(state),
                                               btnSH['x'].setEnabled(state),
                                               btnSH['y'].setEnabled(state)))
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.spinSH)
        layout.addWidget(btnSH['x'])
        layout.addWidget(btnSH['y'])
        layout.addWidget(self.checkBoxSH)

        shear = QWidget()
        shear.setLayout(layout)

        return shear
