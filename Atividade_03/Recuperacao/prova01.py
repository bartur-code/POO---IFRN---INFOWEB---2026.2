class Produto: # - tipo de variável
    def __init__(self): # - método mágico
        self.__id = 1
        self.__nome = "Sem nome"
        self.__preco = 0.0
        self.__avaliacao = 1
    def set_id(self, id):
        if id < 0: raise ValueError("Id tem que ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("nome não pode ser vazio")
        self.__nome = nome
    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço tem que ser positivo")
        self.__preco = preco
    def set_avaliacao(self, avaliacao):
        if avaliacao < 0: raise ValueError("Avaliação não pode ser negativa")
        self.__avaliacao = avaliacao
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_avaliacao(self):
        return self.__avaliacao

a = Produto() # - nome da classe seguido de "()" chama o __init__

print(a.get_id())
print(a.get_nome())
print(a.get_preco())
print(a.get_avaliacao())