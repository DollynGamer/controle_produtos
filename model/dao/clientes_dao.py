from model.clientes import Clientes

class Clientes_DAO:
    def __init__(self):
        self._clientes = []
        self._id_counter = 1
    
    def save(self, cliente:Clientes):
        cliente._id = self._id_counter
        self._id_counter += 1
        self._clientes.append(cliente)
        return cliente
    
    def get_all(self):
        return self._clientes
    
    def get_by_id(self, id):
        for cliente in self._clientes:
            if cliente._id == id:
                    return cliente
        return None
    
    def delete(self, id):
        cliente = self.get_by_id(id)
        if cliente:
            self._clientes.remove(cliente)
            return True
        return False
    
    def update(self, cliente_atualizado:Clientes):
        cliente = self.get_by_id(cliente_atualizado._id)
        if cliente:
            cliente._nome = cliente_atualizado._nome
            cliente._cpf = cliente_atualizado._cpf
            cliente._email = cliente_atualizado._email
            cliente._renda = cliente_atualizado._renda
            return True
        return False
    