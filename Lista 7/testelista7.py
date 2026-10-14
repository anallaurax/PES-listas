class CarteiraDeMotorista:
    def __init__(self, numero, categoria):
        self.numero = numero
        self.categoria = categoria
    def __repr__(self):
        return f"CarteiraDeMotorista(numero={self.numero}, categoria={self.categoria})"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.cnh = None
    def tirar_habilitacao(self, numero, categoria):
        if self.cnh is None:
            self.cnh = CarteiraDeMotorista(numero, categoria)
        else:
            print(f"{self.nome} já possui uma CNH: {self.cnh}")
    def eh_habilitada(self):
        if self.cnh is None:
            return "Não possui habilitação"
        else:
            return 'Possui habilitação!'
        
    def __repr__(self):
        return f"Pessoa: nome={self.nome}, cnh={self.cnh}"
    
# Programa Principal - primeira parte
n = input("Digite o nome da pessoa: ")
print(f"Criando o objeto '{n}'...")
pessoa = Pessoa(n)

print(f"Objeto criado: {pessoa}")

# --- Verificando o estado inicial ('0') ---
print(f"A {pessoa.nome} é habilitada? {pessoa.eh_habilitada()}")
print(f"CNH da {pessoa.nome}: {pessoa.cnh}")  # O atributo é None

# --- Mudando o estado para '1' ---
print(f"\n{pessoa.nome} foi tirar a habilitação...")

num = int(input("Digite o número da CNH: "))
cat = input("Digite a categoria da CNH: ").upper()
sucesso = pessoa.tirar_habilitacao(num, cat)

if sucesso:
    print(f"{pessoa.nome} agora é habilitada!")
else:
    print(f"{pessoa.nome} não conseguiu tirar a habilitação.")

print(f"A {pessoa.nome} é habilitada? {pessoa.eh_habilitada()}")
print(f"CNH da {pessoa.nome}: {pessoa.cnh}")  # O atributo agora é um objeto CarteiraDeMotorista
print(f"Número da CNH: {pessoa.cnh.numero}, Categoria: {pessoa.cnh.categoria}")