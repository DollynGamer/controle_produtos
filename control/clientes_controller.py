from model.clientes import Clientes
from model.dao.clientes_dao import Clientes_DAO

class Clientes_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def choice_processor(self, choice):
        try:
            if choice == '1':
                self.add_clientes()
            elif choice == '2':
                self.update_clientes()
            elif choice == '3':
                self.delete_clientes()
            elif choice == '4':
                self.list_clientes()
            elif choice == '5':
                self.list_clientes_by_id()
            else:
                self.view.show_error("Opção Inválida")
        except Exception as e:
            self.view.show_error(str(e))

    def add_clientes(self):
        try:
            dados_cliente = self.view.get_dados_cliente()
            cliente_novo = Clientes(
                id = None,
                nome=dados_cliente['nome'],
                email=dados_cliente['email'],
                renda=dados_cliente['renda'],
                cpf=dados_cliente['cpf']
            )
            cliente_salvo = self.dao.save(cliente_novo)
            self.view.show_message(f"Cliente adicionado com ID: {cliente_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar cliente: {str(e)}")

    def update_clientes(self):
        try:
            id_cliente = self.view.get_id()
            cliente_existente = self.dao.get_by_id(id_cliente)
            if not cliente_existente:
                self.view.show_error("Cliente não encontrado.")
                return
            dados_cliente = self.view.get_dados_cliente(cliente_existente)
            cliente_atualizado = Clientes(
                id = id_cliente,
                nome=dados_cliente['nome'],
                email=dados_cliente['email'],
                renda=dados_cliente['renda'],
                cpf=dados_cliente['cpf']
            )
            if self.dao.update(cliente_atualizado):
                self.view.show_message("Cliente atualizado com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar cliente!")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar cliente: {str(e)}")
    def delete_clientes(self):
        try:
            id_cliente = self.view.get_id()
            if self.dao.delete(id_cliente):
                self.view.show_message("Cliente deletado com sucesso!")
            else:
                self.view.show_error("Cliente não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar cliente: {str(e)}")
    def list_clientes(self):
        try:
            clientes = self.dao.get_all()
            self.view.show_clientes(clientes)
        except Exception as e:
            self.view.show_error(f"Erro ao listar clientes: {str(e)}")

    def list_clientes_by_id(self):
        try:
            id_cliente = self.view.get_id()
            cliente = self.dao.get_by_id(id_cliente)
            if not cliente:
                self.view.show_error("Cliente não encontrado!")
                return
            self.view.show_cliente_details(cliente)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar cliente: {str(e)}")