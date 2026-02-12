
from model.dao.produto_dao_mysql import Produto_DAO
from model.dao.movimentacao_dao import Movimentacao_DAO
from model.dao.enderecos_dao import Enderecos_DAO
from model.dao.clientes_dao_mysql import Clientes_DAO
from model.dao.contatos_dao import Contatos_DAO
from model.dao.fornecedor_dao_mysql import Fornecedor_DAO
from model.dao.categoria_dao import Categoria_DAO
from view.produto_gui import Produto_View
from view.movimentacao_gui import Movimentacao_View
from view.enderecos_gui import Enderecos_View
from view.clientes_gui import Clientes_View
from view.contatos_gui import Contatos_View
from view.fornecedor_gui import Fornecedor_View
from view.categoria_gui import Categoria_View
from view.categoria_v2_gui import Categoria_V2_View
from view.categoria_fornecedor_gui import Categoria_Fornecedor_View
from control.produto_controller import Produto_Controller
from control.movimentacao_controller import Movimentacao_Controller
from control.enderecos_controller import Enderecos_Controller
from control.clientes_controller import Clientes_Controller
from control.contatos_controller import Contatos_Controller
from control.fornecedor_controller import Fornecedor_Controller
from control.categoria_controller import Categoria_Controller
from control.categoria_v2_controller import Categoria_V2_Controller

class Main_Controller:
    def __init__(self, main_view, db_config):
        self.main_view = main_view
        self.db_config = db_config

    def exibir_produtos(self):
        dao = Produto_DAO(self.db_config)
        view = Produto_View() 
        ctrl = Produto_Controller(dao, view)
        view.run()

    def exibir_movimentacao(self):
        dao_mov = Movimentacao_DAO(self.db_config)
        dao_prod = Produto_DAO(self.db_config)
        view = Movimentacao_View() 
        ctrl = Movimentacao_Controller(dao_mov, dao_prod, view)
        ctrl.list_related_produtos()

    def exibir_enderecos(self):
        dao_end = Enderecos_DAO(self.db_config)
        dao_cli = Clientes_DAO(self.db_config)
        view = Enderecos_View() 
        ctrl = Enderecos_Controller(dao_end, dao_cli, view)
        ctrl.list_related_clientes()

    def exibir_clientes(self):
        dao = Clientes_DAO(self.db_config)
        view = Clientes_View()
        ctrl = Clientes_Controller(dao, view)
        view.run()

    def exibir_contatos(self):
        dao_con = Contatos_DAO(self.db_config)
        dao_for = Fornecedor_DAO(self.db_config)
        view = Contatos_View() 
        ctrl = Contatos_Controller(dao_con, dao_for, view)
        ctrl.list_related_fornecedor()

    def exibir_fornecedor(self):
        dao = Fornecedor_DAO(self.db_config)
        view = Fornecedor_View()
        ctrl = Fornecedor_Controller(dao, view)
        view.run()

    def exibir_categorias(self):
        dao_cat = Categoria_DAO(self.db_config)
        dao_prod = Produto_DAO(self.db_config)
        view = Categoria_View()
        ctrl = Categoria_Controller(dao_cat, dao_prod, view)
        ctrl.abrir_tela()
    
    def exibir_categorias_v2(self):
        dao_cat = Categoria_DAO(self.db_config)
        dao_prod = Produto_DAO(self.db_config)
        dao_for = Fornecedor_DAO(self.db_config)
        view = Categoria_V2_View()
        ctrl = Categoria_V2_Controller(dao_cat, dao_prod, dao_for, view)
        ctrl.abrir_tela_produto()

    def exibir_categorias_fornecedor(self):
        dao_cat = Categoria_DAO(self.db_config)
        dao_prod = Produto_DAO(self.db_config)
        dao_for = Fornecedor_DAO(self.db_config)
        view = Categoria_Fornecedor_View()
        ctrl = Categoria_V2_Controller(dao_cat, dao_prod, dao_for, view)
        ctrl.abrir_tela_fornecedor()