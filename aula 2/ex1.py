"""

Criar um banco de dados que contenha:

ID
NOME
NOTA 1
NOTA 11
NOTA 111

"""
import sqlite3
import csv

if __name__ == '__main__':

    conn = sqlite3.connect('db.sqlite3')

    # Criar tabela
    comando = """
    CREATE TABLE IF NOT EXISTS tabela_alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            nota1 FLOAT NOT NULL,
            nota2 FLOAT NOT NULL,
            nota3 FLOAT NOT NULL
    )
    """

    conn.execute(comando)

    # Inserir um aluno

    # comando = """
    # INSERT INTO tabela_alunos(nome, nota1, nota2, nota3) values (
    # 'Jorge', 4.2, 7.4, 5.3
    # )
    # """
    #     conn.execute(comando)
    #     conn.commit()

    with open(file="alunos.csv", mode="r", encoding="utf-8") as _file:

        fieldnames = ["nome", "nota1", "nota2", "nota3"]
        csv_reader = csv.DictReader(_file, fieldnames=fieldnames, delimiter=";")

        for index, item in enumerate(csv_reader):
            if index > 0:
                comando = f"""
                INSERT INTO tabela_alunos(nome, nota1, nota2, nota3) values
                ("{item["nome"]}", {float(item["nota1"])}, {float(item["nota2"])}, {float(item["nota3"])})
                """

                conn.execute(comando)
                conn.commit()
