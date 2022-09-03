import unittest
from prog01 import inverte_texto

class TestProg01(unittest.TestCase):

    def test_invert_texto_deve_retornar_texto_invertido(self):
        """


        """

        # Preparo ( Arrange )
        texto = "Python"
        saida_esperada  = "nohtyP"

        # Chamada ( Act )
        resultado = inverte_texto(texto)

        # Verificação ( Assert )
        self.assertEqual(saida_esperada, resultado)

    def test_inverte_texto_deve_gerar_erro_se_a_entrada_nao_for_string(self):
        # Arrange
        texto = 2019

        # Act
        with self.assertRaises(Exception) as exc_info:
            resultado = inverte_texto(texto)

        # Assert
        self.assertEqual(exc_info.exception.args[0], "Você deve passar um texto para a função!")


if __name__ == "__main__":
    unittest.main()