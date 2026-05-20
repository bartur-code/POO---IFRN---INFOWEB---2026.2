class Time:
    def __init__(self, id, nome, estado): # faz o set de todos os  atributos
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, id):
        if id < 0: raise ValueError("O id precisa ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome < 0: raise ValueError("Não pode ser vazio")
        self.__nome = nome
    def set_estado(self, estado):
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",\
                  "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",\
                   "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        if estado not in estados: raise ValueError("Estado inválido") 
        self.__estado = estado
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def __str__(self): # faz o get de todos os atributos
        return f"{self.__id} - {self.__nome} - {self.__estado}"
        #return f"{self.get_id()} - {self.get_nome()} - {self.get_estado()}" 

class UI:
    times = [] # lista de times
    def main():
        op = 0
        while op != 9:
            op = UI.menu() # lê a opção do usuário
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
    def menu():
        print("1- Inserir time, 2- Listar times, 3- Atualizar time, 4- Excluir time, 9- Sair")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir_time(cls):      # C - reate
        id = int(input("Informe o id: ")) # lê os dados do time
        nome = input("Informe o nome: ")
        estado = input("Informe o estado: ")
        x = Time(id, nome, estado) # cria o objeto time
        cls.times.append(x) # insere o time na lista
    @classmethod
    def listar_time(cls):       # R - ead
        for x in cls.times: print() # percorre a lista e mostra cada time
    @classmethod
    def atualizar_time(cls):    # U - pdate
        pass
    @classmethod
    def excluir_time(cls):      # D - elete
        pass
UI.main()