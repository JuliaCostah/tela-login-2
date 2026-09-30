import customtkinter as ctk

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

botao_principal = ctk.CTkButton(
    barra_lateral,
    text='Dashboard Principal',
    font=('Cascadia Code',18,'bold'),
    corner_radius=10,
    border_width=2,
    border_color="#0C090A",
    fg_color="transparent",
    cursor='hand2',
    hover_color= "#B5085F"
    )
botao_principal.pack(pady=(40,20),padx=(20,20))

switch_mododark = ctk.CTkSwitch(
    barra_lateral,
    text='Modo Escuro',
    font=('Cascadia Code',18),
)
switch_mododark.pack(side='bottom',pady=(0,40))

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
janela_abas.add('Preferências')
janela_abas.add('Dashboard')
#--------------------------------------------------
# Primeira aba

aba_perfil = janela_abas.tab('Perfil')

campo_nome = ctk.CTkEntry(
    aba_perfil,
    placeholder_text='Informe seu nome completo',
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
    value=1
)
radio_basico.pack(anchor='w',padx=(220,0),pady=(10,10))

radio_admin = ctk.CTkRadioButton(
    aba_perfil,
    text='Administrador',
    font=('Cascadia Code',16,'bold'),                        
    variable=nivel_usuario,
    value=2
)
radio_admin.pack(anchor='w',padx=(220,0),pady=(10,10))

checkbox_notificacoes = ctk.CTkCheckBox(
    aba_perfil,
    text='Receber notificações por e-mail',
    font=('Cascadia Code',16,'bold'),                        
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
    hover_color= "#B5085F"          
)
botao_salvar_perfil.pack(pady=(30,30))


janela.mainloop()