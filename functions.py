from datetime import datetime, timedelta
#import yagmail
import pandas as pd
import string
import random


def checar_estoque(code, qtd):
    data = pd.read_excel("database.xlsx", index_col=0, sheet_name="Livros")

    for i in range(len(data.columns)):

        if i == len(data.columns):
            break

        if code in list(data[i]):

            if data[i][5] < qtd:
                print("[!] A quantidade excede o estoque do produto")
                return False

            else:
                return True


def checar_dados(workbook, entrada):
    data = pd.read_excel("database.xlsx", index_col=0, sheet_name=workbook)

    counter = 0

    for i in range(len(data.columns)):

        if i == len(data.columns):
            break

        if entrada in list(data[i]):
            counter += 1
            return True

    if counter == 0:
        return False

def checar_login(workbook, email,senha):
    data = pd.read_excel("database.xlsx", index_col=0, sheet_name=workbook)

    counter = 0

    for i in range(len(data.columns)):

        if i == len(data.columns):
            break

        if email and senha in list(data[i]):
            counter += 1
            return True

    if counter == 0:
        return False

def subtrair_item(dic):
    data = pd.read_excel("database.xlsx", index_col=0, sheet_name="Livros")

    for i in range(len(dic)):

        for j in range(len(data.columns)):

            if j == len(data.columns):
                break

            if list(dic.keys())[i] in list(data[j]):
                data[j][5] = data[j][5] - dic[list(dic.keys())[0]]

    with pd.ExcelWriter("database.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:

        data.to_excel(writer, sheet_name="Livros")


def writeto_excel(workbook, dados):
    data = pd.read_excel("database.xlsx", engine="openpyxl", index_col=0, sheet_name=workbook)

    if len(data.columns) == 0:

        data[0] = dados

    else:

        data[data.columns[-1] + 1] = dados

    with pd.ExcelWriter("database.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:

        data.to_excel(writer, sheet_name=workbook)


def cadastrar_funcionario(lista,matricula):

    info = lista

    check = checar_dados("Funcionários", matricula)

    if check:
        print("Elemento já cadastrado\n")
        return

    writeto_excel("Funcionários", info)


def cadastrar_aluno(lista,matricula):
    info = lista

    check = checar_dados("Alunos", matricula)

    if check:
        print("Elemento já cadastrado\n")
        return

    writeto_excel("Alunos", info)

def gerar_numeracao(assunto, autor, titulo):
    listaNumeros = []

    def converter_letras():

        for i in range(3):

            if i == 0:

                numero = str(string.ascii_uppercase.index(autor[i]))

            else:

                numero = str(string.ascii_lowercase.index(autor[i]))

            listaNumeros.append(numero)

        numerosString = "".join(listaNumeros)

        return numerosString

    return assunto + autor[0] + converter_letras() + titulo[0].lower()

def gerar_assunto(assunto):
    dewey = {
        "000": "Ciências Computacionais e da Informação",
        "100": "Filosofia e Psicologia",
        "200": "Religião",
        "300": "Ciências Sociais",
        "400": "Linguagem",
        "500": "Ciência",
        "600": "Tecnologia",
        "700": "Artes e Lazer",
        "800": "Literatura",
        "900": "História e Geografia",
    }

    return dewey[assunto]

def cadastrar_livro(codigo,titulo, ano, assunto, autor, editora, estoque):
    #codigo = gerar_numeracao(assunto, autor, titulo)

    #codigo = gerar_numeracao(assunto, autor, titulo)

    info = [codigo, titulo, ano,assunto, autor, editora, estoque]

    check = checar_dados("Livros", codigo)

    if check:
        print("Elemento já cadastrado\n")
        return

    writeto_excel("Livros", info)


def registrar_reserva(email,codigoLivro):

    dicItem = {}

    #check = checar_dados("Livros", codigoLivro)

    #if check == False:
    #    print("[!] A entrada não consta no banco de dados")
    #    return

    #check = checar_estoque(codigoLivro, 1)

    #if not check:
    #    return

    #dicItem[codigoLivro] = 1

    codigoReserva = "%016x" % random.getrandbits(64)

    dataLimite = datetime.today() + timedelta(7)
    dataLimite = datetime.strftime(dataLimite, "%d/%m/%y")

    devolvido = 0

    info = [codigoReserva, email, dataLimite, str(dicItem), devolvido]

    writeto_excel("Reservas", info)

    subtrair_item(dicItem)


def comunicar_aluno(email):
    user = 'engenhariadesoftwareprojeto@gmail.com'
    app_password = 'kkurogbllninuxxb'
    to = email

    subject = 'Lembrete - Devolução de Livro Emprestado'
    content = ['Caro (a) aluno (a). Esta mensagem tem como objetivo comunicar que o'
               ' seu empréstimo da obra está próximo de vencer. Evite multas, devolvendo o recurso '
               ' à biblioteca assim que possível.']

    #with yagmail.SMTP(user, app_password) as yag:
        #yag.send(to, subject, content)
        #print("Aluno comunicado com sucesso")

#def verificar_atraso():
