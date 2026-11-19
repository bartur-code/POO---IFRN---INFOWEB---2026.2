from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__()

    def inserir(self, obj: Cliente) -> None:
        self._abrir()
        sql = "INSERT INTO cliente (nome, email, fone, senha) VALUES (?, ?, ?, ?)"
        self._execute(sql, (obj.nome, obj.email, obj.fone, obj.senha))
        self._fechar()

    def listar(self) -> list:
        self._abrir()
        sql = "SELECT id, nome, email, fone, senha FROM cliente"
        cursor = self._execute(sql)
        rows = cursor.fetchall()
        self._fechar()
        return [Cliente(r[0], r[1], r[2], r[3], r[4]) for r in rows]

    def listar_id(self, id: int) -> Cliente:
        self._abrir()
        sql = "SELECT id, nome, email, fone, senha FROM cliente WHERE id = ?"
        cursor = self._execute(sql, (id,))
        row = cursor.fetchone()
        self._fechar()
        if row:
            return Cliente(row[0], row[1], row[2], row[3], row[4])
        return None

    def atualizar(self, obj: Cliente) -> None:
        self._abrir()
        sql = "UPDATE cliente SET nome = ?, email = ?, fone = ?, senha = ? WHERE id = ?"
        self._execute(sql, (obj.nome, obj.email, obj.fone, obj.senha, obj.id))
        self._fechar()

    def excluir(self, id: int) -> None:
        self._abrir()
        sql = "DELETE FROM cliente WHERE id = ?"
        self._execute(sql, (id,))
        self._fechar()