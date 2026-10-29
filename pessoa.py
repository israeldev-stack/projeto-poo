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