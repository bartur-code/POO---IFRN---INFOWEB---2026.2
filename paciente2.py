from datetime import datetime


class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    # Getters
    def getNome(self):
        return self.__nome

    def getCPF(self):
        return self.__cpf

    def getTelefone(self):
        return self.__telefone

    def getNascimento(self):
        return self.__nascimento

    # Setters
    def setNome(self, nome):
        self.__nome = nome

    def setCPF(self, cpf):
        self.__cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def Idade(self):
        hoje = datetime.now().date()

        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month

        if hoje.day < self.__nascimento.day:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

def ToString(self):
        return (
            f"Nome: {self.__nome}\n"
            f"CPF: {self.__cpf}\n"
            f"Telefone: {self.__telefone}\n"
            f"Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"
        )
x = Paciente("Nome", "123", "456", datetime(2009, 10, 29))
print(x)
print(x.Idade())