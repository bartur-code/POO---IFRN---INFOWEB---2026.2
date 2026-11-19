from datetime import datetime
from models import Cliente, Profissional, Horario
from service import Service

service = Service()

# --- UI CLIENTES ---
class UIAbrirConta:
    @staticmethod
    def executar():
        print("\n--- [UI] Abrir Conta (Cliente) ---")
        try:
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            
            c = Cliente(id=len(service.clientes) + 1, nome=nome, email=email, senha=senha)[cite: 1]
            service.inserir_cliente(c)[cite: 1]
            print(" Conta criada com sucesso!")
        except Exception as e:
            print(f" Erro ao abrir conta: {e}")[cite: 1]

class UIManterCliente:
    @staticmethod
    def cadastrar():
        try:
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            c = Cliente(id=len(service.clientes) + 1, nome=nome, email=email, senha=senha)[cite: 1]
            service.inserir_cliente(c)[cite: 1]
            print(" Cliente cadastrado com sucesso!")
        except Exception as e:
            print(f" Erro ao cadastrar cliente: {e}")[cite: 1]

    @staticmethod
    def excluir():
        try:
            id_c = int(input("ID do cliente a ser excluído: "))
            service.excluir_cliente(id_c)[cite: 1]
            print(" Cliente excluído com sucesso!")
        except Exception as e:
            print(f" Erro ao excluir cliente: {e}")[cite: 1]

class UIPerfilCliente:
    @staticmethod
    def atualizar(id_cliente: int):
        print("\n--- [UI] Perfil do Cliente - Atualizar ---")
        try:
            nome = input("Novo Nome: ")
            email = input("Novo E-mail: ")
            senha = input("Nova Senha: ")
            c = Cliente(id=id_cliente, nome=nome, email=email, senha=senha)[cite: 1]
            service.atualizar_cliente(c)[cite: 1]
            print(" Perfil atualizado com sucesso!")
        except Exception as e:
            print(f" Erro ao atualizar perfil: {e}")[cite: 1]


# --- UI PROFISSIONAIS ---
class UIManterProfissional:
    @staticmethod
    def cadastrar():
        try:
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            p = Profissional(id=len(service.profissionais) + 1, nome=nome, email=email, senha=senha)[cite: 1]
            service.inserir_profissional(p)[cite: 1]
            print(" Profissional cadastrado com sucesso!")
        except Exception as e:
            print(f" Erro ao cadastrar profissional: {e}")[cite: 1]

    @staticmethod
    def excluir():
        try:
            id_p = int(input("ID do profissional a ser excluído: "))
            service.excluir_profissional(id_p)[cite: 1]
            print(" Profissional excluído com sucesso!")
        except Exception as e:
            print(f" Erro ao excluir profissional: {e}")[cite: 1]

class UIPerfilProfissional:
    @staticmethod
    def atualizar(id_prof: int):
        print("\n--- [UI] Perfil do Profissional - Atualizar ---")
        try:
            nome = input("Novo Nome: ")
            email = input("Novo E-mail: ")
            senha = input("Nova Senha: ")
            p = Profissional(id=id_prof, nome=nome, email=email, senha=senha)[cite: 1]
            service.atualizar_profissional(p)[cite: 1]
            print(" Perfil atualizado com sucesso!")
        except Exception as e:
            print(f" Erro ao atualizar perfil do profissional: {e}")[cite: 1]


# --- UI HORÁRIOS ---
class UIManterHorario:
    @staticmethod
    def cadastrar():
        try:
            id_p = int(input("ID do Profissional: "))
            data_str = input("Data e Hora (dd/mm/aaaa HH:MM): ")
            dt_hora = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            
            h = Horario(id=len(service.horarios) + 1, data_hora=dt_hora, id_profissional=id_p)[cite: 1]
            service.inserir_horario(h)[cite: 1]
            print(" Horário adicionado com sucesso!")
        except Exception as e:
            print(f" Erro ao cadastrar horário: {e}")[cite: 1]

    @staticmethod
    def excluir():
        try:
            id_h = int(input("ID do Horário a ser excluído: "))
            service.excluir_horario(id_h)[cite: 1]
            print(" Horário excluído com sucesso!")
        except Exception as e:
            print(f" Erro ao excluir horário: {e}")[cite: 1]

class UIAbrirAgenda:
    @staticmethod
    def executar(id_prof: int):
        print("\n--- [UI] Abrir Agenda do Profissional ---")
        try:
            data_str = input("Data e Hora para abertura (dd/mm/aaaa HH:MM): ")
            dt_hora = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            
            h = Horario(id=len(service.horarios) + 1, data_hora=dt_hora, id_profissional=id_prof)[cite: 1]
            service.inserir_horario(h)[cite: 1]
            print(" Agenda aberta com sucesso!")
        except Exception as e:
            print(f" Erro ao abrir agenda: {e}")[cite: 1]


# --- BLOCOS DE TESTE/DEMONSTRAÇÃO DA INTERFACE ---
if __name__ == "__main__":
    print("=== TESTANDO TRATAMENTO DE EXCEÇÕES E REGRAS DE NEGÓCIO ===")
    
    # 1. Testando exceção de e-mail 'admin' e campos vazios
    UIAbrirConta.executar()
    
    # 2. Testando exceção de data anterior a 2025
    UIManterHorario.cadastrar()