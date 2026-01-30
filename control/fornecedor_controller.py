from model.fornecedor import Fornecedor
from model.dao.fornecedor_dao import Fornecedor_DAO

class Fornecedor_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def choice_processor(self, choice):
        try:
            if choice == '1':
                self.add_fornecedor()
            elif choice == '2':
                self.update_fornecedor()
            elif choice == '3':
                self.delete_fornecedor()
            elif choice == '4':
                self.list_fornecedor()
            elif choice == '5':
                self.list_fornecedor_by_id()
            else:
                self.view.show_error("Opção Inválida")
        except Exception as e:
            self.view.show_error(str(e))

    def add_fornecedor(self):
        try:
            dados_fornecedor = self.view.get_dados_fornecedor()
            fornecedor_novo = Fornecedor(
                id = None,
                razao_social=dados_fornecedor['razao_social'],
                nome_fantasia=dados_fornecedor['nome_fantasia'],
                cnpj=dados_fornecedor['cnpj'],
                email=dados_fornecedor['email']
            )
            fornecedor_salvo = self.dao.save(fornecedor_novo)
            self.view.show_message(f"Fornecedor adicionado com ID: {fornecedor_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar fornecedor: {str(e)}")

    def update_fornecedor(self):
        try:
            id_fornecedor = self.view.get_id()
            fornecedor_existente = self.dao.get_by_id(id_fornecedor)
            if not fornecedor_existente:
                self.view.show_error("Fornecedor não encontrado.")
                return
            dados_fornecedor = self.view.get_dados_fornecedor(fornecedor_existente)
            fornecedor_atualizado = Fornecedor(
                id = id_fornecedor,
                razao_social=dados_fornecedor['razao_social'],
                nome_fantasia=dados_fornecedor['nome_fantasia'],
                cnpj=dados_fornecedor['cnpj'],
                email=dados_fornecedor['email']
            )
            if self.dao.update(fornecedor_atualizado):
                self.view.show_message("Fornecedor atualizado com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar fornecedor!")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar fornecedor: {str(e)}")

    def delete_fornecedor(self):
        try:
            id_fornecedor = self.view.get_id()
            if self.dao.delete(id_fornecedor):
                self.view.show_message("Fornecedor deletado com sucesso!")
            else:
                self.view.show_error("Fornecedor não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar fornecedor: {str(e)}")

    def list_fornecedores(self):
        try:
            fornecedores = self.dao.get_all()
            self.view.show_fornecedores(fornecedores)
        except Exception as e:
            self.view.show_error(f"Erro ao listar fornecedores: {str(e)}")

    def list_fornecedor_by_id(self):
        try:
            id_fornecedor = self.view.get_id()
            fornecedor = self.dao.get_by_id(id_fornecedor)
            if not fornecedor:
                self.view.show_error("Fornecedor não encontrado!")
                return
            self.view.show_fornecedor_details(fornecedor)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar fornecedor: {str(e)}")