"""

POO Herança -

"""
import uuid


class Pagamento:

    def __init__(self, valor):
        self._valor = valor

    # Com a Exceção na classe mãe, forçamos as classes filhas a terem suas próprias funções pagar
    def pagar(self):
        raise NotImplementedError("Você deve implementar este método!")


class PagamentoPorBoleto(Pagamento):

    def __init__(self, valor, numero, codigo):
        # A funcao super() executa um método ou acessa um atributo da superclasse
        super().__init__(valor)
        self._numero = numero
        self._codigo = codigo

    def pagar(self):
        texto = f"Boleto com o código {uuid.uuid4()} foi gerado com o valor de {self._valor}"
        print(texto)


class PagamentoPorCartaoDeCredito(Pagamento):
    def __init__(self, valor, numero, codigo):
        # A funcao super() executa um método ou acessa um atributo da superclasse
        super().__init__(valor)
        self._numero = numero
        self._codigo = codigo

    def pagar(self):
        texto = f"""
        Dados de pagamento via cartão:
        Valor: {self._valor}
        Número: {self._numero}
        Código: {self._codigo}
    """
        print(texto)

    def _tem_limite(self):
        return True


if __name__ == '__main__':
    pagamento_boleto = PagamentoPorBoleto(200, "203.436-00", "0000")

    pagamento_boleto.pagar()

    pagamento_cartao = PagamentoPorCartaoDeCredito(1000, '1235', '7642')

    pagamento_cartao.pagar()
