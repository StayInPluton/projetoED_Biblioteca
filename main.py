import os
from time import sleep
from livros import GerenciadorLivros
from reservas import GerenciadorReservas
from heap_popularidade import MaxHeapRanking
from historico import HistoricoEmprestimos
from emprestimos import GerenciadorEmprestimos


def limpar_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')


class Biblioteca:
    def __init__(self):
        # 1. Inicializa todas as estruturas de dados
        self.livros = GerenciadorLivros()
        self.ranking = MaxHeapRanking()
        self.reservas = GerenciadorReservas()
        self.historico = HistoricoEmprestimos()

        # 2. Inicializa o Gerenciador de Empréstimos, passando as estruturas necessárias
        self.emprestimos = GerenciadorEmprestimos(
            ranking=self.ranking,
            reservas=self.reservas,
            historico=self.historico
        )

    def cadastrar_livro(self, id, titulo, autor):
        self.livros.cadastrar(id, titulo, autor)
        livro_obj = self.livros.buscar(id)
        if livro_obj:
            self.ranking.inserir(livro_obj)

    def realizar_emprestimo(self, id_livro, id_usuario):
        livro = self.livros.buscar(id_livro)
        if livro:
            self.emprestimos.emprestar(livro, id_usuario)
        else:
            print("Erro: Livro não encontrado.")

    def realizar_devolucao(self, id_livro):
        livro = self.livros.buscar(id_livro)
        if livro:
            self.emprestimos.devolver(livro)
        else:
            print("Erro: Livro não encontrado.")

    def obter_titulo_livro(self, id_livro):
        """Busca e retorna o título de um livro pelo ID."""
        # Assume que você já tem este método para buscar o objeto livro
        livro = self.livros.buscar(id_livro) 
        if livro:
            return livro.titulo
        return "Livro Desconhecido" # Caso o livro não exista

    def exibir_historico(self):
        dados_historico = self.historico.exibir_historico()
        
        if not dados_historico:
            print("Histórico de empréstimos está vazio.")
            return

        print("\n====================================")
        print("     HISTÓRICO DE EMPRÉSTIMOS")
        print("====================================")
        
        pos = 1
        for registro in dados_historico:
            titulo = self.obter_titulo_livro(registro['id_livro'])
            
            print(
                f"{pos}. Título: {titulo} | "
                f"Nome do Usuário: {registro['id_usuario']} | "
                f"Data: {registro['data_emprestimo']}"
            )
            pos += 1
        print("------------------------------------")


def menu():
    biblioteca = Biblioteca()

    limpar_terminal()
    while True:
        sleep(2.5)
        limpar_terminal()
        print("\n====================================")
        print("           MENU PRINCIPAL           ")
        print("====================================")
        print("1. Cadastrar Livro")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Mostrar Ranking de Popularidade")
        print("5. Mostrar Histórico de Empréstimos")
        print("6. Sair")
        print("------------------------------------")

        escolha = input("Escolha uma opção: ")

        try:
            if escolha == '1':
                limpar_terminal()
                print("\n====================================")
                print("           CADASTRO DE LIVROS           ")
                print("====================================")

                id_livro = int(input("  ID do Livro (número): "))
                titulo = input("  Título do Livro: ")
                autor = input("  Autor do Livro: ")
                biblioteca.cadastrar_livro(id_livro, titulo, autor)

            elif escolha == '2':
                limpar_terminal()
                print("\n====================================")
                print("           EMPRÉSTIMO           ")
                print("====================================")
                id_livro = int(input("  ID do Livro: "))
                id_usuario = input("  Nome do Usuário: ")
                biblioteca.realizar_emprestimo(id_livro, id_usuario)
            
            elif escolha == '3':
                limpar_terminal()
                print("\n====================================")
                print("           DEVOLUÇÃO           ")
                print("====================================")
                id_livro = int(input("  ID do Livro: "))
                biblioteca.realizar_devolucao(id_livro)
                
            elif escolha == '4':
                limpar_terminal()
                print("\n====================================")
                print("           RANKING DE POPULARIDADE    ")
                print("====================================")
                biblioteca.ranking.mostrar_ranking()
                sleep(5)
                
            elif escolha == '5':
                limpar_terminal()
                biblioteca.exibir_historico()
                sleep(5)
                
            elif escolha == '6':
                limpar_terminal()
                print("\n====================================")
                print("      Saindo do sistema. Obrigado!    ")
                print("====================================")
                sleep(2)
                limpar_terminal()
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para o ID do Livro.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# =======================================================
# PONTO DE ENTRADA DO PROGRAMA
# =======================================================
if __name__ == "__main__":
    menu()