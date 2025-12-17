# Biblioteca 

Aplicativo de linha de comando para gerenciar uma biblioteca pequena. Ele permite cadastrar livros, emprestar e devolver com fila de reservas, acompanhar popularidade por um ranking (max-heap) e consultar um histórico encadeado de empréstimos.

## Funcionalidades
- Cadastro de livros com verificação de IDs duplicados.
- Empréstimo de livros e devolução com atendimento automático da fila de reservas.
- Fila de reservas por livro (FIFO).
- Ranking de popularidade via max-heap, atualizado a cada empréstimo/devolução atendida.
- Histórico de empréstimos implementado como lista encadeada (ordem LIFO para inserções).
- Menu interativo para operar todas as ações.

## Estrutura do projeto
- `main.py`: ponto de entrada e menu principal (interface de linha de comando).
- `livros.py`: modelo `Livro` e `GerenciadorLivros` para cadastro/listagem/busca.
- `emprestimos.py`: `GerenciadorEmprestimos` para emprestar/devolver e atualizar ranking/histórico.
- `reservas.py`: `GerenciadorReservas` com fila por livro.
- `heap_popularidade.py`: max-heap para ranking de popularidade.
- `historico.py`: lista encadeada para armazenar o histórico de empréstimos.

## Pré-requisitos
- Python 3.10+ (biblioteca padrão apenas, sem dependências externas).

## Como executar
1) Clone o repositório e entre na pasta:
```bash
git clone https://github.com/StayInPluton/projetoED_Biblioteca.git 
&& cd projetoED_Biblioteca
```

2) Rode o menu interativo:
```bash
python main.py
```

## Uso rápido (menu)
- `1` Cadastrar Livro: informe ID numérico, título e autor.
- `2` Emprestar Livro: registra empréstimo; se indisponível, adiciona usuário à fila de reservas.
- `3` Devolver Livro: devolve e, se houver fila, passa automaticamente para o próximo usuário.
- `4` Mostrar Ranking: exibe livros ordenados por popularidade (contador de atendimentos).
- `5` Mostrar Histórico: lista registros do histórico com título, usuário e data.
- `6` Sair: encerra a aplicação.

## Estruturas de dados utilizadas
- Max-heap para o ranking de popularidade (`MaxHeapRanking`).
- Lista encadeada simples para o histórico (`HistoricoEmprestimos`).
- Fila (lista) por livro para reservas (`GerenciadorReservas`).

## Autores
- Dafni Milla - https://github.com/DafniMilla

- Karlos Marques - https://github.com/karlosmarques

- Maria Giuliana - https://github.com/Giuliana-05

- Pedro Heleno - https://github.com/StayInPluton

- Vicente Campos - https://github.com/Vicente-Campos



