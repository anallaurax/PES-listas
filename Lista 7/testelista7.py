class CarteiraDeMotorista: #01
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
    
#02
class MarcadorDePagina:
    def __init__(self, pagina_atual, livro):
        self.pagina_atual = pagina_atual
        self.livro = livro

    def __repr__(self):
        return f"MarcadorDePagina(pagina_atual={self.pagina_atual}, livro={self.livro.titulo})"

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if pagina < 1 or pagina > self.total_paginas:
            print(f"Página inválida. O livro '{self.titulo}' tem {self.total_paginas} páginas.")
            return False
        if self.marcador is None:
            self.marcador = MarcadorDePagina(pagina)
            return True
        else:
            self.marcador.pagina_atual = pagina
            return True
        

#03
class Motor:
    def __init__(self, potencia_cv):
        self.potencia_cv = potencia_cv
        self.ligado = False


    def __repr__(self):
        return f"Motor potência = {self.potencia_cv}, ligado:={self.ligado})"
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def esta_ligado(self):
        return self.ligado
    
class Carro:
    def __init__(self, modelo, ano, motor_potencia):
        self.modelo = modelo
        self.ano = ano
        self.motordocarro = Motor(motor_potencia)

    def __repr__(self):
        return f"Modelo do carro ={self.modelo}, ano do carro ={self.ano}, moto do carror ={self.motordocarro}"        
      

    def ligar_carro(self):
        self.motordocarro.ligar()

    def desligar_carro(self):
        self.motordocarro.desligar()

    def esta_ligado(self):
        return self.motordocarro.esta_ligado()
    


# Criar carro 

m = input("Digite o modelo do carro: ")
a = int(input("Digite o ano do carro: "))
p = int(input("Digite a potência do motor do carro (em cv): "))

carro1 = Carro(m, a, p)

print(f"Carro criado teste: {carro1}")

if carro1.esta_ligado():
    print(f"O carro {carro1.modelo} está ligado.")
else:
    print(f"O carro {carro1.modelo} está desligado.")


'''# Programa Principal - primeira parte
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
print(f"Número da CNH: {pessoa.cnh.numero}, Categoria: {pessoa.cnh.categoria}")'''

