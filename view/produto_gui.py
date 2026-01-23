import tkinter as tk
from tkinter import messagebox, ttk

class Produto_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Cadastro de Produtos")
        self.root.geometry("800x600")

        self.var_id = tk.StringVar()
        self.var_nome = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_estoque = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE PRODUTOS", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text="Dados do Produto",padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Nome:").grid(row=0, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_nome, width=35).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Preço Unit.:").grid(row=1, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_valor, width=15).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Estoque:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_estoque, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self.acao_editar, bg="#ff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._limpar_campos, width=15).pack(side=tk.LEFT, padx=5)


        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "nome", "preco", "qtd", "total")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("preco", text="Preço Unit.")
        self.tree.heading("qtd", text="Estoque")
        self.tree.heading("total", text="Total R$")

        for col in self.colunas: self.tree.column(col, anchor="center")

        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)