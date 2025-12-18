from model.dao.produto_dao_mysql import Produto_DAO
from view.produto_view import Produto_View
from control.produto_controller import Produto_Controller

from model.dao.clientes_dao import Clientes_DAO
from view.clientes_view import Clientes_View
from control.clientes_controller import Clientes_Controller

from model.dao.fornecedor_dao import Fornecedor_DAO
from view.fornecedor_view import Fornecedor_View
from control.fornecedor_controller import Fornecedor_Controller
from dotenv import load_dotenv
import os


db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
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

    #fornecedor_dao = Fornecedor_DAO(db_config)
    #fornecedor_view = Fornecedor_View()
    #fornecedor_controller = Fornecedor_Controller(fornecedor_dao, fornecedor_view)
    #fornecedor_view.run()

if __name__ == "__main__":
    main()