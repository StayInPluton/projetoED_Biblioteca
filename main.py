from livros import GerenciadorLivros
from reservas import GerenciadorReservas
from heap_popularidade import MaxHeapRanking
from historico import HistoricoEmprestimos
from emprestimos import GerenciadorEmprestimos

class Biblioteca:
    def __init__(self):
        # 1. Inicializa todas as estruturas de dados
        self.livros = GerenciadorLivros()
        self.ranking = MaxHeapRanking()
        self.reservas = GerenciadorReservas()
        self.historico = HistoricoEmprestimos() # A Lista Encadeada

        # 2. Inicializa o Gerenciador de Empréstimos, passando as estruturas necessárias
        self.emprestimos = GerenciadorEmprestimos(
            ranking=self.ranking, 
            reservas=self.reservas, 
            historico=self.historico 
        )

    def cadastrar_livro(self, id, titulo, autor):
        self.livros.cadastrar(id, titulo, autor)
        # Assumindo que o livro cadastrado deve ser inserido no ranking
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
            
    def exibir_historico(self):
        self.historico.exibir_historico()

# =======================================================
# FUNÇÃO DO MENU PRINCIPAL
# =======================================================
def menu():
    biblioteca = Biblioteca()
    
    # 📚 Pré-cadastro de alguns livros para teste rápido
    print("--- Inicializando Biblioteca com dados de teste ---")
    biblioteca.cadastrar_livro(101, "Estruturas de Dados Essenciais", "A. Programador")
    biblioteca.cadastrar_livro(102, "Algoritmos Rápidos", "B. Desenvolvedor")
    
    while True:
        print("\n====================================")
        print("           MENU PRINCIPAL           ")
        print("====================================")
        print("1. Emprestar Livro")
        print("2. Devolver Livro")
        print("3. Mostrar Ranking de Popularidade (Max Heap)")
        print("4. Mostrar Histórico de Empréstimos (Lista Encadeada)")
        print("5. Sair")
        print("------------------------------------")
        
        escolha = input("Escolha uma opção: ")

        try:
            if escolha == '1':
                id_livro = int(input("  [Empréstimo] ID do Livro: "))
                id_usuario = input("  [Empréstimo] ID do Usuário: ")
                biblioteca.realizar_emprestimo(id_livro, id_usuario)
            
            elif escolha == '2':
                id_livro = int(input("  [Devolução] ID do Livro: "))
                biblioteca.realizar_devolucao(id_livro)
                
            elif escolha == '3':
                biblioteca.ranking.mostrar_ranking()
                
            elif escolha == '4':
                biblioteca.exibir_historico()
                
            elif escolha == '5':
                print("Saindo do sistema. Obrigado!")
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