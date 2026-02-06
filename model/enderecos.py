class Enderecos:
    def __init__(self, id, id_cliente, cep, logradouro, cidade, tipo, nome_c):
        self._id = id
        self._id_cliente = id_cliente
        self._cep = cep
        self._logradouro = logradouro
        self._cidade = cidade
        self._tipo = tipo
        self._nome_c = nome_c

    def to_string(self):
        return f"ID: {self._id} | Cliente: {self._id_cliente} | CEP: {self._cep} | Logradouro: {self._logradouro} | Cidade: {self._cidade} | Tipo: {self._tipo}"