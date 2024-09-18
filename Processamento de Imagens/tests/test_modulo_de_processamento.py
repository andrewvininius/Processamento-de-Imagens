import unittest
import numpy as np
from nome_do_pacote.modulo_de_processamento import inverter_cores

class TestProcessamentoDeImagem(unittest.TestCase):
    def test_inverter_cores(self):
        imagem_teste = np.array([[0, 255], [128, 127]], dtype=np.uint8)
        imagem_esperada = np.array([[255, 0], [127, 128]], dtype=np.uint8)
        imagem_resultante = inverter_cores(imagem_teste)
        np.testing.assert_array_equal(imagem_resultante, imagem_esperada)

if __name__ == '__main__':
    unittest.main()
