class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def apresentar(self):
        return (
            f"Nome:{self.nome} |" 
            f"Idade:{self.idade} |" 
            f"Telefone:{self.telefone}|"
        )

class Paciente(Pessoa):
    def __init__(self,nome, idade, telefone, contato_de_emergencia):
        super().__init__(nome, idade, telefone)
        self.contato_de_emergencia = contato_de_emergencia

    def apresentar(self):
        return (
            super().apresentar() +
            f"Contato de Emergência:{self.contato_de_emergencia}|"
        )

class Cuidador(Pessoa):
    def __init__(self, nome, idade, telefone, especialidade):
        super().__init__(nome, idade, telefone)
        self.especialidade = especialidade

    def apresentar(self):
        return (
            super().apresentar() +
            f"Especialidade:{self.especialidade}|"
        )

Cuidador1 = Cuidador("Israel", 49, "(51)98186-4241", "Enfermagem")
print(Cuidador1.apresentar())
Paciente1 = Paciente("João", 39, "(51)98186-4241", "Maria")
print(Paciente1.apresentar())

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

medicamento1 = Medicamentos("Dipirona", "500mg", "08:00, 12:00, 18:00", 10, "2024-06-01")
print(medicamento1.apresentar())

print("Estoque atual:", medicamento1.consultar_estoque())
print("Estoque baixo?", medicamento1.verificar_estoque_baixo())