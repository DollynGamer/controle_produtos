class Categoria_Controller:
    def __init__(self, dao_cat, dao_prod, view):
        self.dao_cat = dao_cat
        self.dao_prod = dao_prod
        self.view = view
        self.view.controller = self

    def add_vinculo(self):
        dados = self.view.get_dados_vinculo()
        if dados:
            try:
                self.dao_cat.vincular_produto(dados['id_p'], dados['id_c'])
                self.view.show_message("Vinculo N:N realizado com sucesso!")
            except Exception as e:
                self.view.show_error(f"Erro ao vincular: {e}")

    def list_vinculos(self):
        self.view.show_vinculos(self.dao_cat.get_vinculos_detalhados_produto())

    def abrir_tela(self):
        prods = self.dao_prod.get_all()
        cats = self.dao_cat.get_all()
        self.view.preencher_combos(prods, cats)
        self.list_vinculos()
        self.view.run()