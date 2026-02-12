import tkinter as tk
from tkinter import messagebox, ttk

class Categoria_Fornecedor_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Gestão de Categorias de Fornecedores")
        self.root.geometry("450x600")
        self.root.configure(bg="#f0f0f0")
        
        self.var_f = tk.StringVar()
        self.check_vars = {} 
        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CATEGORIAS POR FORNECEDOR", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        
        frame_f = tk.LabelFrame(self.root, text=" 1. Escolha o Fornecedor ", padx=10, pady=10)
        frame_f.pack(fill="x", padx=20)
        
        self.cb_f = ttk.Combobox(frame_f, textvariable=self.var_f, width=50, state="readonly")
        self.cb_f.pack()
        self.cb_f.bind("<<ComboboxSelected>>", lambda e: self.controller.carregar_checklists_fornecedor())

        tk.Label(self.root, text="2. Marque as Categorias:", bg="#f0f0f0").pack(pady=(15, 0))
        
        self.container_canvas = tk.Frame(self.root, bd=1, relief="sunken")
        self.container_canvas.pack(expand=True, fill="both", padx=20, pady=5)
        
        self.canvas = tk.Canvas(self.container_canvas, bg="white")
        self.scrollbar = tk.Scrollbar(self.container_canvas, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", expand=True, fill="both")
        self.scrollbar.pack(side="right", fill="y")

        tk.Button(self.root, text="SALVAR ALTERAÇÕES", bg="#28a745", fg="white", 
                  font=("Arial", 11, "bold"), command=self._acao_salvar).pack(pady=20, fill="x", padx=20)

    def desenhar_checklist(self, categorias):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.check_vars = {}

        for cat in categorias:
            var = tk.BooleanVar()
            self.check_vars[cat._id] = var
            cb = tk.Checkbutton(self.scrollable_frame, text=cat._nome, variable=var, 
                                bg="white", font=("Arial", 10), anchor="w")
            cb.pack(fill="x", padx=10, pady=2)

    def marcar_checks(self, lista_ids_vinculados):
        for id_cat, var in self.check_vars.items():
            var.set(id_cat in lista_ids_vinculados)

    def _acao_salvar(self):
        self.controller.sincronizar_fornecedor()

    def get_id_fornecedor(self):
        try: return int(self.var_f.get().split(" - ")[0])
        except: return None

    def get_ids_selecionados_fornecedor(self):
        return [id_cat for id_cat, var in self.check_vars.items() if var.get()]

    def run(self):
        self.root.grab_set()

    def show_message(self, m): messagebox.showinfo("Sucesso", m)