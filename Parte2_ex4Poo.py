class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, usuario, livro):
        if livro.disponivel:
            livro.disponivel = False
            usuario.livros.append(livro)
            print(f"{usuario.nome} pegou '{livro.titulo}'")
        else:
            print("Livro indisponível")

    def devolver_livro(self, usuario, livro):
        if livro in usuario.livros:
            livro.disponivel = True
            usuario.livros.remove(livro)
            print(f"{usuario.nome} devolveu '{livro.titulo}'")
        else:
            print("Usuário não está com esse livro")

    def consultar_disponibilidade(self, livro):
        if livro.disponivel:
            print("Livro disponível")
        else:
            print("Livro emprestado")


biblioteca = Biblioteca()

livro1 = Livro("1984", "George Orwell")
usuario1 = Usuario("Ana")

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_usuario(usuario1)

biblioteca.emprestar_livro(usuario1, livro1)
biblioteca.consultar_disponibilidade(livro1)

biblioteca.devolver_livro(usuario1, livro1)
biblioteca.consultar_disponibilidade(livro1)