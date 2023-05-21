import json
import string
from cryptography.fernet import Fernet


def armazenar_dados(data, arquivo):
    with open("{}.json".format(arquivo), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def ler_dados(arquivo):
    with open("{}.json".format(arquivo), "r") as f:
        data = json.load(f)
        return data


def inicializar_database():
    data = {
        "Funcionarios": [],
        "Alunos": [],
        "Livros": [],
        "Reservas": []
    }
    armazenar_dados(data, "database")


def inicializar_dewey():
    data = {
        "Codigos":
            {
                "000": "Ciências Computacionais e da Informação",
                "100": "Filosofia e Psicologia",
                "200": "Religião",
                "300": "Ciências Sociais",
                "400": "Linguagem",
                "500": "Ciência",
                "600": "Tecnologia",
                "700": "Artes e Lazer",
                "800": "Literatura",
                "900": "História e Geografia"
            }
    }

    armazenar_dados(data, "dewey")


def inicializar_login():
    key = Fernet.generate_key()

    data = {
        "Funcionarios": [],
        "Alunos": [],
        "Key": str(key)
    }

    armazenar_dados(data, "login")


def checar_dado(tipo, dado, arquivo):
    data = ler_dados(arquivo)[tipo]
    for i in range(len(data)):
        if dado in data[i].values():
            return True

    return False


def recuperar_indice(tipo, dado, arquivo):
    counter = 0

    data = ler_dados(arquivo)[tipo]
    for i in range(len(data)):
        if dado in data[i].values():
            return counter
        else:
            counter += 1


def advertir_usuario(caso):
    if caso == 2:
        print("[!] Senha incorreta")
        print("\n")
    if caso == 1:
        print("[!] A entrada já consta no sistema")
        print("\n")
    if caso == 0:
        print("[!] A entrada não consta no sistema")
        print("\n")


def gerar_numeracao(assunto, autor, titulo):
    listaNumeros = []

    def converter_letras():

        for i in range(3):
            if i == 0:
                numero = str(string.ascii_uppercase.index(autor[i]))
            else:
                numero = str(string.ascii_lowercase.index(autor[i]))

            listaNumeros.append(numero)

            numString = "".join(listaNumeros)

            return numString

    livroID = assunto + autor[0] + converter_letras() + titulo[0].lower()

    return livroID


def gerar_assunto(assunto):
    with open("dewey.json", "r") as f:
        data = json.load(f)

    return data["Codigos"][assunto]


def encrypt_decrypt_senha(senha, caso):
    data = ler_dados("login")
    key = eval(data["Key"])

    crypter = Fernet(key)

    if caso == 1:
        senhaEncriptada = crypter.encrypt(senha)
        return senhaEncriptada
    if caso == 2:
        senhaDecriptada = crypter.decrypt(senha)
        return senhaDecriptada


def login_usuario(area,matricula,senha):
    matriculaUsuario = matricula
    if not checar_dado(area, matriculaUsuario, "login"):
        advertir_usuario(0)
        return False

    data = ler_dados("login")

    senhaUsuario = senha.encode()
    senhaArquivo = data["{}".format(area)][recuperar_indice("{}".format(area), matriculaUsuario, "login")]["Senha"]
    senhaArquivo = encrypt_decrypt_senha(eval(senhaArquivo), 2)

    if senhaUsuario != senhaArquivo:
        advertir_usuario(2)
        return False

    return True

def criar_admin():
    data = ler_dados("login")

    usuarioAdmin = "admin"
    senhaAdmin = "senhaadmin"
    dadosAdmin = {"Matricula": usuarioAdmin, "Senha": str(encrypt_decrypt_senha(senhaAdmin.encode(), 1))}

    data["Funcionarios"].append(dadosAdmin)
    armazenar_dados(data, "login")

def subtrair_item(codigo):
    data = ler_dados("database")

    for i in range(len(data["Livros"])):
        if int(data["Livros"][i]["ID"]) == codigo:
            if data["Livros"][i]["Estoque"] <= 0:
                advertir_usuario(3)
                return False
            else:

                estoque = data["Livros"][i]["Estoque"]
                estoque -= 1
                data["Livros"]["Estoque"][i] = estoque
                armazenar_dados(data, "database")
                return True
