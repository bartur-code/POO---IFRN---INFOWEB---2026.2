class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.email} - {self.fone}"

class ContatoUI:
    contatos = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
    @staticmethod
    def menu()
        print("1 - Inserir 2 - Listar 3 - Atualizar 4 - Excluir 5 - Pesquisar 6 - Fim")
        return int(input("Escolha uma opção: "))
    def inserir()

ContatoUI.main()



