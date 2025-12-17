from model.clientes import Clientes
from model.dao.base_dao import Base_DAO
    
class Clientes_DAO(Base_DAO):
    def save(self, cliente:Clientes):
        sql = """insert into cliente (nome, cpf, email, renda)
                values (%s, %s, %s, %s)"""
        
        values = (cliente._nome, cliente._cpf, cliente._email, cliente._renda)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        cliente._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return cliente
    
    def get_all(self):
        sql = "select id, nome, cpf, email, renda from cliente"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        clientes = []
        for(id, nome, cpf, email, renda) in cursor:
            clientes.append(Clientes(id, nome, cpf, email, renda))
        cursor.close()
        conn.close()
        return clientes
    
    def get_by_id(self, id):
        sql = """select id, nome, cpf, email, renda from cliente where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        cliente = None
        if row:
            id, nome, cpf, email, renda = row
            cliente = Clientes(id, nome, cpf, email, renda)
        cursor.close()
        conn.close()
        return cliente

    def delete(self, id):
        sql = "delete from cliente where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, cliente_atualizado:Clientes):
        sql = """update cliente set nome = %s, cpf = %s, email = %s, renda = %s where id = %s"""
        
        values = (cliente_atualizado._nome, cliente_atualizado._cpf, cliente_atualizado._email, cliente_atualizado._renda, cliente_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0