
from model.dao.produto_dao_mysql import Produto_DAO
from model.dao.movimentacao_dao import Movimentacao_DAO
from view.produto_gui import Produto_View
from view.movimentacao_gui import Movimentacao_View
from control.produto_controller import Produto_Controller
from control.movimentacao_controller import Movimentacao_Controller

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