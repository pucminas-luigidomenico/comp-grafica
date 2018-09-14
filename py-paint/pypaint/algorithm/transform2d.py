import numpy as np

def identity():
    """ Retorna a matriz identidade de dimensão 3x3. """
    
    return np.identity(3)

def translation(a, b):
    """ Retorna a matriz referente a translação. """
    
    return np.mat([[1, 0, a], [0, 1, b], [0, 0, 1]])


def scale(a, b):
    """ Retorna a matriz referente a escala. """
        
    return np.mat([[a, 0, 0], [0, b, 0],[0, 0, 1]])


def rotate(theta):
    """ Retorna a matriz referente a rotação. """
    
    rad = np.deg2rad(theta)
    return np.mat([[np.cos(rad), -np.sin(rad), 0],
                   [np.sin(rad), np.cos(rad), 0],
                   [0, 0, 1]])


def reflexion(axis):
    """ Retorna a matriz referente a reflexão. """
    
    x = 1 if axis == 'x' else -1
    y = 1 if axis == 'y' else -1
    return np.mat([[x, 0, 0], [0, y, 0], [0, 0, 1]])


def shear(axis, value):
    """ Retorna a matriz referente ao cisalhamento. """
    
    a = value if axis == 'x' else 0
    b = value if axis == 'y' else 0

    return np.mat([[1, a, 0], [b, 1, 0], [0, 0, 1]])


def transformMatrix(translation, scale, rotate, reflexion, shear):
    """ Retorna a matriz composta da multiplicação de todas as transformações. """
    
    return translation * scale * rotate * reflexion * shear


def toOrigin(matrix, p):
    """ Retorna a matriz referente ao posicionamento do ponto na origem,
    para a realização das transformações a partir do ponto p. """
    
    to = translation(-p['x'], -p['y'])
    undo = translation(p['x'], p['y'])

    return undo * matrix * to


def transformPoint(matrix, point):
    """ Retorna o ponto alterado pelas transformações presentes na matriz. """
    
    pointMatrix = np.mat([point['x'], point['y'], 1]).reshape(3, 1)
    x, y, _ = matrix * pointMatrix
    return {'x': round(np.asscalar(x)), 'y': round(np.asscalar(y))}
