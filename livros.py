from time import sleep
class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.popularidade = 0

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.titulo} - {self.autor} ({status})"


class GerenciadorLivros:
    def __init__(self):
        self.livros = {}

    def cadastrar(self, id, titulo, autor):
        if id in self.livros:
            print("livro já cadastrado.")
            sleep(2)
            return
        self.livros[id] = Livro(id, titulo, autor)
        print("Livro cadastrado com sucesso.")
        sleep(2)

    def listar(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros.values():
            print(livro)

    def buscar(self, id):
        return self.livros.get(id)
