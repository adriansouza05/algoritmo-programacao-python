class Aluno:
    def __init__(self, nome, ra):
        self._nome = nome
        self._ra = ra

    def __str__(self):
        return f"{self._ra}:{self._nome}" 


class Notas:
    def __init__(self, aluno):
        self._aluno = aluno
        self._valores = []

    def calcular_media(self):
        return sum(self._valores) / len(self._valores) if len(self._valores) > 0 else 0

    def __str__(self):
        return f"{self._aluno} -> Notas: {self._valores}"


class Turma:
    def __init__(self, disciplina):
        self._disciplina = disciplina
        self._notas = []

    def adicionar_aluno(self, aluno):
        if list(filter(lambda nota: nota._aluno._ra == aluno._ra, self._notas)) != []:
            raise ValueError(f"Aluno {aluno} já existe na turma.")
        self._notas.append(Notas(aluno))

    def registrar_nota(self, aluno, nota):
        def detecta(nota):
            return nota._aluno._ra == aluno._ra

        nota_aluno = list(filter(detecta, self._notas))
        if len(nota_aluno) > 0: 
            nota_aluno[0]._valores.append(nota)
        else:
            raise ValueError(f"Aluno {aluno} não existe na turma")

    def calcular_media(self, aluno):
        als = list(filter(lambda nota: nota._aluno._ra == aluno._ra, self._notas))
        if len(als) > 0:
            return als[0].calcular_media()
        else:
            raise ValueError(f"Aluno {aluno} não existe na turma")

    def __str__(self):
        return "\n".join([f"{nota}" for nota in self._notas])


def main():
    al1 = Aluno("Joao", 123)
    al2 = Aluno("Maria", 456)
    al3 = Aluno("Carlos", 789)

    turma = Turma("ALP")
    turma.adicionar_aluno(al1)
    turma.adicionar_aluno(al3)

    turma.registrar_nota(al1, 10)
    turma.registrar_nota(al1, 1)
    turma.registrar_nota(al3, 5)

    print(turma)


if __name__ == "__main__":
    main()
