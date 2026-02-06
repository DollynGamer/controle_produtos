import tkinter as tk

class Main_gui:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Sistema de Gestão")
        self.root.state('zoomed')
        
        self._setup_menu()
        
        # Tela de boas-vindas simples
        tk.Label(self.root, text="Seja Bem-vindo ao Sistema", font=("Arial", 16)).pack(expand=True)

    def _setup_menu(self):
        barra_menu = tk.Menu(self.root)
        
        # Menu Cadastros
        menu_cadastros = tk.Menu(barra_menu, tearoff=0)
        menu_cadastros.add_command(label="Produtos", command=self._abrir_produtos)
        menu_cadastros.add_command(label="Movimentação", command=self._abrir_movimentacao)
        menu_cadastros.add_command(label="Endereços", command=self._abrir_enderecos)
        menu_cadastros.add_command(label="Clientes", command=self._abrir_clientes)
        menu_cadastros.add_command(label="Contatos", command=self._abrir_contatos)
        menu_cadastros.add_command(label="Fornecedor", command=self._abrir_fornecedor)
        menu_cadastros.add_separator()
        menu_cadastros.add_command(label="Sair", command=self.root.quit)
        
        barra_menu.add_cascade(label="Módulos", menu=menu_cadastros)
        self.root.config(menu=barra_menu)

    def _abrir_produtos(self):
        if self.controller:
            self.controller.exibir_produtos()

    def _abrir_movimentacao(self):
        if self.controller:
            self.controller.exibir_movimentacao()

    def _abrir_enderecos(self):
        if self.controller:
            self.controller.exibir_enderecos()

    def _abrir_clientes(self):
        if self.controller:
            self.controller.exibir_clientes()

    def _abrir_contatos(self):
        if self.controller:
            self.controller.exibir_contatos()

    def _abrir_fornecedor(self):
        if self.controller:
            self.controller.exibir_fornecedor()

    def run(self):
        self.root.mainloop()