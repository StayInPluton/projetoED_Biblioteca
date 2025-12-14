class NoHistorico:
    """Representa um único empréstimo na lista encadeada."""
    def __init__(self, id_livro, id_usuario, data_emprestimo):
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.proximo = None  # Aponta para o próximo nó na lista



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

        if not self.head:
            return [] # Retorna uma lista vazia se não houver registros

        registros = []
        atual = self.head 
        while atual:
            registros.append({
                'id_livro': atual.id_livro,
                'id_usuario': atual.id_usuario,
                'data_emprestimo': atual.data_emprestimo
            })
            atual = atual.proximo
        return registros # Retorna os dados puros