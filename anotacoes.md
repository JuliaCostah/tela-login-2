# - cria titulos
* - listas com marcadores
** ** deixa em negrito
''' cria blocos de códigos
_________________________________________

# 1° Parte - Criar a Janela
 
 . Escolher um tema para janela - dark,ligth or System
    
        ctk.set_appearance_mode()

 . Posso escolher uma paleta de cores para os elementos interativos -
        blue , green or dark-blue

        ctk.set_default_color_theme()

 .  Criar a janela 

        ctk.CTk()

        janela.title()
        janela.geometry()

        .mainloop()

# 2° Parte - Dividir a tela em parte lateral e parte Central

 .  Minha janela terá duas colunas(lateral e central) e uma única
    linha.
    Para fazer isso pode usar o metódo .grid() que transforma a janela
    em uma "tabela do excel" com linhas(rows) e colunas(columns).

        janela.grid_columnconfigure()
        janela.grid_rowconfigure()

 .  O weight() é o peso, ou seja, ele  define a regra de quem fica
    com o espaço sobrante caso a janela seja esticada ou redimensionada. Por padrão, as linhas e colunas tem weigth=0.
    Ficam **fixas** do tamanho exato dos elementos que estão nela.
    Se o weight=1 a linha ou coluna expande junto com a tela. 
    painel lateral -> linha 0, coluna 0
    painel central -> linha 0, coluna 1

        janela.grid_columnconfigure(1, weight=1)
        janela.grid_rowconfigure(0, weigth=1)

# 3° Parte - Criar as barra lateral e a Aba central

 .  Na parte lateral:
    Criar um **Frame**, pois quero que ela seja fixa.

 .  1° -> passar para o frame a janela e a largura(width=) dele.
    No caso, como eu tenho uma largura total de 900px, o meu frame irá receber 200px.
    2° -> Informar onde o frame vai ficar na janela. 
    row=0 e column=0

        barra_lateral = ctk.CTkFrame(
            janela,width=200
        )
        barra_lateral.grid(row=0,column=0)

 .  Aba central:
    Criar um **TabView**, pois dentro dele eu vou ter 3 abas.

 .  1° -> mesmas coisas do frame, porém a largura dele será de 400px, e vai sobrar    300px da largura total que será preenchido automaticamente pelo TabView por causa do weigth=1. Logo, o TabView terá uma largura de 700px.

 .  2° -> Informar onde o TabView vai ficar na janela. 
    row=0 e column=1

        parte_central = ctk.CTkTabview(
            janela,width=400
        )

        parte_central.grid(row=0,column=1,sticky='nsew',padx=10)

# 4° Parte - Colocar os elementos no frame

 .  Vou precisar de um Label, um botão principal e um switch.

    Para o botão:

        botao_principal = ctk.CTkButton(
        barra_lateral,
        text='Dashboard Principal',
        font=('Cascadia Code',18,'bold'),
        corner_radius=10, **É o arredondamento dos cantos**
        border_width=2, **Espessura da borda**
        border_color="#4F052A",   **Cor da borda**
        fg_color="#B21463",   **Cor do botão**
        cursor='hand2',     **Como o cursor fica no botão**
        hover_color= "#810C46" **Cor ao passar o cursor no botão
        )
        botao_principal.pack(pady=(40,20),padx=(20,20))

    Para o switch (alterna entre [Ativado/Desativado]):

        switch_mododark = ctk.CTkSwitch(
            barra_lateral,
            text='Modo Escuro',
            font=('Cascadia Code',18),
            )
        switch_mododark.pack(side='bottom',pady=(0,40))  **O side= é onde eu 
        quero o meu elemento.

# 5° Parte - Dentro da Parte central preciso de 3 abas.

 .  **1° Aba** -> Perfil
    Vou precisar de:
        . Campo de nome (usa um .tab('Perfil') e um CTkEntry)
        . Radio Button de nível de usuário (botão que só pode escolher uma opção)
            . Uso um ctk.IntVar(value=0), ela monitora os botões e guarda a escolha
            do usuário.
            . Se os dois botões compartilham a mesma variable=nivel_usuario eles  estão conectados.
        . checkbox de notificações
            . Uso ctk.CTkCheckBox()
        . botão salvar perfil




