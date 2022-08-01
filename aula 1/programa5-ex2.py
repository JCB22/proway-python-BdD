"""

1 - Criar uma classe que chamada Container. Essa classe tera um atributo de nome "espaços",
que vai reprezentar os espaços vagos nesse container

2 - Criar 2 classes: Uma chamado Baú, e outra chamada Mochila que devem herdar da classe Container.
3 - A classe Bau deve ter o alor do atributo espaços em 30, e a classe Mochila em 10
4 - Criar a classe Item, que tera 2 atributos: Nome e tamanho
5 - Herdando da classe Item, voce pode herdar m numero ilimitado de classes (Espada, Cantil, etc) que terao
que ter a informaão de tamanho e nome
6 - Deve ser possivel botar itens dentro de qualquer container, respeitando o espaço máximo do container. Por
    exemplo: Se dentro de uma Mochila só podem caber itens em que a soma do tamanho não ultrapassem 10
8 - Antes de colocar um item no container, sera feito uma verificaçao da quantidade de espaços disponiveis nesse
container. Se a quantidade maxima de espaços for ultrapasssado, devera ser lançado
uma exceçao de nome EspaçoInsuficiente

"""