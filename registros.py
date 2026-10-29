from datetime import datetime
import cuidador
import medicamento
class RegistroAdministracao ():
    def __init__(
        self,
        medicamento,
        cuidador,
        status,
        observacao=""
    ):
        status_permitidos = {
            "Realizada",
            "Não realizada",
            "Pendente"
        }

        if status not in status_permitidos:
            raise ValueError("Status de administração inválido.")

        self.medicamento = medicamento
        self.cuidador = cuidador
        self.data_hora = datetime.now()
        self.__status = status
        self.observacao = observacao

    def consultar_status(self):
        return self.__status

    def apresentar(self):
        return (
            f"Medicamento: {self.medicamento.nome} | "
            f"Cuidador: {self.cuidador.nome} | "
            f"Data/hora: {self.data_hora:%d/%m/%Y %H:%M} | "
            f"Status: {self.__status} | "
            f"Observação: {self.observacao or 'Nenhuma'}"
        )

