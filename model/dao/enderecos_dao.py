from model.enderecos import Enderecos
from model.dao.base_dao import Base_DAO

class Enderecos_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, end:Enderecos):
        sql_end = """insert into enderecos (id_cliente, cep, logradouro, cidade, tipo) values (%s, %s, %s, %s, %s)"""

        conn = self._get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql_end, (end._id_cliente, end._cep, end._logradouro, end._cidade, end._tipo))
            end._id = cursor.lastrowid

            conn.commit()
            return end
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    
    def get_all(self):
        sql = """select e.id, e.id_cliente, e.cep, e.logradouro, e.cidade, e.tipo, c.nome
                from enderecos e
                inner join clientes c on e.id_cliente = c.id
                order by e.id_cliente desc"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        enderecos = []
        for (id, id_cliente, cep, logradouro, cidade, tipo, nome_c) in cursor:
            enderecos.append(Enderecos(id, id_cliente, cep, logradouro, cidade, tipo, nome_c))
        cursor.close()
        conn.close()
        return enderecos
    
    def get_by_id(self, id):
        sql = """select id, id_cliente, cep, logradouro, cidade, tipo from enderecos where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        enderecos = None
        if row:
            id, id_cliente, cep, logradouro, cidade, tipo = row
            enderecos = Enderecos(id, id_cliente, cep, logradouro, cidade, tipo)
        cursor.close()
        conn.close()
        return enderecos
    
    def delete(self, id):
        sql = """delete from enderecos where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, end: Enderecos):
        sql = """update enderecos set id_cliente = %s, cep = %s, logradouro = %s, cidade = %s, tipo = %s where id = %s"""
        values = (end._id_cliente, end._cep, end._logradouro, end._cidade, end._tipo)
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0