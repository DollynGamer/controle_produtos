from model.enderecos import Enderecos

class Enderecos_Controller:
    def __init__(self, dao_end, dao_cli, view):
        self.dao_end = dao_end
        self.dao_cli = dao_cli
        self.view = view
        self.view.controller = self

    def add_enderecos(self):
        try:
            dados = self.view.get_dados_enderecos()
            end_nova = Enderecos(
                id = None,
                id_cliente=dados['id_cliente'],
                cep=dados['cep'],
                logradouro=dados['logradouro'],
                cidade=dados['cidade'],
                tipo=dados['tipo']
            )
            self.dao_end.save(end_nova)
            self.view.show_message("Endereço registrado com sucesso!")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar: {str(e)}")

    def update_enderecos(self):
        try:
            id_end = self.view.get_id()
            dados = self.view.get_dados_enderecos()
            end_atu = Enderecos(id_end, dados['id_cliente'], dados['cep'], dados['logradouro'], dados['cidade'], dados['tipo'])
            
            if self.dao_end.update(end_atu):
                self.view.show_message("Endereço atualizada com sucesso!")
            else:
                self.view.show_error("Erro ao atualizar!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def delete_enderecos(self):
        try:
            id_end = self.view.get_id()
            if self.dao_end.delete(id_end):
                self.view.show_message("Endereço excluído!")
            else:
                self.view.show_error("Não encontrado!")
        except Exception as e:
            self.view.show_error(f"Erro: {str(e)}")

    def list_enderecos(self):
        try:
            ends = self.dao_end.get_all()
            self.view.show_enderecos(ends)
        except Exception as e:
            self.view.show_error(f"Erro ao listar: {str(e)}")

    def list_related_clientes(self):
        self.view.preencher_combo_clientes(self.dao_cli.get_all())
        self.view.run()