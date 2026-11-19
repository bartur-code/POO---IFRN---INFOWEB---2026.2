from dao_sql.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__()

    def inserir(self, obj: Servico) -> None:
        self._abrir()
        sql = "INSERT INTO servico (descricao, valor) VALUES (?, ?)"
        self._execute(sql, (obj.descricao, obj.valor))
        self._fechar()

    def listar(self) -> list:
        self._abrir()
        sql = "SELECT id, descricao, valor FROM servico"
        cursor = self._execute(sql)
        rows = cursor.fetchall()
        self._fechar()
        return [Servico(r[0], r[1], r[2]) for r in rows]

    def listar_id(self, id: int) -> Servico:
        self._abrir()
        sql = "SELECT id, descricao, valor FROM servico WHERE id = ?"
        cursor = self._execute(sql, (id,))
        row = cursor.fetchone()
        self._fechar()
        if row:
            return Servico(row[0], row[1], row[2])
        return None

    def atualizar(self, obj: Servico) -> None:
        self._abrir()
        sql = "UPDATE servico SET descricao = ?, valor = ? WHERE id = ?"
        self._execute(sql, (obj.descricao, obj.valor, obj.id))
        self._fechar()

    def excluir(self, id: int) -> None:
        self._abrir()
        sql = "DELETE FROM servico WHERE id = ?"
        self._execute(sql, (id,))
        self._fechar()