import math

class Circulo:
    def __init__(self, raio=0):
        self.__raio = raio  # atributo privado

    # Método para definir o raio
    def set_raio(self, raio):
        if raio >= 0:
            self.__raio = raio
        else:
            print("O raio não pode ser negativo.")

    # Método para obter o raio
    def get_raio(self):
        return self.__raio

    # Método para calcular a área
    def calcular_area(self):
        return math.pi * (self.__raio ** 2)

    # Método para calcular a circunferência
    def calcular_circunferencia(self):
        return 2 * math.pi * self.__raio
    # Criando um objeto da classe Circulo
c = Circulo()

# Definindo o raio
raio = float(input("Digite o valor do raio: "))
c.set_raio(raio)

# Exibindo os resultados
print(f"Raio: {c.get_raio()}")
print(f"Área: {c.calcular_area():.2f}")
print(f"Circunferência: {c.calcular_circunferencia():.2f}")