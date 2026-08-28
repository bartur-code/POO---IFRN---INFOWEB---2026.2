from datetime import datetime


class Profissional:
    def __init__(self, id, nome, email, especialidade):
        self.id = id
        self.nome = nome
        self.email = email
        self.especialidade = especialidade


class Horario:
    def __init__(
        self,
        id,
        data,
        confirmado,
        id_cliente,
        id_servico,
        id_profissional
    ):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_servico = id_servico
        self.id_profissional = id_profissional

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_confirmado(self):
        return self.confirmado

    def get_id_cliente(self):
        return self.id_cliente

    def get_id_servico(self):
        return self.id_servico

    def get_id_profissional(self):
        return self.id_profissional

    def set_data(self, data):
        self.data = data

    def set_confirmado(self, confirmado):
        self.confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        self.id_servico = id_servico

    def set_id_profissional(self, id_profissional):
        self.id_profissional = id_profissional


class HorarioDAO:
    def __init__(self):
        self.horarios = []
        self.proximo_id = 1

    def inserir(self, horario):
        horario.id = self.proximo_id
        self.horarios.append(horario)
        self.proximo_id += 1

    def listar(self):
        return self.horarios

    def buscar_por_id(self, id):
        for horario in self.horarios:
            if horario.get_id() == id:
                return horario

        return None


class Service:
    def __init__(self):
        self.horario_dao = HorarioDAO()

        # Profissionais cadastrados
        self.profissionais = [
            Profissional(
                1,
                "João",
                "joao@gmail.com",
                "Eletricista"
            ),
            Profissional(
                2,
                "Maria",
                "maria@gmail.com",
                "Encanadora"
            )
        ]

    def listar_profissionais(self):
        return self.profissionais

    def buscar_profissional(self, id):
        for profissional in self.profissionais:
            if profissional.id == id:
                return profissional

        return None

    def inserir_horario(
        self,
        data,
        confirmado,
        id_cliente,
        id_servico,
        id_profissional
    ):
        profissional = self.buscar_profissional(id_profissional)

        if profissional is None:
            return False

        horario = Horario(
            0,
            data,
            confirmado,
            id_cliente,
            id_servico,
            id_profissional
        )

        self.horario_dao.inserir(horario)

        return True

    def listar_horarios(self):
        return self.horario_dao.listar()


class ManterHorarioUI:
    def __init__(self, service):
        self.service = service

    def cadastrar(self):
        print("\n--- CADASTRO DE HORÁRIO ---")

        data_texto = input(
            "Data e hora (dd/mm/aaaa HH:MM): "
        )

        data = datetime.strptime(
            data_texto,
            "%d/%m/%Y %H:%M"
        )

        id_cliente = int(
            input("ID do cliente: ")
        )

        id_servico = int(
            input("ID do serviço: ")
        )

        print("\nProfissionais disponíveis:")

        profissionais = self.service.listar_profissionais()

        for profissional in profissionais:
            print(
                profissional.id,
                "-",
                profissional.nome,
                "(" + profissional.especialidade + ")"
            )

        id_profissional = int(
            input("ID do profissional: ")
        )

        confirmado = False

        resultado = self.service.inserir_horario(
            data,
            confirmado,
            id_cliente,
            id_servico,
            id_profissional
        )

        if resultado:
            print("Horário cadastrado com sucesso!")
        else:
            print("Profissional não encontrado.")

    def listar(self):
        print("\n--- HORÁRIOS ---")

        horarios = self.service.listar_horarios()

        if len(horarios) == 0:
            print("Nenhum horário cadastrado.")
            return

        for horario in horarios:

            profissional = self.service.buscar_profissional(
                horario.get_id_profissional()
            )

            print("\nID do horário:", horario.get_id())
            print("Data:", horario.get_data().strftime(
                "%d/%m/%Y %H:%M"
            ))
            print("Cliente:", horario.get_id_cliente())
            print("Serviço:", horario.get_id_servico())
            print(
                "Profissional:",
                profissional.nome
            )
            print(
                "Confirmado:",
                horario.get_confirmado()
            )


# Programa principal
service = Service()
horario_ui = ManterHorarioUI(service)

while True:

    print("\n===== HORÁRIOS =====")
    print("1 - Cadastrar horário")
    print("2 - Listar horários")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        horario_ui.cadastrar()

    elif opcao == "2":
        horario_ui.listar()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")