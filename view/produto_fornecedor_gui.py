import tkinter as tk
from tkinter import messagebox, ttk

class Produto_Fornecedor_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Gestão de Produtos de Fornecedores")
        self.root.geometry("700x550")
        
        self.var_p = tk.StringVar()
        self.var_f = tk.StringVar()
        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="PRODUTOS DE FORNECEDORES", font=("Arial", 14, "bold"), pady=10).pack()
        
        frame = tk.LabelFrame(self.root, text=" Novo Vínculo ", padx=10, pady=10)
        frame.pack(fill="x", padx=20)

        tk.Label(frame, text="Produto:").grid(row=0, column=0)
        self.cb_p = ttk.Combobox(frame, textvariable=self.var_p, width=30, state="readonly")
        self.cb_p.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Fornecedor:").grid(row=0, column=2)
        self.cb_f = ttk.Combobox(frame, textvariable=self.var_f, width=30, state="readonly")
        self.cb_f.grid(row=0, column=3, padx=5)

        tk.Button(self.root, text="VINCULAR", bg="#d4edda", width=15, command=self._acao_vincular).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("id", "f", "p"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("f", text="Fornecedor")
        self.tree.heading("p", text="Produto")
        self.tree.column("id", anchor="center")
        self.tree.column("f", anchor="center")
        self.tree.column("p", anchor="center")

        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

    def _acao_vincular(self):
        self.controller.add_vinculo()
        self.controller.list_vinculos()

    def get_dados_vinculo(self):
        try:
            return {
                "id_p": int(self.var_p.get().split(" - ")[0]), 
                "id_f": int(self.var_f.get().split(" - ")[0])
            }
        except:
            return None

    def preencher_combos(self, prods, forn):
        self.cb_p['values'] = [f"{p._id} - {p._nome}" for p in prods]
        self.cb_f['values'] = [f"{f._id} - {f._nome_fantasia}" for f in forn]

    def show_vinculos(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for item in lista:
            self.tree.insert("", "end", values=item)

    def run(self):
        self.root.grab_set()
        self.root.focus_force()

    def show_message(self, m): messagebox.showinfo("Sucesso", m)
    def show_error(self, e): messagebox.showerror("Erro", e)