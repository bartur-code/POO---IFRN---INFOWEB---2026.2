class Endereço:
    def __init__(self, id, nome, email, fone, especialidade):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.especialidade = especialidade

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_fone(self):
        return self.fone

    def get_especialidade(self):
        return self.especialidade

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_fone(self, fone):
        self.fone = fone

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

class EnderecoDAO:
    def __init__(self):
        self.endereços = []
        self.proximo_id = 1

    def inserir(self, endereco):
        endereco.set_id(self.proximo_id)
        self.endereco.append(endereco)
        self.proximo_id += 1

    def listar(self):
        return self.endereco

    def buscar_por_id(self, id):
        for endereco in self.endereco:
            if endereco.get_id() == id:
                return endereco
        return None

    def atualizar(self, endereco):
        for i in range(len(self.endereco)):
            if self.endereco[i].get_id() == endereco.get_id():
                self.endereco[i] = endereco
                return True

        return False

    def excluir(self, id):
        endereco = self.buscar_por_id(id)

        if endereco is not None:
            self.enderecos.remove(endereco)
            return True

        return False

class Service:
    def __init__(self):
        self.endereco_dao = EnderecoDAO()

    def inserir_cliente(self, nome, email, fone, especialidade):
        endereco = endereco(
            0,
            nome,
            email,
            fone,
            especialidade
        )

        self.endereco_dao.inserir(endereco)

    def listar_endereco(self):
        return self.endereco_dao.listar()

    def buscar_endereco(self, id):
        return self.endereco_dao.buscar_por_id(id)

    def atualizar_endereco(self, id, nome, email, fone, especialidade):
        endereco = endereco(
            id,
            nome,
            email,
            fone,
            especialidade
        )

        return self.endereco_dao.atualizar(endereco)

    def excluir_endereco(self, id):
        return self.endereco_dao.excluir(id)

class ManterEnderecoUI:
    def __init__(self, service):
        self.service = service

    def cadastrar(self):
        print("\n--- CADASTRO DE ENDEREÇO ---")

        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        especialidade = input("Especialidade: ")

        self.service.inserir_endereco(
            nome,
            email,
            fone,
            especialidade
        )

        print("Endereço cadastrado com sucesso!")

    def listar(self):
        print("\n--- ENDEREÇOS CADASTRADOS ---")

        endereco = self.service.listar_enderecos()

        if len(endereco) == 0:
            print("Nenhum endereco cadastrado.")
            return

        for endereco in endereco:
            print(
                "ID:", endereco.get_id(),
                "| Nome:", endereco.get_nome(),
                "| E-mail:", endereco.get_email(),
                "| Especialidade:", endereco.get_especialidade()
            )

    def excluir(self):
        print("\n--- EXCLUIR ENDEREÇO ---")

        id = int(input("Digite o ID do Endereço: "))

        if self.service.excluir_endereco(id):
            print("Endereço excluído com sucesso!")
        else:
            print("Endereço não encontrado.")

class IndexUI:
    def __init__(self):
        self.service = Service()
        self.endereco_ui = ManterEnderecoUI(self.service)

    def iniciar(self):
        while True:
            print("\n===== SISTEMA DE AGENDAMENTO =====")
            print("1 - Cadastrar endereço")
            print("2 - Listar endereços")
            print("3 - Excluir endereço")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.endereco_ui.cadastrar()

            elif opcao == "2":
                self.endereco_ui.listar()

            elif opcao == "3":
                self.endereco_ui.excluir()

            elif opcao == "0":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida.")


sistema = IndexUI()
sistema.iniciar()