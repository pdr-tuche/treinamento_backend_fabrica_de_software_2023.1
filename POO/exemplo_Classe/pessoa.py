class Pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        return f'olá me chamo {self.nome} e tenho {self.idade} nome'