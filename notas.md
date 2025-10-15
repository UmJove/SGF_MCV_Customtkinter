# AULAS:

### MINHA PLAYLIST:
### [Customtkinter c/ Arquitetura MVC](https://www.youtube.com/playlist?list=PLemyHd_j0duAYSurKP2-SDf1v3eQCLiAZ)
---

### [01/SGF - Preparação do Ambiente e Executando a nossa primeira Janela.](https://www.youtube.com/watch?v=cj0qDJcH1s0)

- Criação de arq **_README.md_**;
- Criação de arquivo **_main.py_**;
- Criação pastas (MCV) e seus arquivos de `__init__`;
- Criação da classe `AppController` e sua função `run()`;
- Instanciação de `AppController` em **_main.py_** e função `run()`;

### [02/SGF - Modelo de Usuários - Banco de Dados](https://www.youtube.com/watch?v=GSk3vLjjM8w)

- Criação de arquivo **_database.py_**, 
    - import de _sqlite3_,
    - criação classe `DataBase` e sua função `create_tables()`,
        - ativação da função criada no `__init__` da classe;
- Import de `DataBase` para o arquivo **_app_controller_**,
    - instanciação da classe `DataBase` no `__init__` da classe `AppController` (criando a tabela caso ela ainda não exista quando o programa for rodado);
- Rodar o programa em **_main.py_** para ver a criação da tabela;

### [03/SGF || CUSTOMTKINTER - Banco de Dados com Python - Criando tabela de funcionários](https://youtu.be/XmEgkA5m_RE?si=B0AO_lXk3jz978mr)

- Adicionou a criação da tabela _employees_ dentro da função `create_tables`;
- Rodou o programa em **_main.py_** para confirmar criação da tabela dentro do arquivo **_app.db_**;

### [04/SGF || CUSTOMTKINTER - Navegação entre Telas (LOGIN - DASHBOARD)](https://youtu.be/j2wb4GYdSCc?si=bvrVEptCNDleUPXc)
- Em **_app_controller_** definiu o que precisaria ser criado com comentários:
        ```python
                # Tela de login
                
                # Criação de admin padrão (se não houver ainda um admin criado)

            # Controle de login do usuário
            def login(self):
                ...
            
            def logout(self):
                ...


            # Mostrar a tela de dashboard
            def show_dashboard_view(self):
                ...
        ```;

- Criou arquivos **_dashboard_view.py_** e **_login_view.py_**:
    - definiu suas classes `DashboardView(ctk.CTkFrame)` e `LoginView(ctk.CTkFrame)`,
        - subordinou elas ao atributo `AppController.root`(a CTk) e à classe `AppController`;

- Chamou no arquivo **_app_controller.py_** a classe `LoginView(ctk.CTkFrame)`;


### []()


**__**

### []()

### []()

### []()

### []()

### []()

### []()