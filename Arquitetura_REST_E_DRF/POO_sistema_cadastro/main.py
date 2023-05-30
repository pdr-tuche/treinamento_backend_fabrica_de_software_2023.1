from anime import Anime, Crunchyroll

crunch = Crunchyroll()
while True:
    nome = input('digite um nome de anime')
    gen = input('digite o genero do anime')

    anime = Anime(nome, gen)
    
    crunch.adicionar_anime(anime)

    flag = input('deseja continuar cadastrando?')


    if flag != 'sim':
        break



crunch.mostrar_animes()