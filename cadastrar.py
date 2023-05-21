from functions import *


def cadastrar_funcionario(matriculaFuncionario,nomeFuncionario):

    if checar_dado("Funcionarios", matriculaFuncionario, "database"):
        advertir_usuario(1)
        return

    dadosFuncionario = {"Matricula": matriculaFuncionario, "Nome": nomeFuncionario}
    data = ler_dados("database")

    data["Funcionarios"].append(dadosFuncionario)
    armazenar_dados(data, "database")


def cadastrar_aluno(matriculaAluno,emailAluno,senhaAluno):

    if checar_dado("Alunos", matriculaAluno, "database"):
        advertir_usuario(1)
        return

    dadosAluno = {"Matricula": matriculaAluno, "Email": emailAluno}
    data = ler_dados("database")
    data["Alunos"].append(dadosAluno)
    armazenar_dados(data, "database")

    dadosAluno = {"Matricula": matriculaAluno, "Senha": str(encrypt_decrypt_senha(senhaAluno.encode(), 1))}
    data = ler_dados("login")
    data["Alunos"].append(dadosAluno)
    armazenar_dados(data, "login")


def cadastrar_livro(codigoLivro,tituloLivro,assuntoLivro, anoLivro,autorLivro,editoraLivro,estoqueLivro):

    if checar_dado("Livros", codigoLivro, "database"):
        advertir_usuario(1)
        return

    dadosLivro = {
        "ID": codigoLivro,
        "Titulo": tituloLivro,
        "Assunto": assuntoLivro,
        "Ano": anoLivro,
        "Autor": autorLivro,
        "Editora": editoraLivro,
        "Estoque": estoqueLivro
    }

    data = ler_dados("database")

    data["Livros"].append(dadosLivro)
    armazenar_dados(data, "database")


def cadastrar_reserva(matriculaAluno,codigo):
    if not checar_dado("Alunos", matriculaAluno, "database"):
        advertir_usuario(0)
        return

    dadosReserva = {"Matricula": matriculaAluno, "Livro": codigo}
    data = ler_dados("database")
    data["Reservas"].append(dadosReserva)
    armazenar_dados(data, "database")

#login_usuario("Alunos")