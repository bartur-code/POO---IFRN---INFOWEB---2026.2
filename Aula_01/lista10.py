class Profissional:
    def __init__(self, id, nome, email, especialidade):
        self.id = id
        self.nome = nome
        self.email = email
        self.especialidade = especialidade

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_especialidade(self):
        return self.especialidade

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade


class ProfissionalDAO:
    def __init__(self):
        self.profissionais = []
        self.proximo_id = 1

    def inserir(self, profissional):
        profissional.set_id(self.proximo_id)
        self.profissionais.append(profissional)
        self.proximo_id += 1

    def listar(self):
        return self.profissionais

    def buscar_por_id(self, id):
        for profissional in self.profissionais:
            if profissional.get_id() == id:
                return profissional

        return None

    def atualizar(self, profissional):
        for i in range(len(self.profissionais)):
            if self.profissionais[i].get_id() == profissional.get_id():
                self.profissionais[i] = profissional
                return True

        return False

    def excluir(self, id):
        profissional = self.buscar_por_id(id)

        if profissional is not None:
            self.profissionais.remove(profissional)
            return True

        return False


class Service:
    def __init__(self):
        self.profissional_dao = ProfissionalDAO()

    def inserir_profissional(self, nome, email, especialidade):
        profissional = Profissional(
            0,
            nome,
            email,
            especialidade
        )

        self.profissional_dao.inserir(profissional)

    def listar_profissionais(self):
        return self.profissional_dao.listar()

    def buscar_profissional(self, id):
        return self.profissional_dao.buscar_por_id(id)

    def atualizar_profissional(self, id, nome, email, especialidade):
        profissional = Profissional(
            id,
            nome,
            email,
            especialidade
        )

        return self.profissional_dao.atualizar(profissional)

    def excluir_profissional(self, id):
        return self.profissional_dao.excluir(id)


class ManterProfissionalUI:
    def __init__(self, service):
        self.service = service

    def cadastrar(self):
        print("\n--- CADASTRO DE PROFISSIONAL ---")

        nome = input("Nome: ")
        email = input("E-mail: ")
        especialidade = input("Especialidade: ")

        self.service.inserir_profissional(
            nome,
            email,
            especialidade
        )

        print("Profissional cadastrado com sucesso!")

    def listar(self):
        print("\n--- PROFISSIONAIS CADASTRADOS ---")

        profissionais = self.service.listar_profissionais()

        if len(profissionais) == 0:
            print("Nenhum profissional cadastrado.")
            return

        for profissional in profissionais:
            print(
                "ID:", profissional.get_id(),
                "| Nome:", profissional.get_nome(),
                "| E-mail:", profissional.get_email(),
                "| Especialidade:", profissional.get_especialidade()
            )

    def excluir(self):
        print("\n--- EXCLUIR PROFISSIONAL ---")

        id = int(input("Digite o ID do profissional: "))

        if self.service.excluir_profissional(id):
            print("Profissional excluído com sucesso!")
        else:
            print("Profissional não encontrado.")


class IndexUI:
    def __init__(self):
        self.service = Service()
        self.profissional_ui = ManterProfissionalUI(self.service)

    def iniciar(self):
        while True:
            print("\n===== SISTEMA DE AGENDAMENTO =====")
            print("1 - Cadastrar profissional")
            print("2 - Listar profissionais")
            print("3 - Excluir profissional")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.profissional_ui.cadastrar()

            elif opcao == "2":
                self.profissional_ui.listar()

            elif opcao == "3":
                self.profissional_ui.excluir()

            elif opcao == "0":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida.")


# Programa principal
sistema = IndexUI()
sistema.iniciar()