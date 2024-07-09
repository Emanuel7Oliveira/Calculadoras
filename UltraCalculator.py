
# Cabeca da calculadora
class Contas:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2
    
    # Primeira funcao a qual soma 2 valore
    def somar(self):
        print(self.numero1 + self.numero2)
    
    def subtrai(self):
        print(self.numero1 - self.numero2)
    
    def multiplica(self):
        print(self.numero1 * self.numero2)
        
    def divide(self):
        print(self.numero1 / self.numero2)
    
    def menu(self):
        print('''Escolha uma das opções abaixo:
[1]Adição
[2]Subtração
[3]Multiplicação
[4]Divisão''')


# Aplica informacoes nas variaveis de Contas 
x = Contas(int(input('Numero1: ')), int(input('Numero2: ')))
x.menu()

user = int(input('...'))

 # Executa funcao da classe Contas para realizar as operacoes
if user == 1:
    x.somar()
elif user == 2:
    x.subtrai()
elif user == 3:
    x.multiplica()
elif user == 4:
    x.divide()