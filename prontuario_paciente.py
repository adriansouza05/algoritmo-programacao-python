from datetime import datetime
from copy import deepcopy


class ProntuarioPaciente:
    def __init__(self, paciente_id: str, nome: str):
        self._paciente_id = paciente_id
        self._nome = nome
        self.__historico = []  # privado (name mangling)

    @property
    def paciente_id(self) -> str:
        return self._paciente_id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def historico(self):
        # Retorna cópia para evitar alteração externa
        return tuple(deepcopy(self.__historico))

    def registrar_evento(self, profissional: str, descricao: str) -> None:
        if not descricao or len(descricao.strip()) < 5:
            raise ValueError("Descrição do evento é inválida.")
        self.__historico.append(
            {
                "data": datetime.now().isoformat(timespec="minutes"),
                "profissional": profissional.strip(),
                "descricao": descricao.strip(),
            }
        )

    def atualizar_evento(self, indice: int, nova_descricao: str) -> None:
        if indice < 0 or indice >= len(self.__historico):
            raise IndexError("Índice de evento inválido.")
        if not nova_descricao or len(nova_descricao.strip()) < 5:
            raise ValueError("Nova descrição inválida.")
        self.__historico[indice]["descricao"] = nova_descricao.strip()

    @historico.deleter
    def historico(self) -> None:
        # Exemplo de regra de negócio: nunca apagar prontuário completo
        raise PermissionError("Remoção total do histórico não é permitida.")
