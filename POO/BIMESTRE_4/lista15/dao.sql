import sqlite3
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, nome_bd: str = "agenda.db"):
        self._conn = None
        self._nome_bd = nome_bd
        self._criar_tabelas()

    def _abrir(self) -> None:
        self._conn = sqlite3.connect(self._nome_bd)

    def _fechar(self) -> None:
        if self._conn:
            self._conn.close()
            self._conn = None

    def _execute(self, sql: str, params: tuple = ()) -> sqlite3.Cursor:
        cursor = self._conn.cursor()
        cursor.execute(sql, params)
        self._conn.commit()
        return cursor

    def _criar_tabelas(self) -> None:
        self._abrir()
        self._execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        self._execute("""
            CREATE TABLE IF NOT EXISTS profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especialidade TEXT NOT NULL,
                conselho TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        self._execute("""
            CREATE TABLE IF NOT EXISTS servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
            )
        """)
        self._execute("""
            CREATE TABLE IF NOT EXISTS horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                confirmado INTEGER NOT NULL,
                id_cliente INTEGER,
                id_servico INTEGER,
                id_profissional INTEGER,
                FOREIGN KEY (id_cliente) REFERENCES cliente(id),
                FOREIGN KEY (id_servico) REFERENCES servico(id),
                FOREIGN KEY (id_profissional) REFERENCES profissional(id)
            )
        """)
        self._execute("""
            CREATE TABLE IF NOT EXISTS atendimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                descricao TEXT NOT NULL,
                id_cliente INTEGER NOT NULL,
                id_profissional INTEGER NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES cliente(id),
                FOREIGN KEY (id_profissional) REFERENCES profissional(id)
            )
        """)
        self._fechar()

    @abstractmethod
    def inserir(self, obj: object) -> None:
        pass

    @abstractmethod
    def listar(self) -> list:
        pass

    @abstractmethod
    def listar_id(self, id: int) -> object:
        pass

    @abstractmethod
    def atualizar(self, obj: object) -> None:
        pass

    @abstractmethod
    def excluir(self, id: int) -> None:
        pass