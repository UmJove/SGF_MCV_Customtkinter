import customtkinter as ctk

class EmployeeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ctk.CTkLabel(self, text="Tela de Funcionários!")
        label.pack()