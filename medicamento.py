class Medicamentos:
    def __init__(
            self,
            nome,
            dose,
            horários,
            estoque,
            data_inicio,
            data_fim = None
    ):
        self.nome = nome
        self.dose = dose
        self.horários = horários
        self.estoque = estoque
        self.data_inicio = data_inicio
        self.data_fim = data_fim


    def consultar_estoque(self):
        return self.estoque
    def verificar_estoque_baixo(self):
        return self.estoque <= 5
    def apresentar(self):
        return (
            f"Medicamento: {self.nome}|"
            f"Dose: {self.dose}|"
            f"Horários: {self.horários}|"
            f"Estoque: {self.estoque}|"
        )