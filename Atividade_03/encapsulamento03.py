class Viagem:
    def __init__(self, distancia=0.0, horas=0, minutos=0):
        self.__distancia = distancia
        self.__horas = horas
        self.__minutos = minutos

    # Métodos de acesso (get/set)
    def set_distancia(self, distancia):
        if distancia >= 0:
            self.__distancia = distancia
        else:
            print("Distância inválida.")

    def get_distancia(self):
        return self.__distancia

    def set_tempo(self, horas, minutos):
        if horas >= 0 and 0 <= minutos < 60:
            self.__horas = horas
            self.__minutos = minutos
        else:
            print("Tempo inválido.")

    def get_tempo(self):
        return self.__horas, self.__minutos

    # Método de cálculo
    def calcular_velocidade(self):
        tempo_total_horas = self.__horas + (self.__minutos / 60)

        if tempo_total_horas == 0:
            return 0

        return self.__distancia / tempo_total_horas

# Criando objeto
v = Viagem()

# Entrada de dados
distancia = float(input("Digite a distância (km): "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

# Definindo valores
v.set_distancia(distancia)
v.set_tempo(horas, minutos)

# Exibindo resultados
h, m = v.get_tempo()

print(f"\nDistância: {v.get_distancia()} km")
print(f"Tempo: {h}h {m}min")
print(f"Velocidade média: {v.calcular_velocidade():.2f} km/h")