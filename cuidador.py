from pessoa import Pessoa

class Cuidador(Pessoa):
    def __init__(self, nome, idade, telefone, especialidade):
        super().__init__(nome, idade, telefone)
        self.especialidade = especialidade

    def apresentar(self):
        return (
            super().apresentar() +
            f"Especialidade:{self.especialidade}|"
        )
