
# Cabeca da calculadora
class Contas:
    def __init__(self, num1, num2, form):
        self.numero1 = num1
        self.numero2 = num2
        self.formatar = form
    
    # Primeira funcao a qual soma 2 valore
    def somar(self):
        total = self.numero1 + self.numero2
        formatar = format(total, ",").replace(",", ".")
        print(f'O resultado da adição de {self.numero1} + {self.numero2} resulta em: ', formatar)
    
    def subtrai(self):
        total = self.numero1 - self.numero2
        formatar = format(total, ",").replace(",", ".")
        print(f'O resultado da subtração de {self.numero1} - {self.numero2} resulta em: ', total)
    
    def multiplica(self):
        total = self.numero1 * self.numero2
        formatar = format(total, ",").replace(",", ".")
        print(f'O resultado da multiplicação de {self.numero1} x {self.numero2} resulta em: ', total)
        
    def divide(self):
        total = self.numero1 / self.numero2
        formatar = format(total, ",").replace(",", ".")
        print(f'O resultado da divisão de {self.numero1} ÷ {self.numero2} resulta em: ', total)
    
    def menu(self):
        print('''Escolha uma das opções abaixo:
[1]Adição
[2]Subtração
[3]Multiplicação
[4]Divisão
[0]Encerrar''')

class resultado(Contas):
    def __init__(self, num1, num2, form, x):
        
        super().__init__(num1, num2, form)
        print("A")
        
    def execute(self):
# Aplica informacoes nas variaveis de Contas e exibe um menu ao usuario
print('Abaixo digite dois numeros que serão utilizados a seguir')
x = Contas(int(input('Numero1: ')), int(input('Numero2: ')), ",")
x.menu()

# Esta parte recolhe a informacao de qual operacao sera executada abaixo
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
else:
    print(':)')