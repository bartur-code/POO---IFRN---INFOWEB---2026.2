from datetime import datetime
from dao_sql.dao import DAO
from models.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__()

    def inserir(self, obj: Atendimento) -> None:
        self._abrir()
        sql = "INSERT INTO atendimento (data, descricao, id_cliente, id_profissional) VALUES (?, ?, ?, ?)"
        data_str = obj.data.strftime("%Y-%m-%d %H:%M:%S")
        self._execute(sql, (data_str, obj.descricao, obj.id_cliente, obj.id_profissional))
        self._fechar()

    def listar(self) -> list:
        self._abrir()
        sql = "SELECT id, data, descricao, id_cliente, id_profissional FROM atendimento"
        cursor = self._execute(sql)
        rows = cursor.fetchall()
        self._fechar()
        return [
            Atendimento(r[0], datetime.strptime(r[1], "%Y-%m-%d %H:%M:%S"), r[2], r[3], r[4])
            for r in rows
        ]

    def listar_id(self, id: int) -> Atendimento:
        self._abrir()
        sql = "SELECT id, data, descricao, id_cliente, id_profissional FROM atendimento WHERE id = ?"
        cursor = self._execute(sql, (id,))
        row = cursor.fetchone()
        self._fechar()
        if row:
            return Atendimento(row[0], datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"), row[2], row[3], row[4])
        return None

    def atualizar(self, obj: Atendimento) -> None:
        self._abrir()
        sql = "UPDATE atendimento SET data = ?, descricao = ?, id_cliente = ?, id_profissional = ? WHERE id = ?"
        data_str = obj.data.strftime("%Y-%m-%d %H:%M:%S")
        self._execute(sql, (data_str, obj.descricao, obj.id_cliente, obj.id_profissional, obj.id))
        self._fechar()

    def excluir(self, id: int) -> None:
        self._abrir()
        sql = "DELETE FROM atendimento WHERE id = ?"
        self._execute(sql, (id,))
        self._fechar()