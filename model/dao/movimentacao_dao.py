from model.movimentacao import Movimentacao
from model.dao.base_dao import Base_DAO

class Movimentacao_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, mov:Movimentacao):
        sql_mov = """insert into movimentacao (id_produto, tipo, quantidade) values (%s, %s, %s)"""

        operador = "+" if mov._tipo == "Entrada" else "-"
        sql_prod = f"update produto set estoque = estoque {operador} %s where id = %s"

        conn = self._get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql_mov, (mov._id_produto, mov._tipo, mov._quantidade))
            mov._id = cursor.lastrowid

            cursor.execute(sql_prod, (mov._quantidade, mov._id_produto))

            conn.commit()
            return mov
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    def get_all(self):
        sql = """select m.id, m.id_produto, m.tipo, m.quantidade, m.data_movimentacao, p.nome
                from movimentacao m
                inner join produto p on m.id_produto = p.id
                order by m.data_movimentacao desc"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        movimentacoes = []
        for (id, id_prod, tipo, qtd, data, nome_p) in cursor:
            movimentacoes.append(Movimentacao(id, id_prod, tipo, qtd, data, nome_p))
        cursor.close()
        conn.close()
        return movimentacoes
    
    def get_by_id(self, id):
        sql = """select id, id_produto, tipo, quantidade, data_movimentacao from movimentacao where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        movimentacao = None
        if row:
            id, id_prod, tipo, qtd, data = row
            movimentacao = Movimentacao(id, id_prod, tipo, qtd, data)
        cursor.close()
        conn.close()
        return movimentacao
    
    def delete(self, id):
        sql = """delete from movimentacao where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, mov: Movimentacao):
        sql = """update movimentacao set id_produto = %s, tipo = %s, quantidade = %s where id = %s"""
        values = (mov._id_produto, mov._tipo, mov._quantidade, mov._id)
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0