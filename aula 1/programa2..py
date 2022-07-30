# PascalCase    ->  Nomes de Classes de funções começam sempre com maiúsculas
# camelCase     ->  A primeira letra do nome deve ser minúscula
# snake_case    ->  Todas as letras são minusculas com as palavras compostas sao separadas por _
class Pokemon:

    shared = 1  # Atributo de classe

    # O init é chamado imediatamente após a classe ser instanciada
    # self é uma referencia a instancia do objeto
    def __init__(self, name, type, health, id):
        self._name = name   # Atributos de instância
        self._type = type
        self._health = health
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __repr__(self):
        return f"Nome: {self._name}\nTipo: {self._type}\nVida: {self._health}\nID:   {self._id}"

    # Os métodos comuns de uma classe devem ser definidos com o self como primeiro argumento
    def attack(self):
        print(f'{self._name} atacou!')

    def dodge(self):
        print(f"{self._name} desviou!")

    def evolve(self):
        print(f"{self._name} evoluiu!")


if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Elétrico", 70, 51)

    print(pikachu)

    pikachu.attack()
    pikachu.dodge()
    pikachu.evolve()

    pikachu.name = "Raichu"

    charizard = Pokemon("Charizard", ["Fogo", "Voador"], 200, 9)
    print(charizard)
    charizard.attack()
