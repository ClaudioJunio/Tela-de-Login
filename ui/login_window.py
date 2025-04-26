import tkinter as tk
from tkinter import messagebox

# Importa a função de autenticação
from core.auth import authenticate


# Define a classe da tela de login
class LoginWindow:
    def __init__(self, master):
        # Guarda a referência da janela principal
        self.master = master

        # Define o título da janela
        self.master.title("Tela de Login")

        # Define um tamanho fixo para a janela (largura x altura)
        self.master.geometry("400x300")

        # Impede o redimensionamento da janela
        self.master.resizable(False, False)

        # Cria um frame centralizado dentro da janela para organizar os elementos
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True)

        # Label do título
        self.title_label = tk.Label(self.frame, text="Bem-vindo!", font=("Helvetica", 18, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Label e campo de entrada para o nome de usuário
        self.username_label = tk.Label(self.frame, text="Usuário:")
        self.username_label.grid(row=1, column=0, sticky="e", pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Label e campo de entrada para a senha
        self.password_label = tk.Label(self.frame, text="Senha:")
        self.password_label.grid(row=2, column=0, sticky="e", pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")  # Oculta o texto digitado
        self.password_entry.grid(row=2, column=1, pady=5)

        # Botão para fazer login
        self.login_button = tk.Button(self.frame, text="Entrar", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Checkbox para mostrar ou ocultar a senha
        self.show_password = tk.BooleanVar()  # Variável de controle do checkbox
        self.show_password_check = tk.Checkbutton(
            self.frame,
            text="Mostrar senha",
            variable=self.show_password,
            command=self.toggle_password_visibility
        )
        self.show_password_check.grid(row=4, column=0, columnspan=2)

    # Função para alternar a visibilidade da senha
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.password_entry.config(show="")  # Mostra a senha
        else:
            self.password_entry.config(show="*")  # Oculta a senha

    # Função chamada ao clicar no botão de login
    def login(self):
        # Obtém os dados digitados pelo usuário
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Verifica se os campos estão vazios
        if not username or not password:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        # Tenta autenticar o usuário usando os dados fornecidos
        if authenticate(username, password):
            # Se for válido, mostra mensagem de boas-vindas
            messagebox.showinfo("Login", f"Login bem-sucedido!\nBem-vindo, {username}!")
        else:
            # Se for inválido, mostra erro
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

