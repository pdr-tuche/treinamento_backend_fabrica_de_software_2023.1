from animal import Animal

class Catioro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print('auauauauauAuauauauauau')
