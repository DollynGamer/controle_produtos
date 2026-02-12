from model.dao.base_dao import Base_DAO
from model.categoria import Categoria

class Categoria_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, cat: Categoria):
        sql = "insert into categoria (nome) values (%s)"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (cat._nome))
        cat._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return cat
    
    def get_all(self):
        sql = "select id, nome from categoria"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = [Categoria(id, nome) for (id, nome) in cursor]
        cursor.close()
        conn.close()
        return res
    
    def get_by_id(self, id):
        sql = "select id, nome from categoria where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        res = Categoria(row[0], row[1]) if row else None
        cursor.close()
        conn.close()
        return res
    
    def delete(self, id):
        sql = "delete from categoria where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        afetados = cursor.rowcount
        cursor.close()
        conn.close
        return afetados > 0
    
    def update(self, cat:Categoria):
        sql = "update categoria set nome = %s where id = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (cat._nome, cat._id))
        conn.commit()
        afetados = cursor.rowcount
        cursor.close()
        conn.close()
        return afetados > 0
    
    def vincular_produto(self, id_p, id_c):
        sql = "insert into produto_categoria (id_produto, id_categoria) values (%s, %s)"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_p, id_c))
        conn.commit()
        cursor.close()
        conn.close()

    def get_vinculos_detalhados_produto(self):
        sql = """select p.id, p.nome, c.nome
                from produto p
                join produto_categoria pc on p.id = pc.id_produto
                join categoria c on c.id = pc.id_categoria
                order by p.nome"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res
    
    def sincronizar_vinculos_produto(self, id_produto, lista_ids_categoria):
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("delete from produto_categoria where id_produto = %s", (id_produto,))

            if lista_ids_categoria:
                sql = "insert into produto_categoria (id_produto, id_categoria) values (%s, %s)"
                for id_cat in lista_ids_categoria:
                    cursor.execute(sql, (id_produto, id_cat))
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    
    def get_categorias_por_produto(self, id_produto):
        sql = "select id_categoria from produto_categoria where id_produto = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_produto,))
        ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return ids
    
    def vincular_fornecedor(self, id_f, id_c):
        sql = "insert into fornecedor_categoria (id_fornecedor, id_categoria) values (%s, %s)"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_f, id_c))
        conn.commit()
        cursor.close()
        conn.close()

    def get_vinculos_detalhados_fornecedor(self):
        sql = """select f.id, f.nome, c.nome
                from fornecedor f
                join fornecedor_categoria fc on f.id = fc.id_fornecedor
                join categoria c on c.id = fc.id_categoria
                order by f.nome_fantasia"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res
    
    def sincronizar_vinculos_fornecedor(self, id_fornecedor, lista_ids_categoria):
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("delete from fornecedor_categoria where id_fornecedor = %s", (id_fornecedor,))

            if lista_ids_categoria:
                sql = "insert into fornecedor_categoria (id_fornecedor, id_categoria) values (%s, %s)"
                for id_cat in lista_ids_categoria:
                    cursor.execute(sql, (id_fornecedor, id_cat))
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
    
    def get_categorias_por_fornecedor(self, id_fornecedor):
        sql = "select id_categoria from fornecedor_categoria where id_fornecedor = %s"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_fornecedor,))
        ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return ids