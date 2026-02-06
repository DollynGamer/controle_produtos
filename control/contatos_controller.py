from model.contatos import Contatos


class Contatos_Controller:
    def __init__(self, dao_con, dao_for, view):
        self.dao_con = dao_con
        self.dao_for = dao_for
        self.view = view
        self.view.controller = self

    def add_contatos(self):
        try:
            dados = self.view.get_dados_contatos()
            con_nova = Contatos(
                id = None,
                id_fornecedor=dados['id_fornecedor'],
                nome=dados['nome'],
                telefone=dados['telefone'],
                email=dados['email'],
                tipo=dados['tipo']
            )
            self.dao_con.save(con_nova)
            self.view.show_message("Contatos registrado com sucesso!")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar: {str(e)}")

    def update_contatos(self):
        try:
            id_con = self.view.get_id()
            dados = self.view.get_dados_contatos()
            con_atu = Contatos(id_con, dados['id_fornecedor'], dados['nome'], dados['telefone'], dados['email'], dados['tipo'])
            
            if self.dao_end.update(con_atu):
                self.view.show_message("Contatos atualizada com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def delete_contatos(self):
        try:
            id_con = self.view.get_id()
            if self.dao_con.delete(id_con):
                self.view.show_message("Contatos excluído!")
            else:
                self.view.show_error("Não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def list_contatos(self):
        try:
            conts = self.dao_con.get_all()
            self.view.show_contatos(conts)
        except Exception as e:
            self.view.show_error(f"Erro ao listar: {str(e)}")

    def list_related_fornecedor(self):
        self.view.preencher_combo_fornecedor(self.dao_for.get_all())
        self.view.run()