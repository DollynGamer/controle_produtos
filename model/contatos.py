class Contatos:
    def __init__(self, id, id_fornecedor, nome, telefone, email, tipo, nome_f):
        self._id = id
        self._id_fornecedor = id_fornecedor
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._tipo = tipo
        self._nome_f = nome_f

    def to_string(self):
        return f"ID: {self._id} | Fornecedor: {self._id_fornecedor} | Nome: {self._nome} | Telefone: {self._telefone} | Email: {self._email} | Tipo: {self._tipo}"