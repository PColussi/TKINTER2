import tkinter as tk
from tkinter import messagebox

class LoginInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Variáveis para armazenar o e-mail e a senha
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Rótulos e campos de entrada
        tk.Label(root, text="E-mail:").grid(row=0, column=0, sticky=tk.E)
        tk.Entry(root, textvariable=self.email_var).grid(row=0, column=1)

        tk.Label(root, text="Senha:").grid(row=1, column=0, sticky=tk.E)
        tk.Entry(root, textvariable=self.password_var, show="*").grid(row=1, column=1)

        # Botão de login
        tk.Button(root, text="Login", command=self.login).grid(row=2, column=1, pady=10)

    def login(self):
        # Obtém o e-mail e a senha
        email = self.email_var.get()
        password = self.password_var.get()

        # Verifica as condições de login
        if "@" in email and len(password) > 6:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        else:
            messagebox.showerror("Erro", "E-mail ou senha inválidos. Verifique as restrições.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginInterface(root)
    root.mainloop()
