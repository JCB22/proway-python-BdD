
class Container:
    def __init__(self, nome, espaco):
        self._nome = nome
        self._espaco = espaco
        self._itens = []

    def __str__(self):
        return f'Nome {self._nome} | Espaço Restante: {self._espaco} | Itens: {self._itens}'

    @property
    def nome(self):
        return self._nome

    def botar(self, item):
        if self._espaco - item.tamanho >= 0:
            self._itens.append(item)
            self._espaco -= item.tamanho
            print(f"{item.nome} inserido no(a) {self.nome}")
        else:
            print("Muito grande para o espaço restante")

    def retirar(self, item):
        n = 0
        for i in self._itens:
            if i == item:
                self._espaco += item.tamanho
                print(f"{item.nome} retirado do(a) {self.nome}")
                del self._itens[n]
                break
            n += 1


class Bau(Container):
    def __init__(self, nome='Baú', espaco=30):
        super().__init__(nome, espaco)


class Mochila(Container):
    def __init__(self, nome='Mochila', espaco=10):
        super().__init__(nome, espaco)


class Item:
    def __init__(self, nome, tamanho=0):
        self._nome = nome
        self._tamanho = tamanho
        if self._tamanho == 0:
            raise NotImplementedError('Tamanho não existe!')

    def __repr__(self):
        return f'Item: {self._nome} | Tamanho: {self._tamanho}'

    @property
    def nome(self):
        return self._nome

    @property
    def tamanho(self):
        return self._tamanho


class Espada(Item):
    def __init__(self, nome="Espada", tamanho=6):
        super().__init__(nome, tamanho)


class Cantil(Item):
    def __init__(self, nome="Cantil", tamanho=3):
        super().__init__(nome, tamanho)


class Mapa(Item):
    def __init__(self, nome="Mapa", tamanho=3):
        super().__init__(nome, tamanho)


if __name__ == '__main__':
    mochila = Mochila()
    espada = Espada()
    mapa = Mapa()
    cantil = Cantil()

    mochila.botar(espada)
    mochila.botar(mapa)
    mochila.botar(cantil)
    mochila.retirar(espada)

    print(mochila)

    bau = Bau()
    for _ in range(6):
        bau.botar(espada)
