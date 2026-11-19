# models/cliente.py
class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


# models/profissional.py
class Profissional:
    def __init__(self, id: int, nome: str, especialidade: str, conselho: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"{self.id} - {self.nome} ({self.especialidade} - {self.conselho})"


# models/servico.py
class Servico:
    def __init__(self, id: int, descricao: str, valor: float):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.valor:.2f}"


# models/horario.py
from datetime import datetime

class Horario:
    def __init__(self, id: int, data: datetime, confirmado: bool = False, id_cliente: int = None, id_servico: int = None, id_profissional: int = None):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_servico = id_servico
        self.id_profissional = id_profissional

    def __str__(self):
        status = "Confirmado" if self.confirmado else "Disponível"
        return f"{self.id} - {self.data.strftime('%d/%m/%Y %H:%M')} - {status}"


# models/atendimento.py
from datetime import datetime

class Atendimento:
    def __init__(self, id: int, data: datetime, descricao: str, id_cliente: int, id_profissional: int):
        self.id = id
        self.data = data
        self.descricao = descricao
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional

    def __str__(self):
        return f"{self.id} - {self.data.strftime('%d/%m/%Y %H:%M')} - {self.descricao}"