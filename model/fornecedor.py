class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, email):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._email = email
    
    def to_string(self):
        return f"ID: {self._id} | Razão Social: {self._razao_social} | Nome Fantasia: {self._nome_fantasia} | CNPJ: {self._cnpj} | Email: {self._email}"