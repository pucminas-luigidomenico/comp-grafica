import os

from PyQt5.QtGui import QIcon

PATH = os.path.join(os.path.dirname(__file__), '../../images/')

LINE_ICON = 'line_icon.png'
CIRC_ICON = 'circ_icon.png'
CLEAR_ICON = 'clear_icon.png'
TRANSFORM_ICON = 'transform_icon.png'
CLIP_ICON = 'clip_icon.png'
FILL_ICON = 'fill_icon.png'
BEZIER_ICON = 'bezier_icon.png'

def lineIcon():
    """ Retorna o ícone referente a ferramenta de desenho de retas. """
    
    return QIcon(PATH + LINE_ICON)


def circIcon():
    """ Retorna o ícone referente a ferramenta de desenho de circunferências. """
    
    return QIcon(PATH + CIRC_ICON)


def clearIcon():
    """ Retorna o ícone referente a ferramenta de limpeza da tela. """
    
    return QIcon(PATH + CLEAR_ICON)


def transformIcon():
    """ Retorna o ícone referente a ferramenta de transformações. """
    
    return QIcon(PATH + TRANSFORM_ICON)


def clipIcon():
    """ Retorna o ícone referente a ferramenta de recorte. """
    
    return QIcon(PATH + CLIP_ICON)


def fillIcon():
    """ Retorna o ícone referente a ferramenta de preenchimento. """
    
    return QIcon(PATH + FILL_ICON) 


def bezierIcon():
    """ Retorna o ícone referente a ferramenta de curva de bezier. """
    
    return QIcon(PATH + BEZIER_ICON) 
