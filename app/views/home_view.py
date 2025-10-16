import customtkinter as ctk
from app.views.dashboard_view import DashboardView
from app.views.employee_view import EmployeeView
from app.views.user_view import UserView

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # label = ctk.CTkLabel(self, text="Página Inicial!(Home)")
        # label.pack()

        # Menu lateral (widgets)
        self.side_menu = ctk.CTkFrame(self, width=200)
        self.side_menu.pack(side='left', fill='y', padx=10, pady=10)

        #Botões para o menu lateral
        self.btn_home = ctk.CTkButton(self.side_menu, text="Home", command=self.show_home)
        self.btn_home.pack(pady=10, padx=10)

        self.btn_dashboard = ctk.CTkButton(self.side_menu, text="Dashboard", command=self.show_dashboard)
        self.btn_dashboard.pack(pady=10, padx=10)

        self.btn_employees = ctk.CTkButton(self.side_menu, text="Funcionários", command=self.show_employees)
        self.btn_employees.pack(pady=10, padx=10)

        self.btn_users = ctk.CTkButton(self.side_menu, text="Usuários", command=self.show_users)
        self.btn_users.pack(pady=10, padx=10)


        # Mostrar o menu de usuários, somente se o user ativo for o admin

        # Frames do conteúdo da homepage
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side='left', fill='both', expand=True, pady=10, padx=10)

        self.show_home()

    # Função para limpar conteúdos
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    # A função para mostrar a homepage
    def show_home(self):
        self.clear_content()
        welcome_label = ctk.CTkLabel(self.content_frame, text="Bem-vindo ao Sistema!", font=('Arial bold', 20))
        welcome_label.pack(pady=20)

    # Função para mostrar a Dashboard
    def show_dashboard(self):
        self.clear_content()
        self.dashboard_view = DashboardView(self.content_frame, self.controller)
        self.dashboard_view.pack(fill='both', expand=True)

    # Função para mostrar tela de Funcionários
    def show_employees(self):
        self.clear_content()
        self.employees_view = EmployeeView(self.content_frame, self.controller)
        self.employees_view.pack(fill='both', expand=True)

    # Função para mostrar Usuários
    def show_users(self):
        self.clear_content()
        self.user_view = UserView(self.content_frame, self.controller)
        self.user_view.pack(fill='both', expand=True)

