from model.dao.produto_dao import Produto_DAO
from view.produto_view import Produto_View
from control.produto_controller import Produto_Controller

def main():
    produto_dao = Produto_DAO()
    produto_view = Produto_View()
    produto_controller = Produto_Controller(produto_dao, produto_view)
    produto_view.run()

if __name__ == "__main__":
    main()