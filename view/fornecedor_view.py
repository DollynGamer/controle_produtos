from model.fornecedor import Fornecedor
import sys

class Fornecedor_View:
    def __init__(self):
        self.controller = None

    def show_menu(self):
        print("=== Menu de Fornecedores ===")
        print("1. Adicionar Fornecedor")
        print("2. Atualizar Fornecedor")
        print("3. Retirar Fornecedor")
        print("4. Listar Fornecedores")
        print("5. Listar Fornecedor por ID")
        print("6. Sair")

    def get_user_choice(self):
        choice = input("Escolha uma opção: ")
        return choice
    
    def run(self):
        while True:
            try:
                self.show_menu()
                choice = self.get_user_choice()
                if choice == "6":
                    print("Saindo do sistema...")
                    sys.exit()
                if self.controller:
                    self.controller.choice_processor(choice)
            except KeyboardInterrupt:
                print("\nSaindo do Sistema...")
                break
            except Exception as e:
                self.show_error(str(e))

    def show_error(self, message):
        print(f"[ERROR]: {message}")

    def show_message(self, message):
        print(f"[MENSAGEM]: {message}")

    def get_razao_social(self, default_razao_social=""):
        return input(f"Razão Social: [{default_razao_social}]: ") or default_razao_social
    
    def get_nome_fantasia(self, default_nome_fantasia=""):
        return input(f"Nome Fantasia: [{default_nome_fantasia}]: ") or default_nome_fantasia
    
    def get_cnpj(self, default_cnpj=""):
        return input(f"CNPJ: [{default_cnpj}]: ") or default_cnpj
    
    def get_email(self, default_email=""):
        return input(f"EMAIL: [{default_email}]: ") or default_email
    
    def get_id(self):
        id_input = input("ID do Fornecedor: ")
        return int(id_input)
    
    def get_dados_fornecedor(self, fornecedor=None):
        if fornecedor is None:
            razao_social = self.get_razao_social()
            nome_fantasia = self.get_nome_fantasia()
            cnpj = self.get_cnpj()
            email = self.get_email()
        else:
            razao_social = self.get_razao_social(fornecedor._razao_social)
            nome_fantasia = self.get_nome_fantasia(fornecedor._nome_fantasia)
            cnpj = self.get_cnpj(fornecedor._cnpj)
            email = self.get_email(fornecedor._email)
        return {
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "cnpj": cnpj,
            "email": email
        }
    
    def show_fornecedores(self, fornecedores):
        if not fornecedores:
            print("Nenhum fornecedor cadastrado.")
            return
        print('-'*65)
        print(f"{'LISTA DE FORNECEDORES':^65}")
        print('-'*65)
        print(f"{'ID':<5} {'RAZAO SOCIAL':<20} {'NOME FANTASIA':<10} {'CNPJ':<10} {'EMAIL':<20}")
        for fornecedor in fornecedores:
            print(f"{fornecedor._id:<5} {fornecedor._razao_social:<20} {fornecedor._nome_fantasia:<10} {fornecedor._cnpj:<10} {fornecedor._email:<20}")

    def show_fornecedor_details(self, fornecedor):
        if fornecedor is None:
            print("Fornecedor não escontrado.")
            return
        print('-'*20)
        print(f"{'DETALHES DO FORNECEDOR':<20}")
        print('-'*20)
        print(f"ID: {fornecedor._id}")
        print(f"Razão Social: {fornecedor._razao_social}")
        print(f"Nome Fantasia: {fornecedor._nome_fantasia}")
        print(f"CNPJ: {fornecedor._cnpj}")
        print(f"Email: {fornecedor._email}")