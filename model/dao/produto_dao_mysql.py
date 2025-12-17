from model.produto import Produto
from model.dao.base_dao import Base_DAO

class Produto_DAO(Base_DAO):
    def save(self, produto:Produto):
        sql = """insert into produto (nome, valor, estoque)
                values (%s, %s, %s)"""
        
        values = (produto._nome, produto._valor, produto._estoque)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        produto._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return produto
    
    def get_all(self):
        sql = "select id, nome, valor, estoque from produto"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        produtos = []
        for(id, nome, valor, estoque) in cursor:
            produtos.append(Produto(id, nome, valor, estoque))
        cursor.close()
        conn.close()
        return produtos
    
    def get_by_id(self, id):
        sql = """select id, nome, valor, estoque from produto where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        produto = None
        if row:
            id, nome, valor, estoque = row
            produto = Produto(id, nome, valor, estoque)
        cursor.close()
        conn.close()

    def delete(self, id):
        sql = "delete from produto where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, produto_atualizado:Produto):
        sql = """update produto set nome = %s, valor = %s, estoque = %s where id = %s"""
        
        values = (produto_atualizado._nome, produto_atualizado._valor, produto_atualizado._estoque, produto_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0