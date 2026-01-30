import tkinter as tk
from tkinter import messagebox, ttk

class Fornecedor_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Cadastro de Fornecedores")
        self.root.geometry("800x600")

        self.var_id = tk.StringVar()
        self.var_razao_social = tk.StringVar()
        self.var_nome_fantasia = tk.StringVar()
        self.var_cnpj = tk.StringVar()
        self.var_email = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE FORNECEDORES", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text="Dados do Fornecedor",padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Razão Social:").grid(row=0, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_razao_social, width=35).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Nome fantasia:").grid(row=1, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_nome_fantasia, width=35).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="CNPJ:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_cnpj, width=35).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Email:").grid(row=2, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_email, width=35).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._limpar_campos, width=15).pack(side=tk.LEFT, padx=5)


        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "razao_social", "nome_fantasia", "cnpj", "email")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("razao_social", text="Razao Social")
        self.tree.heading("nome_fantasia", text="Nome Fantasia")
        self.tree.heading("cnpj", text="CNPJ")
        self.tree.heading("email", text="Email")

        for col in self.colunas: self.tree.column(col, anchor="center")

        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.mainloop()

    def get_dados_fornecedor(self, fornecedor_existente=None):
        try:
            return{
                "razao_social": self.var_razao_social.get(),
                "nome_fantasia": self.var_nome_fantasia.get(),
                "cnpj": self.var_cnpj.get(),
                "email": self.var_email.get()
            }
        except ValueError:
            self.show_error("Dados inválidos.")
            return None
        
    def _acao_adicionar(self):
        self.controller.add_fornecedor()
        self._acao_listar(self)

    def _acao_listar(self):
        if self.controller: self.controller.list_fornecedores()

    def show_fornecedores(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for p in lista:
            self.tree.insert("","end", values=(
                p._id, p._razao_social, p._nome_fantasia,
                p._cnpj, p._email
            ))

    def _acao_editar(self):
        self.controller.update_fornecedor()
        self._acao_listar()

    def get_id(self, operacao=""):
        val = self.var_id.get()
        return int(val) if val else None
    
    def _acao_excluir(self):
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_fornecedor()
            self._acao_listar()
            self._limpar_campos()

    def _limpar_campos(self):
        for var in [self.var_id, self.var_razao_social, self.var_nome_fantasia, self.var_cnpj, self.var_email]: var.set("")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel)['values']
            self.var_id.set(v[0])
            self.var_razao_social.set(v[1])
            self.var_nome_fantasia.set(v[2])
            self.var_cnpj.set(v[3])
            self.var_email.set(v[4])
    
    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)

    def show_error(self, err): messagebox.showerror("Erro", err)