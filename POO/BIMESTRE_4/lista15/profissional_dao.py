from dao_sql.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__()

    def inserir(self, obj: Profissional) -> None:
        self._abrir()
        sql = "INSERT INTO profissional (nome, especialidade, conselho, email, senha) VALUES (?, ?, ?, ?, ?)"
        self._execute(sql, (obj.nome, obj.especialidade, obj.conselho, obj.email, obj.senha))
        self._fechar()

    def listar(self) -> list:
        self._abrir()
        sql = "SELECT id, nome, especialidade, conselho, email, senha FROM profissional"
        cursor = self._execute(sql)
        rows = cursor.fetchall()
        self._fechar()
        return [Profissional(r[0], r[1], r[2], r[3], r[4], r[5]) for r in rows]

    def listar_id(self, id: int) -> Profissional:
        self._abrir()
        sql = "SELECT id, nome, especialidade, conselho, email, senha FROM profissional WHERE id = ?"
        cursor = self._execute(sql, (id,))
        row = cursor.fetchone()
        self._fechar()
        if row:
            return Profissional(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def atualizar(self, obj: Profissional) -> None:
        self._abrir()
        sql = "UPDATE profissional SET nome = ?, especialidade = ?, conselho = ?, email = ?, senha = ? WHERE id = ?"
        self._execute(sql, (obj.nome, obj.especialidade, obj.conselho, obj.email, obj.senha, obj.id))
        self._fechar()

    def excluir(self, id: int) -> None:
        self._abrir()
        sql = "DELETE FROM profissional WHERE id = ?"
        self._execute(sql, (id,))
        self._fechar()