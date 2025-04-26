# Importa o módulo Tkinter para criar a janela principal da aplicação
import tkinter as tk

# Importa a classe LoginWindow da pasta ui (nossa interface gráfica)
from ui.login_window import LoginWindow

# Função principal que inicia o aplicativo
def main():
    # Cria a janela principal da aplicação
    root = tk.Tk()

    # Cria uma instância da nossa tela de login, passando a janela root
    app = LoginWindow(root)

    # Inicia o loop principal do Tkinter, que mantém a janela aberta e interativa
    root.mainloop()

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == "__main__":
    main()