"""

OOP - Encapsulamento

Utiliza a abstração como base, porém trabalha mais com nivel de aplicacao. É o processo onde "protegemos"
determinadas propriedades ou métodos de serem "expostos".

A máquina de café terá que armazenar café, água, açúcar, leite e chocolate. O usuario poderá escoler a
bebida que quiser escolhendo uma das opções que ser~~ao mostradas, que são:
    1 - Café ( Café e agua )
    2 - Capuccino ( Café , Agua e Chocolate )
    3 - Leite ( Leite e Agua )
    4 - Chocolate ( Chocolate e Agua)

"""


class MaquinaDeCafe:

    def __init__(self, cafe=5000, leite=2000, chocolate=2000):
        self._cafe = cafe
        self._leite = leite
        self._chocolate = chocolate

    def criar_bebida(self, opcao):
        if opcao == 1:
            self._fazer_cafe()
        elif opcao == 2:
            self._fazer_leite()
        elif opcao == 3:
            self._fazer_capuccino()
        elif opcao == 4:
            self._fazer_chocolate()
        else:
            print("Opção Inválida")

    def _fazer_cafe(self):
        print('Preparando Café...')
        self._esquentar_agua()
        self._misturar()
        self._cafe -= 100

    def _fazer_capuccino(self):
        print("Preparando Capuccino...")
        self._esquentar_agua()
        self._misturar()
        self._cafe -= 50
        self._chocolate -= 50

    def _fazer_leite(self):
        print("Preparando Leite...")
        self._esquentar_agua()
        self._misturar()
        self._leite -= 100

    def _fazer_chocolate(self):
        print("Preparando Chocolate...")
        self._esquentar_agua()
        self._misturar()
        self._chocolate -= 100

    def _esquentar_agua(self):
        print("Esquentando Agua")

    def _misturar(self):
        print("Misturando...")


if __name__ == '__main__':
    texto = """
    Escolha a sua opção:
    
    1 - Café ( Café e agua )
    2 - Capuccino ( Café, Agua e Chocolate )
    3 - Leite ( Leite e Agua )
    4 - Chocolate ( Chocolate e Agua)
    
    """

    print(texto)

    opcao = int(input("Informe a opção escolhida: "))

    maquina_cafe = MaquinaDeCafe()

    try:
        maquina_cafe.criar_bebida(opcao)
    except BaseException:
        pass
    else:
        print("Bebida pronta!")
    finally:
        pass
