class Produto:
    def __init__(self, id, nome, valor, estoque):
        self._id = id
        self._nome = nome
        self._valor = valor
        self._estoque = estoque

    @property
    def _valor_em_estoque(self):
        return self._valor * self._estoque
    
    def to_string(self):
        return f"ID: {self._id} | Nome: {self._nome} | Valor: R$ {self._valor:.2f} | Estoque: {self._estoque} | Valor em Estoque: R$ {self._valor_em_estoque:.2f}"