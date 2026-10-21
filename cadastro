import random
import datetime
import ipywidgets as widgets
from IPython.display import display, clear_output

# ==========================================
# 1. MODELO E LÓGICA DE NEGÓCIO 
# ==========================================
class Usuario:
    def __init__(self, id_usuario, nome, data_nascimento, genero, username, senha):
        self.id = id_usuario
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.username = username
        self.senha = senha

class GerenciadorUsuarios:
    def __init__(self):
        self.banco_usuarios = {}
        self.admin_user = "admin"
        self.admin_pass = "admin123"

    def verificar_login(self, username, senha):
        """Verifica as credenciais do admin ou de qualquer usuário cadastrado de forma precisa."""
        user_clean = username.strip()
        senha_clean = senha.strip()

        if user_clean.lower() == self.admin_user.lower() and senha_clean == self.admin_pass:
            return "Administrador"

        for usr in self.banco_usuarios.values():
            if usr.username.strip().lower() == user_clean.lower() and usr.senha.strip() == senha_clean:
                return usr.nome
        return None

    def cadastrar(self, nome, data_nasc, genero, username, senha):
        """Valida os dados de entrada e armazena o novo usuário."""
        erros = []
        if not nome.strip():
            erros.append("Nome")
        if not data_nasc.strip():
            erros.append("Data de Nascimento")
        if not genero or genero == 'Selecione':
            erros.append("Gênero")
        if not username.strip():
            erros.append("Username")
        if not senha.strip():
            erros.append("Senha")

        if erros:
            campos_faltantes = ", ".join(erros)
            raise ValueError(f"Atenção! Faltam informações ou há caixas vazias: {campos_faltantes}.")

        try:
            datetime.datetime.strptime(data_nasc.strip(), "%d/%m/%Y")
        except ValueError:
            raise ValueError("O campo Data de Nascimento deve estar no formato DD/MM/AAAA.")

        for u in self.banco_usuarios.values():
            if u.username.lower().strip() == username.strip().lower():
                raise ValueError("Este nome de usuário já existe.")

        novo_id = self.gerar_id_unico()
        novo_usuario = Usuario(novo_id, nome.strip(), data_nasc.strip(), genero, username.strip(), senha.strip())
        self.banco_usuarios[novo_id] = novo_usuario
        return novo_usuario

    def gerar_id_unico(self):
        """Gera um ID corporativo único de 10 dígitos."""
        while True:
            novo_id = "".join([str(random.randint(0, 9)) for _ in range(10)])
            if novo_id not in self.banco_usuarios:
                return novo_id

# Inicialização do controlador de dados
gerenciador = GerenciadorUsuarios()

# ==========================================
#INTERFACE GRÁFICA ROXO OBSIDIANA (FRONTEND)
# ==========================================
out_status_cadastro = widgets.Output()
out_status_login = widgets.Output()
out_lista = widgets.Output()

titulo = widgets.HTML("""
    <div style='text-align: center; margin-bottom: 25px;'>
        <h2 style='color: #12005e; font-family: sans-serif; font-weight: 700; margin-bottom: 5px; letter-spacing: -0.5px;'>Portal de Credenciamento</h2>
        <span style='color: #4a148c; font-size: 0.85em; letter-spacing: 1.5px; font-weight: bold;'>OBSIDIAN PURPLE EDITION</span>
    </div>
""")

# --- FORMULÁRIO DE CADASTRO ---
layout_input = widgets.Layout(width='100%', margin='4px 0px 8px 0px')
txt_nome = widgets.Text(placeholder='Nome Completo', description='Nome:', layout=layout_input)
txt_data = widgets.Text(placeholder='DD/MM/AAAA', description='Nascimento:', layout=layout_input)
drp_genero = widgets.Dropdown(options=['Selecione', 'Masculino', 'Feminino', 'Outro', 'Não Informar'], description='Gênero:', layout=layout_input)
txt_user = widgets.Text(placeholder='Nome de usuário', description='Username:', layout=layout_input)
txt_senha = widgets.Password(placeholder='Senha de acesso', description='Senha:', layout=layout_input)

btn_cadastrar = widgets.Button(
    description="Registrar e Criar ID",
    layout=widgets.Layout(width='100%', height='40px', margin='10px 0px 5px 0px', border_radius='24px')
)
btn_cadastrar.style.button_color = '#311B92'
btn_cadastrar.style.text_color = 'white'

# --- FORMULÁRIO DE LOGIN ---
txt_login_user = widgets.Text(placeholder='Usuário ou Admin', description='Username:', layout=layout_input)
txt_login_senha = widgets.Password(placeholder='Sua Senha', description='Senha:', layout=layout_input)

btn_login = widgets.Button(
    description="Entrar no Sistema",
    layout=widgets.Layout(width='100%', height='40px', margin='10px 0px 5px 0px', border_radius='24px')
)
btn_login.style.button_color = '#4a148c'
btn_login.style.text_color = 'white'

# Construção das Abas (Tabs) da Esquerda
aba_cadastro = widgets.VBox([
    widgets.HTML("<h4 style='color: #12005e; margin: 10px 0; font-family: sans-serif; font-weight: 700;'>Crie sua conta</h4>"),
    txt_nome, txt_data, drp_genero, txt_user, txt_senha,
    btn_cadastrar,
    out_status_cadastro
])

aba_login = widgets.VBox([
    widgets.HTML("<h4 style='color: #12005e; margin: 10px 0; font-family: sans-serif; font-weight: 700;'>Faça seu Login</h4>"),
    txt_login_user, txt_login_senha,
    btn_login,
    out_status_login
])

grupo_abas = widgets.Tab()
grupo_abas.children = [aba_cadastro, aba_login]
grupo_abas.set_title(0, 'Cadastrar')
grupo_abas.set_title(1, 'Fazer Login')

# --- LISTA LATERAL DE CADASTRADOS ---
def atualizar_lista_colaboradores():
    """Atualiza a lista à direita com design elegante em tons de roxo obsidiana."""
    with out_lista:
        clear_output()
        if not gerenciador.banco_usuarios:
            display(widgets.HTML("""
                <div style='text-align: center; color: #78909C; padding-top: 60px; font-family: sans-serif; font-size: 0.95em;'>
                    Nenhum colaborador registrado ainda.
                </div>
            """))
            return

        html_cartoes = "<h4 style='color: #12005e; margin: 0 0 15px 0; font-family: sans-serif; font-weight: 700; font-size: 1.1em;'>Colaboradores</h4><div style='max-height: 380px; overflow-y: auto; padding-right: 5px;'>"

        for usr in reversed(list(gerenciador.banco_usuarios.values())):
            html_cartoes += f"""
            <div style="background-color: #1a0033; border-radius: 16px; padding: 16px; margin-bottom: 12px; font-family: sans-serif; border: 1px solid #311B92; box-shadow: 0 2px 8px rgba(49, 27, 146, 0.15);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-weight: bold; color: #ede7f6; font-size: 0.95em;">{usr.nome}</span>
                    <span style="font-family: monospace; font-size: 0.85em; background-color: #7b1fa2; color: #ffffff; padding: 3px 10px; border-radius: 12px; font-weight: bold;">ID: {usr.id}</span>
                </div>
                <div style="font-size: 0.8em; color: #b39ddb; line-height: 1.5;">
                    <b>User:</b> {usr.username} &nbsp;&bull;&nbsp;
                    <b>Nascimento:</b> {usr.data_nascimento} &nbsp;&bull;&nbsp;
                    <b>Gênero:</b> {usr.genero}
                </div>
            </div>
            """
        html_cartoes += "</div>"
        display(widgets.HTML(html_cartoes))

def ao_clicar_login(b):
    with out_status_login:
        clear_output()
        nome_usuario = gerenciador.verificar_login(txt_login_user.value, txt_login_senha.value)
        if nome_usuario:
            display(widgets.HTML(f"""
                <div style="padding: 10px 14px; border-radius: 12px; background-color: #E8F5E9; color: #1B5E20; font-family: sans-serif; font-size: 0.85em; margin-top: 10px; border: 1px solid #C8E6C9;">
                    ✓ Bem-vindo de volta, <b>{nome_usuario}</b>! Login realizado com sucesso.
                </div>
            """))
            # Limpar campos
            txt_login_user.value = ''
            txt_login_senha.value = ''
        else:
            display(widgets.HTML("""
                <div style="padding: 10px 14px; border-radius: 12px; background-color: #FFEBEE; color: #C62828; font-family: sans-serif; font-size: 0.85em; margin-top: 10px; border: 1px solid #FFCDD2;">
                    ⚠ Usuário ou senha incorretos.
                </div>
            """))

def ao_clicar_cadastrar(b):
    with out_status_cadastro:
        clear_output()
        try:
            usuario_salvo = gerenciador.cadastrar(
                nome=txt_nome.value,
                data_nasc=txt_data.value,
                genero=drp_genero.value,
                username=txt_user.value,
                senha=txt_senha.value
            )

            # Alerta de sucesso específico solicitado
            display(widgets.HTML(f"""
            <div style="padding: 10px 14px; border-radius: 12px; background-color: #E8F5E9; color: #1B5E20; font-family: sans-serif; font-size: 0.85em; margin-top: 10px; border: 1px solid #C8E6C9;">
                ✓ <b>Cadastro feito com sucesso!</b> Colaborador registrado com o ID: <b>{usuario_salvo.id}</b>
            </div>
            """))

            # Limpar inputs de cadastro
            txt_nome.value = ''
            txt_data.value = ''
            drp_genero.value = 'Selecione'
            txt_user.value = ''
            txt_senha.value = ''

            atualizar_lista_colaboradores()

        except Exception as e:
            display(widgets.HTML(f"""
            <div style="padding: 10px 14px; border-radius: 12px; background-color: #FFEBEE; color: #C62828; font-family: sans-serif; font-size: 0.85em; margin-top: 10px; border: 1px solid #FFCDD2;">
                ⚠ {str(e)}
            </div>
            """))

btn_login.on_click(ao_clicar_login)
btn_cadastrar.on_click(ao_clicar_cadastrar)

# --- LAYOUT FINAL ---
coluna_esquerda = widgets.VBox([grupo_abas], layout=widgets.Layout(width='48%', padding='5px'))
coluna_direita = widgets.VBox([out_lista], layout=widgets.Layout(width='48%', padding='5px'))

painel_principal = widgets.HBox([coluna_esquerda, coluna_direita], layout=widgets.Layout(justify_content='space-between'))

container = widgets.VBox([
    titulo,
    painel_principal
], layout=widgets.Layout(width='75%', margin='0 auto', border='1px solid #d1c4e9', padding='30px', border_radius='24px', box_shadow='0px 8px 30px rgba(49, 27, 146, 0.12)', background_color='#FFFFFF'))

# Renderização inicial
display(container)
atualizar_lista_colaboradores()
