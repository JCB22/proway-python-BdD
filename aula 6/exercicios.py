import requests

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


def ex02(nome_do_pokemon):
    """
    Exercício 02
    Essa função receberá um nome de pokemon, e vai consultas as informações do pokemon
    Endereço da API: https://pokeapi.co/api/v2/pokemon/{nome_do_pokemon}
    As informações que devem ser retornadas pela função são:
    Experiência base (base_experience)
    Altura (height)
    ID (id)
    Nome (name)
    Peso (weight)
    Essa função deve retornar um dicionário com essas informações
    Deve-se criar um 2 testes unitários: 1 Onde a chamada é feita corretamente, outro onde o usuário passa um nome
    de pokemon que não existe.
    PS: As chamadas para a API devem ser mockadas
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_do_pokemon}")
    resultado = response.json()
    species = resultado.get('species')
    types = resultado.get('types')
    output_type = ""
    for type in types:
        # type : Dict
        output_type += type['type']['name'] + "|"

    saida = {
        "nome": resultado.get('name'),
        "id": resultado.get('id'),
        "type(s)": "|" + output_type

    }

    return saida
