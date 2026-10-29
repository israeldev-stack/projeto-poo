from pessoa import Pessoa
from medicamento import Medicamentos
from registros import RegistroAdministracao
from cuidador import Cuidador
from paciente import Paciente

# Criando os objetos
cuidador1 = Cuidador(
    "Israel",
    49,
    "(51) 98186-4241",
    "Enfermagem"
)

paciente1 = Paciente(
    "João",
    39,
    "(51) 98186-4241",
    "Maria"
)

medicamento1 = Medicamentos(
    "Dipirona",
    "500mg",
    ["08:00", "12:00", "18:00"],
    10,
    "2026-10-01"
)


# Apresentando as informações
print("===== CUIDADOR =====")
print(cuidador1.apresentar())

print("\n===== PACIENTE =====")
print(paciente1.apresentar())

print("\n===== MEDICAMENTO =====")
print(medicamento1.apresentar())

print("\nEstoque atual:", medicamento1.consultar_estoque())
print("Estoque baixo?", medicamento1.verificar_estoque_baixo())


# Registrando uma administração
registro1 = RegistroAdministracao(
    medicamento1,
    cuidador1,
    "Realizada",
    "Administração registrada pelo cuidador."
)

print("\n===== REGISTRO DE ADMINISTRAÇÃO =====")
print(registro1.apresentar())

print("\nStatus do registro:", registro1.consultar_status())