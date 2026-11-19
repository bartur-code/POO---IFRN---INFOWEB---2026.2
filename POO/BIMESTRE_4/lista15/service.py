# service/service.py
from datetime import datetime
from models.cliente import Cliente
from models.profissional import Profissional
from models.servico import Servico
from models.horario import Horario
from models.atendimento import Atendimento

from dao_sql.cliente_dao import ClienteDAO
from dao_sql.profissional_dao import ProfissionalDAO
from dao_sql.servico_dao import ServicoDAO
from dao_sql.horario_dao import HorarioDAO
from dao_sql.atendimento_dao import AtendimentoDAO

class Service:
    # --- CLIENTE ---
    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str, senha: str) -> None:
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar() -> list:
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id: int) -> Cliente:
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str, senha: str) -> None:
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id: int) -> None:
        ClienteDAO().excluir(id)

    # --- PROFISSIONAL ---
    @staticmethod
    def profissional_inserir(nome: str, especialidade: str, conselho: str, email: str, senha: str) -> None:
        obj = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_listar() -> list:
        return ProfissionalDAO().listar()

    @staticmethod
    def profissional_listar_id(id: int) -> Profissional:
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_atualizar(id: int, nome: str, especialidade: str, conselho: str, email: str, senha: str) -> None:
        obj = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id: int) -> None:
        ProfissionalDAO().excluir(id)

    # --- SERVICO ---
    @staticmethod
    def servico_inserir(descricao: str, valor: float) -> None:
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar() -> list:
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id: int) -> Servico:
        return ServicoDAO().listar_id(id)

    @staticmethod
    def servico_atualizar(id: int, descricao: str, valor: float) -> None:
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id: int) -> None:
        ServicoDAO().excluir(id)

    # --- HORARIO ---
    @staticmethod
    def horario_inserir(data: datetime, confirmado: bool = False, id_cliente: int = None, id_servico: int = None, id_profissional: int = None) -> None:
        obj = Horario(0, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO().inserir(obj)

    @staticmethod
    def horario_listar() -> list:
        return HorarioDAO().listar()

    @staticmethod
    def horario_listar_id(id: int) -> Horario:
        return HorarioDAO().listar_id(id)

    @staticmethod
    def horario_atualizar(id: int, data: datetime, confirmado: bool, id_cliente: int, id_servico: int, id_profissional: int) -> None:
        obj = Horario(id, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO().atualizar(obj)

    @staticmethod
    def horario_excluir(id: int) -> None:
        HorarioDAO().excluir(id)

    # --- ATENDIMENTO ---
    @staticmethod
    def atendimento_inserir(data: datetime, descricao: str, id_cliente: int, id_profissional: int) -> None:
        obj = Atendimento(0, data, descricao, id_cliente, id_profissional)
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_listar() -> list:
        return AtendimentoDAO().listar()

    @staticmethod
    def atendimento_listar_id(id: int) -> Atendimento:
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_atualizar(id: int, data: datetime, descricao: str, id_cliente: int, id_profissional: int) -> None:
        obj = Atendimento(id, data, descricao, id_cliente, id_profissional)
        AtendimentoDAO().atualizar(obj)

    @staticmethod
    def atendimento_excluir(id: int) -> None:
        AtendimentoDAO().excluir(id)