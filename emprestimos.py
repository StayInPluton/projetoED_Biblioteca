from heap_popularidade import Book

class GerenciadorEmprestimos:
    def __init__(self, ranking, reservas):
        self.ranking = ranking
        self.reservas = reservas

    def emprestar(self, livro, usuario):
        if livro.disponivel:
            livro.disponivel = False
            self.ranking.atualizar_popularidade(livro.id)
            print(f" Livro emprestado para {usuario}")
        else:
            self.reservas.reservar(livro.id, usuario)

    def devolver(self, livro):
        proximo = self.reservas.proximo(livro.id)
        if proximo:
            print(f" Livro reservado para {proximo}")
            self.ranking.atualizar_popularidade(livro.id)
        else:
            livro.disponivel = True
            print(" Livro devolvido ")
