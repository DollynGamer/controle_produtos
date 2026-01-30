import tkinter as tk
from tkinter import messagebox, ttk

class Movimentacao_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Gestão de Movimentações")
        self.root.geometry("850x600")

        self.var_id = tk.StringVar()
        self.var_produto_str = tk.StringVar()
        self.var_tipo = tk.StringVar(value="Entrada")
        self.var_qtd = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE MOVIMENTAÇÕES", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text=" Dados da Movimentação ", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Produto:").grid(row=0, column=2, sticky="e")
        self.combo_produtos = ttk.Combobox(frame_form, textvariable=self.var_produto_str, width=35, state="readonly")
        self.combo_produtos.grid(row=0, column=3, padx=5, pady=5)


        tk.Label(frame_form, text="Tipo:").grid(row=1, column=0, sticky="e")
        ttk.OptionMenu(frame_form, self.var_tipo, "Entrada", "Entrada", "Saída").grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(frame_form, text="Quantidade:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_qtd, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self.limpar_campos, width=15).pack(side=tk.LEFT, padx=5)

        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "prod", "tipo", "qtd", "data")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")
        self.tree.heading("id", text="ID"); self.tree.heading("prod", text="Produto")
        self.tree.heading("tipo", text="Tipo"); self.tree.heading("qtd", text="Qtd")
        self.tree.heading("data", text="Data/Hora")

        for col in self.colunas: self.tree.column(col, anchor="center")
        self.tree.column("prod", width=250, anchor="w")
        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_movimentacao(self):
        try:
            return {
                "id_produto": int(self.var_produto_str.get().split(" - ")[0]),
                "tipo": self.var_tipo.get(),
                "quantidade": int(self.var_qtd.get())
            }
        except:
            self.show_error("Dados inválidos!")
            return None

    def _acao_adicionar(self): 
        self.controller.add_movimentacao()
        self._acao_listar()
        self.limpar_campos()

    def _acao_editar(self): 
        self.controller.update_movimentacao()
        self._acao_listar()

    def _acao_excluir(self): 
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_movimentacao()
            self._acao_listar()
            self.limpar_campos()

    def _acao_listar(self): 
        if self.controller: self.controller.list_movimentacoes()

    def show_movimentacoes(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for m in lista:
            self.tree.insert("", "end", values=(m._id, f"{m._id_produto} - {m._nome_produto}", m._tipo, m._quantidade, m._data_movimentacao))

    def preencher_combo_produtos(self, lista):
        self.combo_produtos['values'] = [f"{p._id} - {p._nome}" for p in lista]

    def get_id(self):
        val = self.var_id.get()
        return int(val) if val else None

    def limpar_campos(self):
        for v in [self.var_id, self.var_produto_str, self.var_qtd]: v.set("")
        self.var_tipo.set("Entrada")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel)['values']
            self.var_id.set(v[0]); self.var_produto_str.set(v[1])
            self.var_tipo.set(v[2]); self.var_qtd.set(v[3])

    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)
    def show_error(self, err): messagebox.showerror("Erro", err)

