class GerenciadorReservas:
    def __init__(self):
        self.reservas = {}  

    def reservar(self, id_livro, usuario):
        if id_livro not in self.reservas:
            self.reservas[id_livro] = []

        self.reservas[id_livro].append(usuario)
        print(f" {usuario} entrou na fila de reserva do livro {id_livro}")

    def proximo(self, id_livro):
        if id_livro in self.reservas and self.reservas[id_livro]:
            return self.reservas[id_livro].pop(0)
        return None

    def mostrar(self, id_livro):
        fila = self.reservas.get(id_livro, [])
        if not fila:
            print("Nenhuma reserva.")
            return
        print("Fila de reservas:")
        for i, user in enumerate(fila, start=1):
            print(f"{i}. {user}")
