import uuid


class Pagamento:

    def __init__(self, valor):
        self._valor = valor

    # Com a Exceção na classe mão, forçamos as classes filhas a terem suas próprias funções pagar
    def pagar(self):
        raise NotImplementedError("Você deve implementar este método!")


# Pagamento por transferencia é como pagamento por Pix, né?
class PagaPorPix(Pagamento):
    def __init__(self, valor, cod_remetente, cod_destinatario):
        super().__init__(valor)
        self._cod_remetente = cod_remetente
        self._cod_destinatario = cod_destinatario

    def pagar(self):
        texto = f""" Usuario {self._cod_remetente} enviou {self._valor} ao usuário {self._cod_destinatario}"""

        print(texto)


if __name__ == '__main__':
    pagamento_pix = PagaPorPix(1500, '0055333222', '1145677433')

    pagamento_pix.pagar()