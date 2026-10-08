from datetime import datetime


class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone


class Profissional:
    def __init__(self, id, nome, email, especialidade):
        self.id = id
        self.nome = nome
        self.email = email
        self.especialidade = especialidade


class Servico:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor


class Horario:
    def __init__(self, id, data, confirmado, id_cliente, id_profissional):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional


class AtendimentoItem:
    def __init__(self, id, id_atendimento, id_servico, quantidade):
        self.id = id
        self.id_atendimento = id_atendimento
        self.id_servico = id_servico
        self.quantidade = quantidade


class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude,
                 avaliacao, prescricao, id_cliente, id_profissional):
        self.id = id
        self.data = data
        self.queixa_principal = queixa_principal
        self.historico_saude = historico_saude
        self.avaliacao = avaliacao
        self.prescricao = prescricao
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.itens = []
        self.total = 0
        self.pago = False

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self, servicos):
        self.total = 0

        for item in self.itens:
            for servico in servicos:
                if servico.id == item.id_servico:
                    self.total += servico.valor * item.quantidade

        return self.total


class Pagamento:
    def __init__(self, id, id_atendimento, valor, data):
        self.id = id
        self.id_atendimento = id_atendimento
        self.valor = valor
        self.data = data


# Dados para testar o sistema

clientes = [
    Cliente(1, "João", "joao@email.com", "99999-1111"),
    Cliente(2, "Maria", "maria@email.com", "99999-2222"),
    Cliente(3, "Pedro", "pedro@email.com", "99999-3333")
]

profissionais = [
    Profissional(1, "Dr. Carlos", "carlos@email.com", "Clínico Geral"),
    Profissional(2, "Dra. Ana", "ana@email.com", "Dermatologia")
]

servicos = [
    Servico(1, "Consulta", 100.00),
    Servico(2, "Exame", 80.00),
    Servico(3, "Procedimento", 150.00)
]

atendimentos = []


def registrar_atendimento():
    print("\n--- Registrar Atendimento ---")

    id_atendimento = len(atendimentos) + 1

    print("Clientes:")
    for cliente in clientes:
        print(cliente.id, "-", cliente.nome)

    id_cliente = int(input("ID do cliente: "))

    print("\nProfissionais:")
    for profissional in profissionais:
        print(profissional.id, "-", profissional.nome)

    id_profissional = int(input("ID do profissional: "))

    data = input("Data do atendimento (dd/mm/aaaa): ")
    data = datetime.strptime(data, "%d/%m/%Y")

    queixa = input("Queixa principal: ")
    historico = input("Histórico de saúde: ")
    avaliacao = input("Avaliação clínica: ")
    prescricao = input("Prescrição: ")

    atendimento = Atendimento(
        id_atendimento,
        data,
        queixa,
        historico,
        avaliacao,
        prescricao,
        id_cliente,
        id_profissional
    )

    print("\nServiços:")
    for servico in servicos:
        print(servico.id, "-", servico.descricao, "- R$", servico.valor)

    while True:
        id_servico = int(input("ID do serviço (0 para terminar): "))

        if id_servico == 0:
            break

        quantidade = int(input("Quantidade: "))

        item = AtendimentoItem(
            len(atendimento.itens) + 1,
            atendimento.id,
            id_servico,
            quantidade
        )

        atendimento.adicionar_item(item)

    atendimento.calcular_total(servicos)
    atendimentos.append(atendimento)

    print("\nAtendimento registrado!")
    print("Total: R$", atendimento.total)


def listar_atendimentos(lista):
    if len(lista) == 0:
        print("\nNenhum atendimento encontrado.")
        return

    print("\n--- Atendimentos ---")

    for atendimento in lista:
        cliente_nome = "Não encontrado"
        profissional_nome = "Não encontrado"

        for cliente in clientes:
            if cliente.id == atendimento.id_cliente:
                cliente_nome = cliente.nome

        for profissional in profissionais:
            if profissional.id == atendimento.id_profissional:
                profissional_nome = profissional.nome

        status = "Pago" if atendimento.pago else "Pendente"

        print(
            "ID:", atendimento.id,
            "| Cliente:", cliente_nome,
            "| Profissional:", profissional_nome,
            "| Data:", atendimento.data.strftime("%d/%m/%Y"),
            "| Total: R$", atendimento.total,
            "| Status:", status
        )


def filtrar_atendimentos():
    print("\n--- Filtrar Atendimentos ---")
    print("1 - Por cliente")
    print("2 - Por profissional")
    print("3 - Pagos")
    print("4 - Pendentes")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        id_cliente = int(input("ID do cliente: "))
        resultado = []

        for atendimento in atendimentos:
            if atendimento.id_cliente == id_cliente:
                resultado.append(atendimento)

    elif opcao == 2:
        id_profissional = int(input("ID do profissional: "))
        resultado = []

        for atendimento in atendimentos:
            if atendimento.id_profissional == id_profissional:
                resultado.append(atendimento)

    elif opcao == 3:
        resultado = []

        for atendimento in atendimentos:
            if atendimento.pago:
                resultado.append(atendimento)

    elif opcao == 4:
        resultado = []

        for atendimento in atendimentos:
            if not atendimento.pago:
                resultado.append(atendimento)

    else:
        print("Opção inválida.")
        return

    listar_atendimentos(resultado)


def ordenar_atendimentos():
    print("\n--- Ordenar Atendimentos ---")
    print("1 - Por data")
    print("2 - Por valor")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = sorted(atendimentos, key=lambda x: x.data)

    elif opcao == 2:
        resultado = sorted(atendimentos, key=lambda x: x.total)

    else:
        print("Opção inválida.")
        return

    listar_atendimentos(resultado)


def pagar_atendimento():
    print("\n--- Pagar Atendimento ---")

    if len(atendimentos) == 0:
        print("Não existem atendimentos.")
        return

    listar_atendimentos(atendimentos)

    id_atendimento = int(input("ID do atendimento que deseja pagar: "))

    for atendimento in atendimentos:
        if atendimento.id == id_atendimento:

            if atendimento.pago:
                print("Esse atendimento já está pago.")
                return

            pagamento = Pagamento(
                1,
                atendimento.id,
                atendimento.total,
                datetime.now()
            )

            atendimento.pago = True

            print("\nPagamento realizado!")
            print("Valor pago: R$", pagamento.valor)
            return

    print("Atendimento não encontrado.")


def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DE AGENDAMENTO")
        print("==============================")
        print("1 - Registrar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Filtrar atendimentos")
        print("4 - Ordenar atendimentos")
        print("5 - Pagar atendimento")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            registrar_atendimento()

        elif opcao == 2:
            listar_atendimentos(atendimentos)

        elif opcao == 3:
            filtrar_atendimentos()

        elif opcao == 4:
            ordenar_atendimentos()

        elif opcao == 5:
            pagar_atendimento()
