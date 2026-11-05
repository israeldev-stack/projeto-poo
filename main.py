from medicamento import Medicamentos
from registros import RegistroAdministracao
from cuidador import Cuidador
from paciente import Paciente

# Listas que guardam os cadastros enquanto o programa roda (só em memória)
cuidadores = []
pacientes = []
medicamentos = []
registros = []


# ---------- Funções auxiliares de entrada ----------

def ler_texto(mensagem):
    """Lê um texto obrigatório: repete até o usuário digitar algo."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("  -> Esse campo não pode ficar vazio. Tente de novo.")


def ler_opcional(mensagem):
    """Lê um texto que pode ficar vazio."""
    return input(mensagem).strip()


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Lê um número inteiro, validando e repetindo em caso de erro."""
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("  -> Digite um número inteiro válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  -> O valor deve ser no mínimo {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  -> O valor deve ser no máximo {maximo}.")
            continue
        return valor


def escolher_da_lista(lista, titulo):
    """Mostra os itens numerados e devolve o objeto escolhido.
    Retorna None se a lista estiver vazia."""
    if not lista:
        return None
    print(f"\n{titulo}")
    for indice, item in enumerate(lista, start=1):
        print(f"  {indice} - {item.nome}")
    escolha = ler_inteiro("Escolha o número: ", minimo=1, maximo=len(lista))
    return lista[escolha - 1]


# ---------- Ações do menu ----------

def cadastrar_cuidador():
    print("\n--- Cadastrar cuidador ---")
    nome = ler_texto("Nome: ")
    idade = ler_inteiro("Idade: ", minimo=0, maximo=120)
    telefone = ler_texto("Telefone: ")
    especialidade = ler_texto("Especialidade: ")
    cuidadores.append(Cuidador(nome, idade, telefone, especialidade))
    print(f"Cuidador '{nome}' cadastrado com sucesso!")


def cadastrar_paciente():
    print("\n--- Cadastrar paciente ---")
    nome = ler_texto("Nome: ")
    idade = ler_inteiro("Idade: ", minimo=0, maximo=120)
    telefone = ler_texto("Telefone: ")
    contato = ler_texto("Contato de emergência: ")
    pacientes.append(Paciente(nome, idade, telefone, contato))
    print(f"Paciente '{nome}' cadastrado com sucesso!")


def cadastrar_medicamento():
    print("\n--- Cadastrar medicamento ---")
    nome = ler_texto("Nome: ")
    dose = ler_texto("Dose (ex: 500mg): ")
    horarios_texto = ler_texto("Horários separados por vírgula (ex: 08:00, 12:00): ")
    horarios = [h.strip() for h in horarios_texto.split(",") if h.strip()]
    estoque = ler_inteiro("Estoque (unidades): ", minimo=0)
    data_inicio = ler_texto("Data de início (ex: 2026-11-05): ")
    data_fim = ler_opcional("Data de fim (opcional, Enter para pular): ")
    medicamentos.append(
        Medicamentos(nome, dose, horarios, estoque, data_inicio, data_fim or None)
    )
    print(f"Medicamento '{nome}' cadastrado com sucesso!")


def registrar_administracao():
    print("\n--- Registrar administração de dose ---")
    if not medicamentos:
        print("Cadastre ao menos um medicamento antes (opção 3).")
        return
    if not cuidadores:
        print("Cadastre ao menos um cuidador antes (opção 1).")
        return

    medicamento = escolher_da_lista(medicamentos, "Medicamentos disponíveis:")
    cuidador = escolher_da_lista(cuidadores, "Cuidadores disponíveis:")

    print("\nStatus da dose:")
    print("  1 - Realizada")
    print("  2 - Não realizada")
    print("  3 - Pendente")
    opcao_status = ler_inteiro("Escolha o status: ", minimo=1, maximo=3)
    status = {1: "Realizada", 2: "Não realizada", 3: "Pendente"}[opcao_status]

    observacao = ler_opcional("Observação (opcional, Enter para pular): ")

    registro = RegistroAdministracao(medicamento, cuidador, status, observacao)
    registros.append(registro)
    print("\nRegistro criado:")
    print(registro.apresentar())

    if status == "Realizada":
        medicamento.baixar_estoque()
        print(f"Estoque de '{medicamento.nome}' agora: {medicamento.consultar_estoque()}")
        if medicamento.verificar_estoque_baixo():
            print("  ATENÇÃO: estoque baixo (5 unidades ou menos)!")


def listar(lista, titulo):
    print(f"\n===== {titulo} =====")
    if not lista:
        print("(nenhum cadastro ainda)")
        return
    for item in lista:
        print(item.apresentar())


def consultar_estoque():
    print("\n--- Consultar estoque ---")
    if not medicamentos:
        print("Nenhum medicamento cadastrado ainda (opção 3).")
        return
    medicamento = escolher_da_lista(medicamentos, "Medicamentos disponíveis:")
    print(f"\nMedicamento: {medicamento.nome}")
    print(f"Estoque atual: {medicamento.consultar_estoque()}")
    print(f"Estoque baixo? {medicamento.verificar_estoque_baixo()}")


# ---------- Menu principal ----------

def mostrar_menu():
    print("\n========= BEM LEMBRADO! =========")
    print("1 - Cadastrar cuidador")
    print("2 - Cadastrar paciente")
    print("3 - Cadastrar medicamento")
    print("4 - Registrar administração de dose")
    print("5 - Listar cuidadores")
    print("6 - Listar pacientes")
    print("7 - Listar medicamentos")
    print("8 - Listar registros de administração")
    print("9 - Consultar estoque de um medicamento")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opção: ", minimo=0, maximo=9)

        if opcao == 1:
            cadastrar_cuidador()
        elif opcao == 2:
            cadastrar_paciente()
        elif opcao == 3:
            cadastrar_medicamento()
        elif opcao == 4:
            registrar_administracao()
        elif opcao == 5:
            listar(cuidadores, "CUIDADORES")
        elif opcao == 6:
            listar(pacientes, "PACIENTES")
        elif opcao == 7:
            listar(medicamentos, "MEDICAMENTOS")
        elif opcao == 8:
            listar(registros, "REGISTROS DE ADMINISTRAÇÃO")
        elif opcao == 9:
            consultar_estoque()
        elif opcao == 0:
            print("\nAté logo! Cuide bem de quem você cuida. ")
            break


if __name__ == "__main__":
    main()
