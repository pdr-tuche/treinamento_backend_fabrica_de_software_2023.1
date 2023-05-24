from animal import Animal

class Catioro(Animal):
    #esse "construtor" chama o construtor da superclasse(Animal) para que se utilize a mesma implementacao do construtor da classe Animal
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        # criando um atributo propio para classe Catiorro
        self.raca = raca

    #sobrescrevendo metodo emitir_som que foi herdado da classe Animal
    def emitir_som(self):
        print('auauauauauAuauauauauau 🐶')

    # método propio da classe Catioro
    def apresentar(self):
        print(f'ola ^^ meu nome é {self.nome} tenho {self.idade} anos e sou da raça {self.raca}')
