'''1 – Crie uma classe chamada Livro com:
• Atributos: titulo e autor.
• Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
Teste criando um objeto e chamando o método para exibir a descrição.'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def descrição(self):
        return f'O livro {self.titulo} foi escrito por {self.autor}'
    





t = input('Digite o nome do titulo do livro:')
a = input('Digite o nome do autor do livro:')

autor1 = Livro(t,a)


print(autor1.descrição())
