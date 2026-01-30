from model.fornecedor import Fornecedor
from model.dao.base_dao import Base_DAO

class Fornecedor_DAO(Base_DAO):
    def save(self, fornecedor:Fornecedor):
        sql = """insert into fornecedor (razao_social, nome_fantasia, cnpj, email)
                values (%s, %s, %s, %s)"""
        
        values = (fornecedor._razao_social, fornecedor._nome_fantasia, fornecedor._cnpj, fornecedor._email)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        fornecedor._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return fornecedor
    
    def get_all(self):
        sql = "select id, razao_social, nome_fantasia, cnpj, email from fornecedor"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        fornecedor = []
        for(id, razao_social, nome_fantasia, cnpj, email) in cursor:
            fornecedor.append(Fornecedor(id, razao_social, nome_fantasia, cnpj, email))
        cursor.close()
        conn.close()
        return fornecedor
    
    def get_by_id(self, id):
        sql = """select id, razao_social, nome_fantasia, cnpj, email from fornecedor where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        fornecedor = None
        if row:
            id, razao_social, nome_fantasia, cnpj, email = row
            fornecedor = Fornecedor(id, razao_social, nome_fantasia, cnpj, email)
        cursor.close()
        conn.close()
        return fornecedor

    def delete(self, id):
        sql = "delete from fornecedor where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, fornecedor_atualizado:Fornecedor):
        sql = """update fornecedor set razao_social = %s, nome_fantasia = %s, cnpj = %s, email = %s where id = %s"""
        
        values = (fornecedor_atualizado._razao_social, fornecedor_atualizado._nome_fantasia, fornecedor_atualizado._cnpj, fornecedor_atualizado._email, fornecedor_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0