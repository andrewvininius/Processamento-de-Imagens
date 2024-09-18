import numpy as np

def inverter_cores(imagem):
    """ Inverte as cores de uma imagem.
    Assume que a imagem é um array NumPy de uma imagem em escala de cinza.
    """
    return 255 - imagem
