

class SenhaIncorretaError(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.message = "Senha incorreta!"


if __name__ == "__main__":
    try:
        senha = input("Escreva sua senha")

        if senha != "456":

            raise SenhaIncorretaError("Senha Incorreta!")

    except SenhaIncorretaError as exc:
        print(exc.message)

    # Roda quando não rolar uma exception
    else:
        print("Bem vindo à máquina!")

    finally:
        print("Saindo da máquina...")