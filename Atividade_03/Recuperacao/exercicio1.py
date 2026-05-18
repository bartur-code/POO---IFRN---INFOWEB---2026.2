# Usuário
# class UI = user interface > Prints e Inputs
#Entidade

# OBS.: O diagrama não muda independente da linguagem
class Frete:
    def __init__(self, d : float, p : float): # construtor (todos os dados) # retorna a variável "Frete"
        self.set_distancia(d) # Outro método é só copiar e colar o "if" e o "self.__variavel"
        self.set_peso(p) # Outro método é só copiar e colar o "if" e o "self.__variavel"
        #if d < 0: raise ValueError("A distância não pode ser negativa")
        #self.__distancia = d
        # if p < 0: raise ValueError("O peso não pode ser negativo")
        #def set_peso(self, p : float):
    def set_distancia(self, d : float): # no diagrmama tem o "void" que não retorna nenhum valor
        if d < 0: raise ValueError("A distância não pode ser negativa") # a variável é testada, e caso não for validada, um erro é gerado
        self.__distancia = d # se não der erro, a variável testada é guardada
    def set_peso(self, p : float): # no diagrmama tem o "void" que não retorna nenhum valor
        if p < 0: raise ValueError("O peso não pode ser negativo") # a variável é testada, e caso não for validada, um erro é gerado
        self.__peso = p # se não der erro, a variável testada é guardada
    def get_distancia(self): # não tem "void", logo tem que ter o "return" em baixo
        return self.__distancia
    def get_peso(self): # não tem "void", logo tem que ter o "return" em baixo
        return self.__peso
    def calc_frete(self): # não tem "void", logo tem que ter o "return" em baixo
        return 0.01 * self.__distancia * self.__peso
    def __str__(self): # mostrar os dados (todos) # não tem "void", logo tem que ter o "return" em baixo
        # retornar vários valores pra texto: return f"{self.__distancia} - {self.__peso}"
        return str(self.__distancia) + " - " + str(self.__peso) # junção de valores (numéricos) para forma de textos
