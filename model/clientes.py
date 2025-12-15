class Clientes:
    def __init__(self, id, nome, cpf, email, renda):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._renda = renda
    
    def to_string(self):
        return f"ID: {self._id} | Nome: {self._nome} | CPF: {self._cpf} | Email: {self._email} | Renda: R$ {self._renda:.2f}"