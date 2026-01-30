from model.movimentacao import Movimentacao

class Movimentacao_Controller:
    def __init__(self, dao_mov, dao_prod, view):
        self.dao_mov = dao_mov
        self.dao_prod = dao_prod
        self.view = view
        self.view.controller = self

    def add_movimentacao(self):
        try:
            dados = self.view.get_dados_movimentacao()
            mov_nova = Movimentacao(
                id = None,
                id_produto=dados['id_produto'],
                tipo=dados['tipo'],
                quantidade=dados['quantidade']
            )
            self.dao_mov.save(mov_nova)
            self.view.show_message("Movimentação registrada com sucesso!")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar: {str(e)}")

    def update_movimentacao(self):
        try:
            id_mov = self.view.get_id()
            dados = self.view.get_dados_movimentacao()
            mov_atu = Movimentacao(id_mov, dados['id_produto'], dados['tipo'], dados['quantidade'])
            
            if self.dao_mov.update(mov_atu):
                self.view.show_message("Movimentação atualizada com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def delete_movimentacao(self):
        try:
            id_mov = self.view.get_id()
            if self.dao_mov.delte(id_mov):
                self.view.show_message("Movimentação excluída!")
            else:
                self.view.show_error("Não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def list_movimentacoes(self):
        try:
            movs = self.dao_mov.get_all()
            self.view.show_movimentacoes(movs)
        except Exception as e:
            self.view.show_error(f"Erro ao listar: {str(e)}")

    def list_related_produtos(self):
        self.view.preencher_combo_produtos(self.dao_prod.get_all())
        self.view.run()