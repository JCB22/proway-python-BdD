"""
POO

Composicao: Um objeto é composto por 1 ou mais objetos

"""
import random

NAIPES = ["\u2660", "\u2665", "\u2663", "\u2666"]
VALORES = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Baralho:
    def __init__(self):
        self._cartas = []

        for naipe in NAIPES:
            for valor in VALORES:
                self._cartas.append(Carta(valor=valor, naipe=naipe))

    def embaralhar(self):
        random.shuffle(self._cartas)

    # O método mágico __repr__ alterna o formato de exibição da classe quando ela está dentro de ium
    # container (lista, tupla, etc)
    def __repr__(self):
        texto = ""
        for carta in self._cartas:
            texto += str(carta) + "\n"
        return texto


class Carta:
    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    def __repr__(self):
        return f'{self._valor} de {self._naipe}'


if __name__ == "__main__":
    carta1 = Carta(4, "Copas")
    print(carta1)

    baralho = Baralho()
    baralho.embaralhar()
    print(baralho)
