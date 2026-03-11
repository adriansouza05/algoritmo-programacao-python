#Implementar uma classe Aluno com validação para nota e frequência

class Aluno:
    def __init__(self, nome:str, ra:str):
        self.nome = nome
        self.ra = ra
        self.notas = Notas(self)
        self.frequencia = Frequencia()

    def __str__(self):
        return f"{self.nome}:{self.ra}"
    
class Notas:
    def __init__(self, aluno):
        self._aluno = aluno
        self._notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
        else:
            raise ValueError("Nota inválida!")

    def calcular_media(self):
        return sum(self._notas) / len(self._notas) if len(self._notas) > 0 else 0
    
    def __str__(self):
        return f"{self._aluno} -> Notas: {self._notas}"
    
class Frequencia:
    def __init__(self):
        self._presencas = 0
        self._total_aulas = 0

    def registrar_aula(self, presente):
        self._total_aulas += 1
        if presente:
            self._presencas += 1

    def calcular_frequencia(self):
        if self._total_aulas == 0:
            return 0
        return (self._presencas / self._total_aulas) * 100


# Criando aluno
aluno1 = Aluno("Ana", "123")

# Notas
aluno1.notas.adicionar_nota(8)
aluno1.notas.adicionar_nota(6)

print("Média:", aluno1.notas.calcular_media())

# Frequência
aluno1.frequencia.registrar_aula(True)
aluno1.frequencia.registrar_aula(True)
aluno1.frequencia.registrar_aula(False)

print("Frequência:", aluno1.frequencia.calcular_frequencia())