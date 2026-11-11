'''2 - Exercício 2: Computador e CPU (1..1).
Objetivo: Implementar um relacionamento obrigatório (Composição).
Classes: CPU e Computador.
Regras:
A classe CPU deve ter atributos fabricante (ex: "Intel") e modelo (ex: "i7-12700K").
• A classe Computador deve ter um atributo tipo (ex: "Desktop" ou "Notebook").
• Um Computador deve ter exatamente uma CPU para ser criado (1..1).
• O __init__ do Computador deve receber os dados necessários para criar sua
própria instância de CPU. O atributo computador.cpu nunca pode ser None.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:'''


class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

class Computador:
    def __init__(self, tipo, fabricante_cpu, modelo_cpu):
        self.tipo = tipo
        self.cpu = CPU(fabricante_cpu, modelo_cpu)


t= input("Digite o tipo do computador (Desktop/Notebook): ")
f = input("Digite o fabricante da CPU: ")
m = input("Digite o modelo da CPU: ")


computador = Computador(t, f, m)

print("\n--- Computador cadastrado ---")
print("Tipo:", computador.tipo)
print("Fabricante da CPU:", computador.cpu.fabricante)
print("Modelo da CPU:", computador.cpu.modelo)