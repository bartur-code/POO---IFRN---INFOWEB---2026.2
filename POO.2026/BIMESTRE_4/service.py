from models import Cliente, Profissional, Horario
from datetime import datetime

class Service:
    def __init__(self):
        self.clientes = []
        self.profissionais = []
        self.horarios = []

    # --- VALIDAÇÕES AUXILIARES ---
    def __validar_email_unico(self, email: str, id_atual: int = None):
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")[cite: 1]
        
        for c in self.clientes:
            if c.email.lower() == email.lower() and c.id != id_atual:
                raise ValueError(f"O e-mail '{email}' já está em uso por outro cliente.")[cite: 1]

        for p in self.profissionais:
            if p.email.lower() == email.lower() and p.id != id_atual:
                raise ValueError(f"O e-mail '{email}' já está em uso por outro profissional.")[cite: 1]

    # --- OPERAÇÕES CLIENTE ---
    def inserir_cliente(self, cliente: Cliente):
        self.__validar_email_unico(cliente.email)[cite: 1]
        self.clientes.append(cliente)

    def atualizar_cliente(self, cliente: Cliente):
        self.__validar_email_unico(cliente.email, cliente.id)[cite: 1]
        for idx, c in enumerate(self.clientes):
            if c.id == cliente.id:
                self.clientes[idx] = cliente
                return
        raise ValueError("Cliente não encontrado para atualização.")

    def excluir_cliente(self, id_cliente: int):
        for h in self.horarios:
            if h.id_cliente == id_cliente:
                raise ValueError("Não é possível remover clientes que possuem horários agendados.")[cite: 1]
        
        self.clientes = [c for c in self.clientes if c.id != id_cliente]

    # --- OPERAÇÕES PROFISSIONAL ---
    def inserir_profissional(self, profissional: Profissional):
        self.__validar_email_unico(profissional.email)[cite: 1]
        self.profissionais.append(profissional)

    def atualizar_profissional(self, profissional: Profissional):
        self.__validar_email_unico(profissional.email, profissional.id)[cite: 1]
        for idx, p in enumerate(self.profissionais):
            if p.id == profissional.id:
                self.profissionais[idx] = profissional
                return
        raise ValueError("Profissional não encontrado para atualização.")

    def excluir_profissional(self, id_profissional: int):
        for h in self.horarios:
            if h.id_profissional == id_profissional:
                raise ValueError("Não é possível remover profissionais que possuem horários cadastrados.")[cite: 1]
        
        self.profissionais = [p for p in self.profissionais if p.id != id_profissional]

    # --- OPERAÇÕES HORÁRIO ---
    def inserir_horario(self, horario: Horario):
        self.__validar_horario_duplicado(horario)[cite: 1]
        self.horarios.append(horario)

    def atualizar_horario(self, horario: Horario):
        self.__validar_horario_duplicado(horario)[cite: 1]
        for idx, h in enumerate(self.horarios):
            if h.id == horario.id:
                self.horarios[idx] = horario
                return
        raise ValueError("Horário não encontrado para atualização.")

    def excluir_horario(self, id_horario: int):
        for h in self.horarios:
            if h.id == id_horario:
                if h.id_cliente is not None:
                    raise ValueError("Não é possível remover horários que já foram agendados por um cliente.")[cite: 1]
                self.horarios.remove(h)
                return
        raise ValueError("Horário não encontrado.")

    def __validar_horario_duplicado(self, horario: Horario):
        for h in self.horarios:
            if h.id_profissional == horario.id_profissional and h.data_hora == horario.data_hora and h.id != horario.id:
                raise ValueError("Já existe um horário cadastrado para este profissional nesta mesma data e hora.")[cite: 1]

