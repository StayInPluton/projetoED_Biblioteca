class Book:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.popularidade = 0  # contador

    def __repr__(self):
        return f"{self.titulo} ({self.popularidade} pts)"


class MaxHeapRanking:
    def __init__(self):
        self.heap = []  # lista que representa o heap

    # -------------------------
    # Função para subir o item
    # -------------------------
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        
        if self.heap[index].popularidade > self.heap[parent].popularidade:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    # -------------------------
    # Função para descer o item
    # -------------------------
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left].popularidade > self.heap[largest].popularidade:
            largest = left

        if right < len(self.heap) and self.heap[right].popularidade > self.heap[largest].popularidade:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    # -------------------------
    # Inserir livro no ranking
    # -------------------------
    def inserir(self, book: Book):
        self.heap.append(book)
        self._heapify_up(len(self.heap) - 1)

    # -------------------------
    # Atualizar popularidade
    # -------------------------
    def atualizar_popularidade(self, book_id):
        for i, book in enumerate(self.heap):
            if book.id == book_id:
                book.popularidade += 1
                self._heapify_up(i)
                return True
        return False

    # -------------------------
    # Obter o top N do ranking
    # -------------------------
    def top_n(self, n=5):
        lista = sorted(self.heap, key=lambda b: b.popularidade, reverse=True)
        return lista[:n]

    # -------------------------
    # Exibir ranking completo
    # -------------------------
    def mostrar_ranking(self):
        print("\n📊 Ranking de Livros Mais Populares")
        print("------------------------------------")
        lista = sorted(self.heap, key=lambda b: b.popularidade, reverse=True)
        for pos, book in enumerate(lista, start=1):
            print(f"{pos}. {book.titulo} — {book.popularidade} ponto(s)")
