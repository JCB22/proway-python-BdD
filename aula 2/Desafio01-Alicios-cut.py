

class Container:

    def __init__(self, nome="", espacos=0):
        self._espacos = espacos
        self._itens = []
        self._nome = nome
        self._espaco_atual = 0

    def _ha_espaco_disponivel(self):
        pass

    def add_item(self, item):
        if self._espaco_atual + item.tamanho > self._espacos:
            raise EspacoInsuficiente
        else:
            self._itens.append(item)
            self._espaco_atual += item.tamanho

    def remove_item(self, item):
        pass

    def info(self):

        espaco_itens = 0
        for item in self._itens:
            espaco_itens += item.tamanho
        texto = f"""
        Informações:
        
        Container: {self._nome}
        Espaço Máximo: {self.espacos}
        Espaço Ocupado: {espaco_itens}
        Itens: {self._itens}
        """

        print(texto)

    @property
    def espacos(self):
        return self._espacos

    @espacos.setter
    def espacos(self, novo_valor):
        self._espacos = novo_valor


class Bau(Container):
    def __init__(self):
        # Chamamos o método "__init__" da superclasse para
        # inicializar o atributo "_espacos" com o valor de 30
        super().__init__(espacos=30, nome="Baú")


class Mochila(Container):
    def __init__(self):
        super().__init__(espacos=10, nome="Mochila")


class Item:

    def __init__(self, nome="", tamanho=0):
        self._nome = nome
        self._tamanho = tamanho

    def __repr__(self):
        return f"""Item: {self._nome}. Tamanho: {self._tamanho}"""

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_valor):
        self._nome = novo_valor

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, novo_valor):
        self._tamanho = novo_valor


class Espada(Item):
    def __init__(self):
        super().__init__(nome="Espada", tamanho=5)


class Elmo(Item):
    def __init__(self):
        super().__init__(nome="Elmo", tamanho=4)


class Mapa(Item):
    def __init__(self):
        super().__init__(nome="Mapa", tamanho=3)


class Cantil(Item):
    def __init__(self):
        super().__init__(nome="Cantil", tamanho=3)


class EspacoInsuficiente(Exception):
    def __init__(self,*args, **kwargs):
        super().__init__(args, kwargs)
        self._message = "Espaço Insuficiente"


if __name__ == "__main__":
    elm = Elmo()
    esp = Espada()
    maap = Mapa()
    can = Cantil()

    for item in [elm, esp, maap, can]:
        print(f'{item.nome} Tamanho: {item.tamanho}')

    moc = Mochila()
    bau = Bau()

    try:
        moc.add_item(esp)
        moc.add_item(elm)
        moc.add_item(can)

        bau.add_item(elm)
        bau.add_item(esp)
        bau.add_item(maap)
        bau.add_item(can)
    except EspacoInsuficiente as exc:
        print('Espaço insuficiente')

    moc.info()
    bau.info()
