from model.produto import Produto
import sys

class Produto_View:
    def __init__(self):
        self.controller = None

    def show_menu(self):
        print("=== Menu de Produtos ===")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Deletar Produto")
        print("4. Listar Produtos")
        print("5. Listar Produtos por ID")
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
    
    def get_valor(self, default_valor=0.0):
        valor_input = input(f"Valor [{default_valor:.2f}]: ") or str(default_valor)
        return float(valor_input)
    
    def get_estoque(self, default_estoque=0):
        estoque_input = input(f"Estoque: [{default_estoque}]: ") or str(default_estoque)
        return int(estoque_input)
    
    def get_dados_produto(self, produto=None):
        if produto is None:
            nome = self.get_nome()
            valor = self.get_valor()
            estoque = self.get_estoque()
        else:
            nome = self.get_nome(produto._nome)
            valor = self.get_valor(produto._valor)
            estoque = self.get_estoque(produto._estoque)
        return {
            "Nome": nome,
            "Valor": valor,
            "Estoque": estoque
        }
    
    def show_produtos(self, produtos):
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        print('-'*65)
        print(f"{'LISTA DE PRODUTOS':^65}")
        print('-'*65)
        print(f"{'ID':<5} {'NOME':<20} {'VALOR':<10} {'ESTOQUE':<10} {'VALOR EM ESTOQUE':<20}")
        for produto in produtos:
            print(f"{produto._id:<5} {produto._nome:<20} R$ {produto._valor:<10.2f} {produto._estoque:<10} R$ {produto._valor_em_estoque:<20.2f}")

    def show_produto_details(self, produto):
        if produto is None:
            print("Produto não escontrado.")
            return
        print('-'*20)
        print(f"{'DETALHES DO PRODUTO':<20}")
        print('-'*20)
        print(f"ID: {produto._id}")
        print(f"Nome: {produto._nome}")
        print(f"Valor: R$ {produto._valor:.2f}")
        print(f"Estoque: {produto._estoque}")
        print(f"Valor em Estoque: R$ {produto._valor_em_estoque:.2f}")