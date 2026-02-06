import tkinter as tk
from tkinter import messagebox, ttk

class Enderecos_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Gestão de Endereços")
        self.root.geometry("850x600")

        self.var_id = tk.StringVar()
        self.var_cliente_str = tk.StringVar()
        self.var_cep = tk.StringVar()
        self.var_logradouro = tk.StringVar()
        self.var_cidade = tk.StringVar()
        self.var_tipo = tk.StringVar(value="Comercial")

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE ENDEREÇOS", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text=" Dados do Endereço ", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Cliente:").grid(row=0, column=2, sticky="e")
        self.combo_clientes = ttk.Combobox(frame_form, textvariable=self.var_cliente_str, width=35, state="readonly")
        self.combo_clientes.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="CEP:").grid(row=1, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_cep, width=15).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Logradouro:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_logradouro, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Cidade:").grid(row=2, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_cidade, width=15).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Tipo:").grid(row=2, column=2, sticky="e")
        ttk.OptionMenu(frame_form, self.var_tipo, "Comercial", "Comercial", "Residencial", "Entrega").grid(row=2, column=3, sticky="w", padx=5)

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self.limpar_campos, width=15).pack(side=tk.LEFT, padx=5)

        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "cli", "cep", "logradouro", "cidade", "tipo")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")
        self.tree.heading("id", text="ID"); self.tree.heading("cli", text="Cliente")
        self.tree.heading("cep", text="CEP"); self.tree.heading("logradouro", text="Logradouro")
        self.tree.heading("cidade", text="Cidade"); self.tree.heading("tipo", text="Tipo")

        for col in self.colunas: self.tree.column(col, anchor="center")
        self.tree.column("cli", width=250, anchor="w")
        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_enderecos(self):
        try:
            return {
                "id_cliente": int(self.var_cliente_str.get().split(" - ")[0]),
                "cep": self.var_cep.get(),
                "logradouro": self.var_logradouro.get(),
                "cidade": self.var_cidade.get(),
                "tipo": self.var_tipo.get()
            }
        except:
            self.show_error("Dados inválidos!")
            return None

    def _acao_adicionar(self): 
        self.controller.add_enderecos()
        self._acao_listar()
        self.limpar_campos()

    def _acao_editar(self): 
        self.controller.update_enderecos()
        self._acao_listar()

    def _acao_excluir(self): 
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_enderecos()
            self._acao_listar()
            self.limpar_campos()

    def _acao_listar(self): 
        if self.controller: self.controller.list_enderecos()

    def show_enderecos(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for e in lista:
            self.tree.insert("", "end", values=(e._id, f"{e._id_cliente} - {e._nome_c}", e._cep, e._logradouro, e._cidade, e._tipo))

    def preencher_combo_clientes(self, lista):
        self.combo_clientes['values'] = [f"{c._id} - {c._nome}" for c in lista]

    def get_id(self):
        val = self.var_id.get()
        return int(val) if val else None

    def limpar_campos(self):
        for v in [self.var_id, self.var_cliente_str, self.var_cep, self.var_logradouro, self.var_cidade]: v.set("")
        self.var_tipo.set("Comercial")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel)['values']
            self.var_id.set(v[0])
            self.var_cliente_str.set(v[1])
            self.var_cep.set(v[2])
            self.var_logradouro.set(v[3])
            self.var_cidade.set(v[4])
            self.var_tipo.set(v[5])

    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)
    def show_error(self, err): messagebox.showerror("Erro", err)

