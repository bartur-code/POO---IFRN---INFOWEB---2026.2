from datetime import datetime
from dao_sql.dao import DAO
from models.horario import Horario

class HorarioDAO(DAO):
    def __init__(self):
        super().__init__()

    def inserir(self, obj: Horario) -> None:
        self._abrir()
        sql = "INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional) VALUES (?, ?, ?, ?, ?)"
        data_str = obj.data.strftime("%Y-%m-%d %H:%M:%S")
        self._execute(sql, (data_str, int(obj.confirmado), obj.id_cliente, obj.id_servico, obj.id_profissional))
        self._fechar()

    def listar(self) -> list:
        self._abrir()
        sql = "SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario"
        cursor = self._execute(sql)
        rows = cursor.fetchall()
        self._fechar()
        return [
            Horario(r[0], datetime.strptime(r[1], "%Y-%m-%d %H:%M:%S"), bool(r[2]), r[3], r[4], r[5])
            for r in rows
        ]

    def listar_id(self, id: int) -> Horario:
        self._abrir()
        sql = "SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario WHERE id = ?"
        cursor = self._execute(sql, (id,))
        row = cursor.fetchone()
        self._fechar()
        if row:
            return Horario(row[0], datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"), bool(row[2]), row[3], row[4], row[5])
        return None

    def atualizar(self, obj: Horario) -> None:
        self._abrir()
        sql = "UPDATE horario SET data = ?, confirmado = ?, id_cliente = ?, id_servico = ?, id_profissional = ? WHERE id = ?"
        data_str = obj.data.strftime("%Y-%m-%d %H:%M:%S")
        self._execute(sql, (data_str, int(obj.confirmado), obj.id_cliente, obj.id_servico, obj.id_profissional, obj.id))
        self._fechar()

    def excluir(self, id: int) -> None:
        self._abrir()
        sql = "DELETE FROM horario WHERE id = ?"
        self._execute(sql, (id,))
        self._fechar()