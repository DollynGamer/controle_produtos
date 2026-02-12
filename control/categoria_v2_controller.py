class Categoria_V2_Controller:
    def __init__(self, dao_cat, dao_prod, dao_for, view):
        self.dao_cat = dao_cat
        self.dao_prod = dao_prod
        self.dao_for = dao_for
        self.view = view
        self.view.controller = self

    def carregar_checklists_produto(self):
        id_p = self.view.get_id_produto()
        if id_p:
            vinculos = self.dao_cat.get_categorias_por_produto(id_p)
            self.view.marcar_checks(vinculos)

    def sincronizar_produto(self):
        id_p = self.view.get_id_produto()
        ids_selecionados = self.view.get_ids_selecionados_produto()
        if id_p:
            self.dao_cat.sincronizar_vinculos_produto(id_p, ids_selecionados)
            self.view.show_message("Categorias atualizadas!")

    def abrir_tela_produto(self):
        self.view.cb_p['values'] = [f"{p._id} - {p._nome}" for p in self.dao_prod.get_all()]
        self.view.desenhar_checklist(self.dao_cat.get_all())
        self.view.run()

    def carregar_checklists_fornecedor(self):
        id_f = self.view.get_id_fornecedor()
        if id_f:
            vinculos = self.dao_cat.get_categorias_por_fornecedor(id_f)
            self.view.marcar_checks(vinculos)

    def sincronizar_fornecedor(self):
        id_f = self.view.get_id_fornecedor()
        ids_selecionados = self.view.get_ids_selecionados_fornecedor()
        if id_f:
            self.dao_cat.sincronizar_vinculos_fornecedor(id_f, ids_selecionados)
            self.view.show_message("Categorias atualizadas!")

    def abrir_tela_fornecedor(self):
        self.view.cb_f['values'] = [f"{f._id} - {f._nome_fantasia}" for f in self.dao_for.get_all()]
        self.view.desenhar_checklist(self.dao_cat.get_all())
        self.view.run()