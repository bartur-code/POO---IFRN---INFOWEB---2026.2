class EntradaCinema:
    def __init__(self, dia="", hora=0):
        self.__dia = dia.lower()
        self.__hora = hora

    # Métodos de acesso
    def set_dia(self, dia):
        self.__dia = dia.lower()

    def get_dia(self):
        return self.__dia

    def set_hora(self, hora):
        if 0 <= hora <= 23:
            self.__hora = hora
        else:
            print("Hora inválida.")

    def get_hora(self):
        return self.__hora

    # Método interno para calcular valor base
    def __valor_base(self):
        if self.__dia in ["segunda", "terça", "terca", "quinta"]:
            return 16.0
        elif self.__dia == "quarta":
            return 8.0
        elif self.__dia in ["sexta", "sábado", "sabado", "domingo"]:
            return 20.0
        else:
            print("Dia inválido.")
            return 0

    # Inteira
    def calcular_inteira(self):
        base = self.__valor_base()

        # quarta já é meia para todos
        if self.__dia == "quarta":
            return base

        # acréscimo horário
        if 17 <= self.__hora <= 23:
            base *= 1.5

        return base

    # Meia entrada
    def calcular_meia(self):
        return self.calcular_inteira() / 2

entrada = EntradaCinema()

# Entrada de dados
dia = input("Digite o dia da sessão: ")
hora = int(input("Digite a hora (0-23): "))

entrada.set_dia(dia)
entrada.set_hora(hora)

# Resultados
print("\n--- Valores ---")
print(f"Dia: {entrada.get_dia()}")
print(f"Hora: {entrada.get_hora()}h")
print(f"Inteira: R$ {entrada.calcular_inteira():.2f}")
print(f"Meia: R$ {entrada.calcular_meia():.2f}")