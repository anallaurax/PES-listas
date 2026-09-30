'''3 – Crie uma classe chamada ContaBancaria com:
• Atributos: titular e saldo.
• Um método chamado depositar que recebe um valor e adiciona ao saldo.
• Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
validar o saldo).
• Um método chamado mostrar_saldo que retorna o saldo atual.
Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor2):
        self.saldo = self.saldo - valor2

    def mostar_saldo(self):
        return f' O saldo atual é {self.saldo}'
    

contat = input('Digite o nome do titular da conta: ')
s = float(input('Digite o saldo da conta: '))

contabanc1 = ContaBancaria(contat, s)

deposito = float(input('Digite o valor que deseja depositar: '))
contabanc1.depositar(deposito)

print(f'O saldo depois do depósito foi de R$ {contabanc1.mostrar_saldo():.2f}')

saque = float(input('Digite o valor que deseja sacar da conta: '))
contabanc1.sacar(saque)

print(f'O titular da conta é {contabanc1.titular}')
print(f'O saldo depois do saque foi de R$ {contabanc1.mostrar_saldo():.2f}')
print(f'O saldo final foi de R$ {contabanc1.mostrar_saldo():.2f}')

