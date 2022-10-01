import PySimpleGUI as Sg
import pandas as pd

def janela_login():
    Sg.theme("DarkPurple6")
    layout = [
        [Sg.Text("Usuário")],
        [Sg.Input(key='usuario')],
        [Sg.Text("Senha")],
        [Sg.Input(key='senha')],
        [Sg.Button('login',key="login")],
        [Sg.Text('',key='mensagem')]
    ]
    return Sg.Window('Biblioteca', layout=layout, finalize=True, resizable=True)

def janela_opcao():
    Sg.theme("DarkPurple6")
    layout = [
        [Sg.Text('Olá seja bem vindo(a)! O que deseja fazer?', font=('Arial', 25))],
        [Sg.Button('Cadastrar livro', font=('Arial', 20)),
         Sg.Button('Lista de livros', font=('Arial', 20))]
        
    ]
    return Sg.Window('Empresa', layout=layout, finalize=True, resizable=True)

def janela_lista_livros():
    data = pd.read_excel('Livros.xlsx')
    dataframe = pd.DataFrame(data)

    Sg.theme('DarkPurple6')
    layout = [
        [Sg.Text(dataframe)],
        [Sg.Button('Voltar', font=('Arial', 20))]
    ]
    return Sg.Window('Lista de livros', layout=layout, finalize=True, resizable=True)

def janela_cadastro_livro():
    Sg.theme('DarkPurple6')
    layout = [
        [Sg.Text('Nome do livro:'), Sg.Input(key='nome_livro')],
        [Sg.Text('Autor:'), Sg.Input(key='nome_autor')],
        [Sg.Text('Ano:'), Sg.Input(key='ano')],
        [Sg.Text('Código:'), Sg.Input(key='code')],
        [Sg.Button('Continuar'), Sg.Button('Voltar')]
    ]
    return Sg.Window('Livros', layout=layout, finalize=True, resizable=True)


def programa():
    janela_log = janela_login()
    janela_cad = janela_cadastro_livro()
    janela_cad.hide()
    janela_op = janela_opcao()
    janela_op.hide()
    janela_lista = janela_lista_livros()
    janela_lista.hide()
   
    while True:
        
        # Quando a janela for fechada
        window, event, values = Sg.read_all_windows()
        if event == Sg.WIN_CLOSED:
            break
        elif event == "login":
            senha_correta = 'admin'
            usuario_correto = 'admin'
            usuario = values['usuario']
            senha = values['senha']
            if senha == senha_correta and usuario == usuario:
                janela_log.hide()
                janela_op.un_hide()
            if senha != senha_correta and usuario != usuario:
                window['mensagem'].update("Usuário ou senha incorreto")
        if window == janela_op and event =='Cadastrar livro':
                janela_op.hide()
                janela_cad.un_hide()
                
        if window == janela_cad and event =='Voltar':
                janela_cad.hide()
                janela_op.un_hide()
        if window == janela_cad and event == 'Continuar':
            data = pd.read_excel('Livros.xlsx', sheet_name='Livros')
            lista_nome_livro = list(data["Nome do livro"])
            lista_nome_livro.append(values["nome_livro"])
            lista_nome_autor = list(data["Autor"])
            lista_nome_autor.append(values["nome_autor"])
            lista_ano = list(data["Ano"])
            lista_ano.append(values["ano"])
            lista_code = list(data["Código"])
            lista_code.append(values["code"])
            df2 = pd.DataFrame({'Código': lista_code, 'Nome do livro': lista_nome_livro,
                                'Autor': lista_nome_autor, 'Ano': lista_ano})
            with pd.ExcelWriter('Livros.xlsx', mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df2.to_excel(writer, sheet_name="Livros", index=False)
            Sg.popup('Cadastro realizado com sucesso!')
        if window == janela_op and event == 'Lista de livros':
            janela_op.hide()
            janela_lista.un_hide()
        if window == janela_lista and event =='Voltar':
                janela_lista.hide()
                janela_op.un_hide()

            




programa()