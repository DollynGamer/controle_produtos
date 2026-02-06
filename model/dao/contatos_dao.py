from model.dao.base_dao import Base_DAO
from model.contatos import Contatos

class Contatos_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)
    
    def save(self, con:Contatos):
        sql_con = """insert into contatos (id_fornecedor, nome, telefone, email, tipo) values (%s, %s, %s, %s, %s)"""

        conn = self._get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql_con, (con._id_fornecedor, con._nome, con._telefone, con._email, con._tipo))
            con._id = cursor.lastrowid

            conn.commit()
            return con
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    
    def get_all(self):
        sql = """select c.id, c.id_fornecedor, c.nome, c.telefone, c.email, c.tipo, f.nome_fantasia
                from contatos c
                inner join fornecedor f on c.id_fornecedor = f.id
                order by c.id_fornecedor desc"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        contatos = []
        for (id, id_fornecedor, nome, telefone, email, tipo, nome_f) in cursor:
            contatos.append(Contatos(id, id_fornecedor, nome, telefone, email, tipo, nome_f))
        cursor.close()
        conn.close()
        return contatos
    
    def get_by_id(self, id):
        sql = """select id, id_fornecedor, nome, telefone, email, tipo from contatos where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        contatos = None
        if row:
            id, id_fornecedor, nome, telefone, email, tipo = row
            contatos = Contatos(id, id_fornecedor, nome, telefone, email, tipo)
        cursor.close()
        conn.close()
        return contatos
    
    def delete(self, id):
        sql = """delete from contatos where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, con:Contatos):
        sql = """update contatos set id_fornecedor = %s, nome = %s, telefone = %s, email = %s, tipo = %s where id = %s"""
        values = (con._id_fornecedor, con._nome, con._telefone, con._email, con._tipo)
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0