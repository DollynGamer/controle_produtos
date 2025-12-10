from model.produto import Produto
from model.dao.produto_dao import Produto_DAO

class Produto_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def choice_processor(self, choice):
        try:
            if choice == '1':
                self.add_produto()
            elif choice == '2':
                self.update_produto()
            elif choice == '3':
                self.delete_produto()
            elif choice == '4':
                self.list_produtos()
            elif choice == '5':
                self.list_produto_by_id()
            else:
                self.view.show_error("Opção Inválida")
        except Exception as e:
            self.view.show_error(str(e))

    def add_produto(self):
        try:
            dados_produto = self.view.get_dados_produto()
            produto_novo = Produto(
                id = None,
                nome=dados_produto['nome'],
                valor=dados_produto['valor'],
                estoque=dados_produto['estoque']
            )
            produto_salvo = self.dao.save(produto_novo)
            self.view.show_message(f"Produto adicionado com ID: {produto_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar produto: {str(e)}")

    def update_produto(self):
        try:
            id_produto = self.view.get_id()
            produto_existente = self.dao.get_by_id(id_produto)
            if not produto_existente:
                self.view.show_error("Produto não encontrado.")
                return
            dados_produto = self.view.get_dados_produto(produto_existente)
            produto_atualizado = Produto(
                id = id_produto,
                nome=dados_produto['nome'],
                valor=dados_produto['valor'],
                estoque=dados_produto['estoque']
            )
            if self.dao.update(produto_atualizado):
                self.view.show_message("Produto atualizado com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar produto!")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar produto: {str(e)}")

    def delete_produto(self):
        try:
            id_produto = self.view.get_id()
            if self.dao.delete(id_produto):
                self.view.show_message("Produto deletado com sucesso!")
            else:
                self.view.show_error("Produto não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar produto: {str(e)}")

    def list_produtos(self):
        try:
            produtos = self.dao.get_all()
            self.view.show_produtos(produtos)
        except Exception as e:
            self.view.show_error(f"Erro ao listar produtos: {str(e)}")

    def list_produto_by_id(self):
        try:
            id_produto = self.view.get_id()
            produto = self.dao.get_by_id(id_produto)
            if not produto:
                self.view.show_error("Produto não encontrado!")
                return
            self.view.show_produto_details(produto)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar produto: {str(e)}")