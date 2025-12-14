from datetime import date
from heap_popularidade import Book
from historico import HistoricoEmprestimos

class GerenciadorEmprestimos:
    def __init__(self, ranking, reservas, historico: HistoricoEmprestimos):
        self.ranking = ranking
        self.reservas = reservas
        self.historico = historico

    def emprestar(self, livro, usuario):
        if livro.disponivel:
            livro.disponivel = False
            self.ranking.atualizar_popularidade(livro.id)
            data_hoje = date.today().strftime("%Y-%m-%d") 
            self.historico.adicionar_registro(livro.id, usuario, data_hoje)
            print(f" Livro emprestado para {usuario}")
        else:
            self.reservas.reservar(livro.id, usuario)

    def devolver(self, livro):
        proximo = self.reservas.proximo(livro.id)
        if proximo:
            data_hoje = date.today().strftime("%Y-%m-%d")
            self.historico.adicionar_registro(livro.id, proximo, data_hoje)
            print(f" Livro reservado para {proximo}")
            self.ranking.atualizar_popularidade(livro.id)
        else:
            livro.disponivel = True
            print(" Livro devolvido ")
