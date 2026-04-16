class ContaBancaria:
    def __init__(self, titular="", numero="", saldo=0.0):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo

    # Métodos de acesso
    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    # Operações bancárias
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor

# Criando conta
conta = ContaBancaria()

# Entrada de dados
titular = input("Digite o nome do titular: ")
numero = input("Digite o número da conta: ")

conta.set_titular(titular)
conta.set_numero(numero)

# Depósito
valor_dep = float(input("Digite o valor para depósito: "))
conta.depositar(valor_dep)

# Saque
valor_saq = float(input("Digite o valor para saque: "))
conta.sacar(valor_saq)

# Exibindo dados
print("\n--- Dados da Conta ---")
print(f"Titular: {conta.get_titular()}")
print(f"Número: {conta.get_numero()}")
print(f"Saldo atual: R$ {conta.get_saldo():.2f}")

