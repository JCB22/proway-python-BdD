from database import engine, Base, session
from models import User, UserProfile, Post

if __name__ == '__main__':

    # Cria as tabelas definidas no módulo models.py
    Base.metadata.create_all(engine)

    # O método all() trás todos os registros da tabela mapeada para a model passada
    # como argumento de query(). No exemplo abaixo, é a model User.
    # SELECT * FROM tb_users
    result = session.query(User).all()

    print(f'Quantidade de registros na tabela tb_users: {len(result)}')

    users = [
        {'first_name': 'Amanda', 'last_name': 'dos Anjos', 'email': 'amanda_a@gmail.com', 'password': '123456'},
        {'first_name': 'Bruna', 'last_name': 'dos Anjos', 'email': 'bruna_a@gmail.com', 'password': '123456'},
        {'first_name': 'Carla', 'last_name': 'dos Anjos', 'email': 'clara_a@gmail.com', 'password': '123456'},
        {'first_name': 'Diana', 'last_name': 'dos Anjos', 'email': 'diana_a@gmail.com', 'password': '123456'}
    ]

    posts = [
        {"user_id": 1, "title": "A linguagem Python", "content": "Python é muito legal."},
        {"user_id": 1, "title": "A linguagem C++", "content": "C++ é muito poderoso."},
        {"user_id": 2, "title": "Docker", "content": "Docker é uma mão na roda."},
    ]

    if len(result) == 0:
        for index, user_info in enumerate(users):

            user = User(email=user_info.get('email'), password=user_info.get('password'))

            session.add(user)
            session.commit()

            user_profile = UserProfile(
                id=user.id,
                first_name=user_info.get('first_name'),
                last_name=user_info.get('last_name')
            )

            session.add(user_profile)
            session.commit()

            user_profile = UserProfile(
                id=user.id,
                first_name=user_info.get("first_name"),
                last_name=user_info.get("last_name")
            )

            session.add(user_profile)
            session.commit()

            for post_data in posts:

                if post_data.get('id') == user.id:
                    post = Post(
                        title=post_data.get('title'),
                        content=post_data.get('content')
                    )

                    # O objeto do tipo Post está sendo salvo na tabela de maneira indireta, pois ele foi adicionado
                    # a lista de posts do objeto user que faz referência a model Post
                    user.posts.append(post)
                    session.add(user)
                    session.commit()

    elif len(result) > 0:
        users = session.query(User).all()

        print('Lista de usuários cadastrados:')
        for user in users:
            user_profile = session.query(UserProfile).filter(UserProfile.id == user.id).first()

            output = f'''
            ID do usuario: {user.id},
            Email: {user.email}
            Nome Completo: {user_profile.first_name} {user_profile.last_name}
            '''

            print(output)
