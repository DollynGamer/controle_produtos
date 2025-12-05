class Produto:
    def __init__(self, id, nome, estoque, valor):
        self._id = id
        self._nome = nome
        self._estoque = estoque
        self._valor = valor

    @property
    def _valor_em_estoque(self):
        return self._valor * self._estoque
    
    def to_string(self):
        return f"ID: {self._id} | Nome: {self._nome} | Valor: R$ {self._valor:.2f} | Estoque: {self._estoque} | Valor em Estoque: R$ {self._valor_em_estoque:.2f}"