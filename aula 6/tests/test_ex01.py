import unittest
from exercicios import ex01


class TestExercicios(unittest.TestCase):

    def test_ex01_deve_retornar_texto_em_ordem_alfabetica(self):

        texto = "abecedario"
        saida_esperada = "aabcdeeior"

        resultado = ex01(texto)

        self.assertEqual(saida_esperada, resultado)

    def test_ex_01_deve_dar_erro_caso_input_nao_seja_string(self):

        texto = 1234

        with self.assertRaises(Exception) as exc_info:
            resultado = ex01(texto)

        self.assertEqual(exc_info.exception.args[0], "Você deve passar um texto para a função!")


if __name__ == "__main__":
    unittest.main()
