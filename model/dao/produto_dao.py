from model.produto import Produto

class Produto_DAO:
    def __init__(self):
        self._produtos = []
        self._id_counter = 1
    
    def save(self, produto:Produto):
        produto._id = self._id_counter
        self._id_counter += 1
        self._produtos.append(produto)
        return produto
    
    def get_all(self):
        return self._produtos
    
    def get_by_id(self, id):
        for produto in self._produtos:
            if produto._id == id:
                    return produto
        return None
    
    def delete(self, id):
         produto = self.get_by_id(id)
         if produto:
              self._produtos.remove(produto)
              return True
         return False