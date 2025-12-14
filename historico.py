class NoHistorico:
    """Representa um único empréstimo na lista encadeada."""
    def __init__(self, id_livro, id_usuario, data_emprestimo):
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.proximo = None  # Aponta para o próximo nó na lista

    def __str__(self):
        return f"Livro ID: {self.id_livro} | Usuário ID: {self.id_usuario} | Data: {self.data_emprestimo}"

class HistoricoEmprestimos:
    """Gerencia a Lista Encadeada do histórico de empréstimos."""
    def __init__(self):
        self.head = None  # O início da lista, inicialmente vazia

    def adicionar_registro(self, id_livro, id_usuario, data_emprestimo):
        """Adiciona um novo registro de empréstimo ao INÍCIO da lista (LIFO)."""
        novo_no = NoHistorico(id_livro, id_usuario, data_emprestimo)
        
        # 1. O 'próximo' do novo nó é o nó que era o 'head' anteriormente.
        novo_no.proximo = self.head
        
        # 2. O novo nó torna-se o novo 'head' (início) da lista.
        self.head = novo_no
        print("Registro de empréstimo adicionado ao histórico.")
        
    def exibir_historico(self):
        """Percorre a lista e exibe todos os registros."""
        if not self.head:
            print("Histórico de empréstimos está vazio.")
            return

        print("\n--- Histórico de Empréstimos ---")
        atual = self.head  # Começa pelo primeiro nó
        while atual:
            print(atual)
            atual = atual.proximo  # Move para o próximo nó
        print("-------------------------------")
