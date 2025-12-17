from model.dao.produto_dao_mysql import Produto_DAO
from view.produto_view import Produto_View
from control.produto_controller import Produto_Controller

from model.dao.clientes_dao import Clientes_DAO
from view.clientes_view import Clientes_View
from control.clientes_controller import Clientes_Controller

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "exemplo_crud_python"
}

def main():
    produto_dao = Produto_DAO(db_config)
    produto_view = Produto_View()
    produto_controller = Produto_Controller(produto_dao, produto_view)
    produto_view.run()

    #clientes_dao = Clientes_DAO()
    #clientes_view = Clientes_View()
    #clientes_controller = Clientes_Controller(clientes_dao, clientes_view)
    #clientes_view.run()

if __name__ == "__main__":
    main()