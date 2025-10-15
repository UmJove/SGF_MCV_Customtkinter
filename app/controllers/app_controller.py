import customtkinter as ctk
from app.models.database import DataBase
from app.views.login_view import LoginView
from app.views.dashboard_view import DashboardView

class AppController:
    def __init__(self):
        self.db = DataBase()
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title("Sistema de Gestão de Funcionários")

        # Tela de login
        self.login_view = LoginView(self.root, self)
        self.login_view.pack(fill="both", expand=True)

        # Criação de admin padrão (se não houver ainda um admin criado)

    # Controle de login do usuário
    def login(self):
        ...
    
    def logout(self):
        ...


    # Mostrar a tela de dashboard
    def show_dashboard_view(self):
        ...


    def run(self):
        self.root.mainloop() 