class Movimentacao:
    def __init__(self, id, id_produto, tipo, quantidade, data_movimentacao=None, nome_produto=""):
        self._id = id
        self._id_produto = id_produto
        self._tipo = tipo
        self._quantidade = quantidade
        self._data_movimentacao = data_movimentacao
        self._nome_produto = nome_produto

    def to_string(self):
        return f"ID: {self._id} | Produto: {self._nome_produto} | Tipo: {self._tipo} | Qtd: {self._quantidade} | Data: {self._data_movimentacao}"