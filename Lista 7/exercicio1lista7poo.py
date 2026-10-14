'''1 - Livro e MarcadorDePagina (0..1).
Objetivo: Implementar um relacionamento opcional simples.
Classes: MarcadorDePagina e Livro.
Regras:
• A classe MarcadorDePagina deve ter um atributo pagina_atual.
• A classe Livro deve ter um atributo titulo e um total_paginas.
• Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
0..1).
• Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
um marcador, apenas atualize a pagina_atual dele.
Comprove o funcionamento da sua implementação no programa principal.'''

class MarcadorDePagina:
    def __init__(self, pagina_atual, livro):
        self.pagina_atual = pagina_atual
        self.livro = livro

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
            self.marcador = MarcadorDePagina(pagina, self)
            return True
        else:
            self.marcador.pagina_atual = pagina
            return True
        

# Programa principal
t = input("Digite o título do livro: ")
p = int(input("Digite o total de páginas do livro: "))
livro1 = Livro(t,p)

# Adicionando marcador na página 
if livro1.adicionar_marcador(p):
    print(f"Marcador adicionado na página {livro1.marcador.pagina_atual} do livro '{livro1.titulo}'.")  