'''Crie uma classe "Animal" com os atributos nome e idade, e métodos para emitir um som característico e se movimentar.
'''

from animal import Animal
from catioro import Catioro

animal = Animal('cachorro', 19)
catioro = Catioro('sully', 2, 'monstrinho')

animal.emitir_som() # output: estou emitindo o som
catioro.emitir_som() # output: auauauauauAuauauauauau 🐶

animal.movimentar() # output: estou me movimentando =)
catioro.movimentar() # output: estou me movimentando =)

catioro.apresentar() # output: ola ^^ meu nome é sully tenho 2 anos e sou da raça monstrinho
animal.apresentar() # metodo apresentar nao existe na classe Animal, irá acontecer um erro nesta linha