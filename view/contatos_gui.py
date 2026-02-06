import tkinter as tk
from tkinter import messagebox, ttk

class Contatos_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Gestão de Contatos")
        self.root.geometry("850x600")

        self.var_id = tk.StringVar()
        self.var_fornecedor_str = tk.StringVar()
        self.var_nome = tk.StringVar()
        self.var_telefone = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_tipo = tk.StringVar(value="Vendas")

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE CONTATOS", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text=" Dados do Contato ", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Fornecedor:").grid(row=0, column=2, sticky="e")
        self.combo_fornecedor = ttk.Combobox(frame_form, textvariable=self.var_fornecedor_str, width=35, state="readonly")
        self.combo_fornecedor.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Nome:").grid(row=1, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_nome, width=15).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Telefone:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_telefone, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Email:").grid(row=2, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_email, width=15).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Tipo:").grid(row=2, column=2, sticky="e")
        ttk.OptionMenu(frame_form, self.var_tipo, "Vendas", "Vendas", "Suporte").grid(row=2, column=3, sticky="w", padx=5)

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self.limpar_campos, width=15).pack(side=tk.LEFT, padx=5)

        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "for", "nome", "telefone", "email", "tipo")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")
        self.tree.heading("id", text="ID"); self.tree.heading("for", text="Fornecedor")
        self.tree.heading("nome", text="Nome"); self.tree.heading("telefone", text="Telefone")
        self.tree.heading("email", text="Email"); self.tree.heading("tipo", text="Tipo")

        for col in self.colunas: self.tree.column(col, anchor="center")
        self.tree.column("for", width=250, anchor="w")
        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_contatos(self):
        try:
            return {
                "id_fornecedor": int(self.var_fornecedor_str.get().split(" - ")[0]),
                "nome": self.var_nome.get(),
                "telefone": self.var_telefone.get(),
                "email": self.var_email.get(),
                "tipo": self.var_tipo.get()
            }
        except:
            self.show_error("Dados inválidos!")
            return None

    def _acao_adicionar(self): 
        self.controller.add_contatos()
        self._acao_listar()
        self.limpar_campos()

    def _acao_editar(self): 
        self.controller.update_contatos()
        self._acao_listar()

    def _acao_excluir(self): 
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_contatos()
            self._acao_listar()
            self.limpar_campos()

    def _acao_listar(self): 
        if self.controller: self.controller.list_contatos()

    def show_contatos(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for c in lista:
            self.tree.insert("", "end", values=(c._id, f"{c._id_fornecedor} - {c._nome_f}", c._nome, c._telefone, c._email, c._tipo))

    def preencher_combo_fornecedor(self, lista):
        self.combo_fornecedor['values'] = [f"{f._id} - {f._nome_fantasia}" for f in lista]

    def get_id(self):
        val = self.var_id.get()
        return int(val) if val else None

    def limpar_campos(self):
        for v in [self.var_id, self.var_fornecedor_str, self.var_nome, self.var_telefone, self.var_email]: v.set("")
        self.var_tipo.set("Vendas")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel)['values']
            self.var_id.set(v[0])
            self.var_fornecedor_str.set(v[1])
            self.var_nome.set(v[2])
            self.var_telefone.set(v[3])
            self.var_email.set(v[4])
            self.var_tipo.set(v[5])

    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)
    def show_error(self, err): messagebox.showerror("Erro", err)

