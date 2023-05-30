class Anime:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def mostrar_dados(self):
        print(f'titulo: {self.titulo}, genero: {self.genero}')


class Crunchyroll:
    def __init__(self):
        self.lista = []

    def adicionar_anime(self, anime):
        self.lista.append(anime)

    def mostrar_animes(self):
        for elem in self.lista:
            print(f'titulo: {elem.titulo}')