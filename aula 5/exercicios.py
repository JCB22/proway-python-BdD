
def ex01(texto):
    """
    Exercicio 01

    Escreva uma função que receba um texto qualquer e organize as letras em ordem alfabetica
    Escreva também 2 testes unitários para esta função. Uma que retorne o texto em ordem alfabética
    e outro teste que capture a exceção caso o usuário passe um valor diferente de String para a função

    Crie um módulo tests/test_exercicios.py
    Crie a classe TestExercicios que conterá os testes unitários dos exercícios
    Dica: Converta a String para uma lista antes de ordenar as letras por ordem alfabética
    """
    if isinstance(texto, str):
        letras = list(texto)

        letras_ordenadas = sorted(letras, key=str.lower)

        return ''.join(letras_ordenadas)

    raise Exception("Você deve passar um texto para a função!")
