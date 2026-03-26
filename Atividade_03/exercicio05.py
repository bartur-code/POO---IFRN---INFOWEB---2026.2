class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def calcular_densidade(self):
        return self.populacao / self.area


# Entrada de dados
nome = input("Digite o nome do país: ")
populacao = int(input("Digite sua população: "))
area = float(input("Digite a área em km2: "))

# Criar objeto
pais = Pais(nome, populacao, area)

# Calcular densidade
densidade = pais.calcular_densidade()

# Mostrar resultado formatado
print(f"A densidade demográfica do {pais.nome} é de {densidade:.2f} hab/km2")