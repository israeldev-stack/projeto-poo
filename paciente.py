from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self,nome, idade, telefone, contato_de_emergencia):
        super().__init__(nome, idade, telefone)
        self.contato_de_emergencia = contato_de_emergencia

    def apresentar(self):
        return (
            super().apresentar() +
            f"Contato de Emergência:{self.contato_de_emergencia}|"
        )