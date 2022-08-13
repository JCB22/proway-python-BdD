from database import engine, Base, session
from models import User, UserProfile, Post

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    result = session.query(User).all()

    print(f'Quantidade de registros na tabela tb_users: {len(result)}')

    users = [
        {'first_name': 'Amanda', 'last_name': 'dos Anjos', 'email': 'amanda_a@gmail.com', 'password': '123456'},
        {'first_name': 'Bruna', 'last_name': 'dos Anjos', 'email': 'bruna_a@gmail.com', 'password': '123456'},
        {'first_name': 'Carla', 'last_name': 'dos Anjos', 'email': 'clara_a@gmail.com', 'password': '123456'},
        {'first_name': 'Diana', 'last_name': 'dos Anjos', 'email': 'diana_a@gmail.com', 'password': '123456'}
    ]

    posts = [
        {'id': '1', 'title': 'my girlfriend hates me after she got me with her best friend',
         'content': 'I(M|32), and my girlfrend(F|29) blahblahblah'}
    ]

    if len(result) == 0:
        for user_info in users:

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

            for post_data in posts:

                if post_data.get('id') == user.id:
                    user.post.apppend(Post(
                        title=post_data.get('title'),
                        content=post_data.get('content')
                    ))

                user.posts.append(post_data)
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
