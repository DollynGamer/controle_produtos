class Categoria_V2_Controller:
    def __init__(self, dao_cat, dao_prod, view):
        self.dao_cat = dao_cat
        self.dao_prod = dao_prod
        self.view = view
        self.view.controller = self

    def carregar_checklists(self):
        id_p = self.view.get_id_produto()
        if id_p:
            vinculos = self.dao_cat.get_categorias_por_produto(id_p)
            self.view.marcar_checks(vinculos)

    def sincronizar(self):
        id_p = self.view.get_id_produto()
        ids_selecionados = self.view.get_ids_selecionados()
        if id_p:
            self.dao_cat.sincronizar_vinculos(id_p, ids_selecionados)
            self.view.show_message("Categorias atualizadas!")

    def abrir_tela(self):
        self.view.cb_p['values'] = [f"{p._id} - {p._nome}" for p in self.dao_prod.get_all()]
        self.view.desenhar_checklist(self.dao_cat.get_all())
        self.view.run()