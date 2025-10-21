import customtkinter as ctk

class EmployeeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Frame de formulário (para cadastro de funcionários)
        header_frame = ctk.CTkFrame(self, fg_color="transparent") #fg_color="transparent"
        header_frame.pack(fill="x", pady=5)

        # Divisão de layout de grades
        header_frame.grid_columnconfigure((0,2), weight=0)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Frame de listagem de funcionários (ScrollableFrame)
        self.list_frame = ctk.CTkScrollableFrame(self, fg_color="transparent", label_text="Funcionários cadastrados no Sistema", label_anchor="w", label_font=("Arial bold", 20)) #fg_color="transparent"
        self.list_frame.pack(fill="both", expand=True, pady=10)

        
        # Widgets importantes
        page_title = ctk.CTkLabel(header_frame, text="Funcionários", font=("Arial bold", 36))
        page_title.grid(column=0, row=0, padx=10)

        add_employee_btn = ctk.CTkButton(header_frame, text="Novo funcionário", fg_color="#900090", command=self.show_add_employee_form)
        add_employee_btn.grid(column=2, row=0, padx=(0, 10))


    # Função para adicionar um funcionário
    def show_add_employee_form(self):
        ...


    # Função de atualizar a lista de funcionários após o cadastro ou ao iniciar o sistema

    # Função para exibir detalhes de funcionário

    # Função para atualizar os dados do funcionário

    # Função para deletar funcionário