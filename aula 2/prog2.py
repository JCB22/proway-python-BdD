import sqlite3


if __name__ == '__main__':

    conn = sqlite3.connect("db.sqlite3")

    # TABELA USUARIOS
    sql = """
    CREATE TABLE IF NOT EXISTS tb_usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email text NOT NULL,
    senha TEXT NOT NULL
    )
    """

    conn.execute(sql)
    conn.commit()

    # TABELA PERFIL
    sql = """
    CREATE TABLE IF NOT EXISTS tb_perfil(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)    
    )
    """

    conn.execute(sql)
    conn.commit()

    # TABELA POSTAGENS
    sql = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(50) NOT NULL,
    post TEXT NOT NULL,
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)
    )
    """

    conn.execute(sql)
    conn.commit()

    # TABELA COMENTÁRIOS
    sql = '''
    CREATE TABLE IF NOT EXISTS tb_comentarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)
    FOREIGN KEY(id) REFERENCES tb_postagens(id)
    )
    '''

    conn.execute(sql)
    conn.commit()

    sql = '''
    CREATE TABLE IF NOT EXISTS tb_categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY(id) REFERENCES tb_postagens(id)
    )
    '''

    conn.execute(sql)
    conn.commit()

    sql = """
    CREATE TABLE IF NOT EXISTS tb_categorias_postagens(
    id_categoria INTEGER NOT NULL,
    id_postagem INTEGER NOT NULL,
    PRIMARY KEY(id_categoria, id_postagem),
    FOREIGN KEY(id_categoria) REFERENCES tb_categorias(id),
    FOREIGN KEY(id_postagem) REFERENCES tb_postagens(id)
    )
    """

    conn.execute(sql)
    conn.commit()
