from model.clientes import Clientes
import sys

class Clientes_View:
    def __init__(self):
        self.controller = None

    def show_menu(self):
        print("=== Menu de Login ===")
        print("1. Adicionar Cliente")
        print("2. Atualizar Cliente")
        print("3. Deletar Cliente")
        print("4. Listar Clientes")
        print("5. Listar Clientes por ID")
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

    def get_nome(self, default_nome=""):
        return input(f"Nome [{default_nome}]: ") or default_nome
    
    def get_email(self, default_email=""):
        return input(f"Email [{default_email}]: ") or default_email
    
    def get_renda(self, default_renda=0.0):
        renda_input = input(f"Renda [{default_renda:.2f}]: ") or str(default_renda)
        return float(renda_input)

    def get_cpf(self, default_cpf=""):
        return input(f"CPF: [{default_cpf}]: ") or str(default_cpf)
    
    def get_id(self):
        id_input = input("ID do Cliente: ")
        return int(id_input)

    def get_dados_cliente(self, cliente=None):
        if cliente is None:
            nome = self.get_nome()
            email = self.get_email()
            renda = self.get_renda()
            cpf = self.get_cpf()
        else:
            nome = self.get_nome(cliente._nome)
            email = self.get_email(cliente._email)
            renda = self.get_renda(cliente._renda)
            cpf = self.get_cpf(cliente._cpf)
        return {
            "nome": nome,
            "email": email,
            "renda": renda,
            "cpf": cpf
        }
    
    def show_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return
        print('-'*65)
        print(f"{'LISTA DE CLIENTES':^65}")
        print('-'*65)
        print(f"{'ID':<5} {'NOME':<20} {'EMAIL':<20} {'RENDAS':<10} {'CPF':<15}")
        for cliente in clientes:
            print(f"{cliente._id:<5} {cliente._nome:<20} {cliente._email:<20} R$ {cliente._renda:<10.2f} {cliente._cpf:<15}")
            
    def show_cliente_details(self, cliente):
        if cliente is None:
            print("Cliente não encontrado.")
            return
        print('-'*20)
        print(f"{'DETALHES DO CLIENTE':<20}")
        print('-'*20)
        print(f"ID: {cliente._id}")
        print(f"Nome: {cliente._nome}")
        print(f"Email: {cliente._email}")
        print(f"Renda: R$ {cliente._renda:.2f}")
        print(f"CPF: {cliente._cpf}")