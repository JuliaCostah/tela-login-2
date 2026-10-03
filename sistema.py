import customtkinter as ctk
import time
#_________________________Funções_____________________________

def ir_para_dashboard():
    
    janela_abas.set('Dashboard')

def mudar_modo_dark():
    
    if switch_mododark.get() == 1:
        ctk.set_appearance_mode('Dark')
    else:
        ctk.set_appearance_mode('Light')
        
def salvar_perfil():
    
    nome = campo_nome.get().title()
    
    if nivel_usuario.get() == 2:
        nivel = 'Administrador'
    else:
        nivel = 'Básico'

    receber_notificacoes = checkbox_notificacoes.get()
    subtitulo.configure(text=f'{nome}\n\n{nivel}')
    
def atualizar_volume(novo_valor_volume):
    
    label_valor_volume.configure(text=f'{novo_valor_volume:.0f}%')
    

def carregar():
    for i in range(101):
        barra_progresso.set((i + 1)/100)
        time.sleep(0.3)
        janela.update()
        volume.configure(text=f'{i}%')
    

ctk.set_appearance_mode('dark')

# Inicio janela
#--------------------------------------------------
janela = ctk.CTk()

janela.title('Sistema de Cadastro de Clientes')
janela.geometry('900x600')
janela.resizable(False,False)
#--------------------------------------------------
# Dividir a tela

janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0,weight=1)

#--------------------------------------------------
# Parte lateral

barra_lateral = ctk.CTkFrame(
    janela,
    width=200
)                     

barra_lateral.grid(
    row=0,
    column=0,
    sticky='nsew'
)

# Criando os elementos para o frame

titulo = ctk.CTkLabel(
    barra_lateral,
    text='Workspace',
    font=('Cascadia Code',28,'bold'),
    text_color="#D70D72"
)
titulo.pack(pady=(40,10),padx=(20,20))

subtitulo = ctk.CTkLabel(
    barra_lateral,
    text='',
    font=('Cascadia Code',16),
    text_color="#D70D72"
)
subtitulo.pack(pady=(5,20))


botao_principal = ctk.CTkButton(
    barra_lateral,
    text='Dashboard Principal',
    font=('Cascadia Code',18,'bold'),
    corner_radius=10,
    border_width=2,
    border_color="#0C090A",
    fg_color="transparent",
    cursor='hand2',
    hover_color= "#B5085F",
    command=ir_para_dashboard
    )
botao_principal.pack(pady=(40,20),padx=(20,20))

switch_mododark = ctk.CTkSwitch(
    barra_lateral,
    text='Modo Escuro',
    font=('Cascadia Code',18),
    progress_color="#B21463",
    button_color = "#840D49",
    button_hover_color= "#931956",
    command=mudar_modo_dark
)
switch_mododark.pack(side='bottom',pady=(0,40))
switch_mododark.select()
#--------------------------------------------------
# Parte Central

janela_abas = ctk.CTkTabview(
    janela,
    width=400,
    segmented_button_selected_color="#840D49",
    segmented_button_selected_hover_color="#B21463",
    segmented_button_unselected_color="#150D0D",
    segmented_button_unselected_hover_color="#635F5F",
    text_color='white'
)
janela_abas._segmented_button.configure(font=('Cascadia Code',15))
janela_abas.grid(row=0,column=1,sticky='nsew',padx=10)

janela_abas.add('Perfil')
aba_perfil = janela_abas.tab('Perfil')

janela_abas.add('Preferências')
aba_preferencias = janela_abas.tab('Preferências')

janela_abas.add('Dashboard')
aba_dashboard = janela_abas.tab('Dashboard')
#--------------------------------------------------
# Primeira aba

campo_nome = ctk.CTkEntry(
    aba_perfil,
    placeholder_text='Informe seu nome',
    width=250,
    height=20,
    font=('Cascadia Code',15)
)
campo_nome.pack(pady=(40,20))

nivel_usuario = ctk.IntVar(value=0)

radio_Label = ctk.CTkLabel(
    aba_perfil,
    text='Nível Usuário:',
    font=('Cascadia Code',20,'bold')                        
)
radio_Label.pack(pady=(30,10))

radio_basico = ctk.CTkRadioButton(
    aba_perfil,
    text='Básico',
    font=('Cascadia Code',16,'bold'),                        
    variable=nivel_usuario,
    value=1,
    fg_color="#840D49",
    hover_color="#B21463"
)
radio_basico.pack(anchor='w',padx=(220,0),pady=(10,10))

radio_admin = ctk.CTkRadioButton(
    aba_perfil,
    text='Administrador',
    font=('Cascadia Code',16,'bold'),                        
    variable=nivel_usuario,
    value=2,
    fg_color="#840D49",
    hover_color="#B21463"
)
radio_admin.pack(anchor='w',padx=(220,0),pady=(10,10))

checkbox_notificacoes = ctk.CTkCheckBox(
    aba_perfil,
    text='Receber notificações por e-mail',
    font=('Cascadia Code',16,'bold'), 
    fg_color="#840D49",
    hover_color="#B21463"                       
)
checkbox_notificacoes.pack(pady=(30,20))

botao_salvar_perfil = ctk.CTkButton(
    aba_perfil,
    text='Salvar perfil',
    font=('Cascadia Code',14),     
    fg_color='transparent',
    corner_radius=10,
    border_width=2,
    border_color="#0C090A",
    cursor='hand2',
    hover_color= "#B5085F",
    command=salvar_perfil          
)
botao_salvar_perfil.pack(pady=(30,30))

#_______________________ Aba Preferências_______________________
# Aqui terá um menu de escolha de idioma e um slider(controle deslizante) 
# para escolher o volume

label_idiomas = ctk.CTkLabel(
    aba_preferencias,
    text='Selecione o idioma:',
    font=('Cascadia Code',18,'bold')                        
)
label_idiomas.pack(pady=(20,5))

menu_opcoes = ctk.CTkOptionMenu(
    aba_preferencias,
    values=["Português","Inglês","Espanhol"],
    font=('Cascadia Code',14),
    fg_color="#B21463",
    button_color = "#840D49",
    button_hover_color= "#931956",
    dropdown_hover_color= "#840D49"                    
)
menu_opcoes.pack(pady=(5,10))

label_volume = ctk.CTkLabel(
    aba_preferencias,
    text='Volume',
    font=('Cascadia Code',18,'bold')                        
)
label_volume.pack(pady=(60,5))

slider_volume = ctk.CTkSlider(
    aba_preferencias,
    from_= 0, to=100,
    progress_color="#B21463",
    button_color = "#840D49",
    button_hover_color= "#931956",
    command=atualizar_volume
)
slider_volume.pack(pady=5)
slider_volume.set(50)

label_valor_volume = ctk.CTkLabel(
    aba_preferencias,
    text="50%",
)
label_valor_volume.pack()

#_______________________ Aba Dashboard_______________________
# Um label; uma barra de progresso e botão iniciar

label_carregamento = ctk.CTkLabel(
    aba_dashboard,
    text='Testar carregamento do sistema',
    font=('Cascadia Code',18,'bold')                        
)
label_carregamento.pack(pady=(20,20))

barra_progresso = ctk.CTkProgressBar(
    aba_dashboard,
    width=400,
    progress_color="#B21463",
)
barra_progresso.pack(pady=(10,10))
barra_progresso.set(0)

volume = ctk.CTkLabel(
    aba_dashboard,
    text='',
    font=('Cascadia Code',13)                       
)
volume.pack(pady=(5,10))

botao_iniciar = ctk.CTkButton(
    aba_dashboard,
    text='Iniciar simulação',
    fg_color='transparent',
    font=('Cascadia Code',14),     
    corner_radius=10,
    border_width=2,
    border_color="#0C090A",
    cursor='hand2',
    hover_color= "#B5085F",
    command=carregar  
)
botao_iniciar.pack(pady=30)

janela.mainloop()