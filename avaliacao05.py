class Cliente:
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

class ClienteDAO:
    def __init__(self):
        self.profissionais = []
        self.proximo_id = 1

    def inserir(self, cliente):
        cliente.set_id(self.proximo_id)
        self.clientes.append(cliente)
        self.proximo_id += 1

    def listar(self):
        return self.clientes

    def buscar_por_id(self, id):
        for cliente in self.clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    def atualizar(self, cliente):
        for i in range(len(self.clientes)):
            if self.clientes[i].get_id() == cliente.get_id():
                self.clientes[i] = cliente
                return True

        return False

    def excluir(self, id):
        cliente = self.buscar_por_id(id)

        if cliente is not None:
            self.clientes.remove(cliente)
            return True

        return False

class Service:
    def __init__(self):
        self.cliente_dao = ClienteDAO()

    def inserir_cliente(self, nome, email, fone, especialidade):
        cliente = Cliente(
            0,
            nome,
            email,
            fone,
            especialidade
        )

        self.cliente_dao.inserir(cliente)

    def listar_clientes(self):
        return self.cliente_dao.listar()

    def buscar_cliente(self, id):
        return self.cliente_dao.buscar_por_id(id)

    def atualizar_cliente(self, id, nome, email, fone, especialidade):
        cliente = Cliente(
            id,
            nome,
            email,
            fone,
            especialidade
        )

        return self.cliente_dao.atualizar(cliente)

    def excluir_cliente(self, id):
        return self.cliente_dao.excluir(id)

class ManterClienteUI:
    def __init__(self, service):
        self.service = service

    def cadastrar(self):
        print("\n--- CADASTRO DE CLIENTE ---")

        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        especialidade = input("Especialidade: ")

        self.service.inserir_cliente(
            nome,
            email,
            fone,
            especialidade
        )

        print("Cliente cadastrado com sucesso!")

    def listar(self):
        print("\n--- CLIENTES CADASTRADOS ---")

        clientes = self.service.listar_clientes()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(
                "ID:", cliente.get_id(),
                "| Nome:", cliente.get_nome(),
                "| E-mail:", cliente.get_email(),
                "| Especialidade:", cliente.get_especialidade()
            )

    def excluir(self):
        print("\n--- EXCLUIR Cliente ---")

        id = int(input("Digite o ID do cliente: "))

        if self.service.excluir_cliente(id):
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

class IndexUI:
    def __init__(self):
        self.service = Service()
        self.cliente_ui = ManterClienteUI(self.service)

    def iniciar(self):
        while True:
            print("\n===== SISTEMA DE AGENDAMENTO =====")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Excluir cliente")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cliente_ui.cadastrar()

            elif opcao == "2":
                self.cliente_ui.listar()

            elif opcao == "3":
                self.cliente_ui.excluir()

            elif opcao == "0":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida.")


sistema = IndexUI()
sistema.iniciar()