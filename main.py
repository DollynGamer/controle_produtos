from dotenv import load_dotenv
import os
from view.main_gui import Main_gui
from control.main_controller import Main_Controller

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def main():
    view_principal = Main_gui()
    controller_geral = Main_Controller(view_principal, db_config)
    view_principal.controller = controller_geral
    view_principal.run()

    #produto_dao = Produto_DAO(db_config)
    #produto_view = Produto_View()
    #produto_controller = Produto_Controller(produto_dao, produto_view)
    #produto_view.run()

    #clientes_dao = Clientes_DAO(db_config)
    #clientes_view = Clientes_View()
    #clientes_controller = Clientes_Controller(clientes_dao, clientes_view)
    #clientes_view.run()

    #fornecedor_dao = Fornecedor_DAO(db_config)
    #fornecedor_view = Fornecedor_View()
    #fornecedor_controller = Fornecedor_Controller(fornecedor_dao, fornecedor_view)
    #fornecedor_view.run()

if __name__ == "__main__":
    main()