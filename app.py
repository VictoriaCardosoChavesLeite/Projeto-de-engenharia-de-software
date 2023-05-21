from contextlib import redirect_stderr
from flask import Flask, render_template, request, redirect, session, flash, url_for
from cadastrar import cadastrar_aluno, cadastrar_funcionario, cadastrar_livro, cadastrar_reserva 
from functions import *

app = Flask(__name__) # Inicializa a aplicação
app.secret_key = 'flask'

@app.route('/')
def login():
  email = request.args.get('email')
  senha = request.args.get('password')
  checa_aluno = login_usuario('Alunos',email,senha)
  checa_func = login_usuario('Funcionarios',email,senha)

  if checa_aluno == True or checa_func == True:
    return render_template("/pagina_inicial.html")
  else:
    #caso as credenciais não sejam validadas, exibe mensagem de erro e redirecion para o login
    flash('Acesso negado, digite novamente!')


  return render_template("pagina_login.html")

@app.route('/pagina_inicial.html')
def inicial():
  flash('Bem vindo!')
  return render_template("pagina_inicial.html")

@app.route('/pagina_reserva_livro.html')
def reservar():
  codigo = request.args.get('codigo')
  matricula = request.args.get('email')
  
  cadastrar_reserva(matricula,codigo)
  subtrair_item(codigo)
  return render_template("/pagina_reserva_livro.html")

@app.route('/pagina_cadastro_livro.html')
def cadastro_livro():
  codigo = request.args.get('codigo')
  titulo = request.args.get('titulo')
  ano = request.args.get('ano')
  assunto = request.args.get('assunto')
  autor = request.args.get('autor')
  editora = request.args.get('editora')
  estoque = request.args.get('estoque')

  cadastrar_livro(codigo,titulo, assunto,ano, autor, editora, estoque)
  return render_template("pagina_cadastro_livro.html")

@app.route('/pagina_cadastro.html') # Nova rota
def cadastro():
    matricula = request.args.get('matricula')
    nome = request.args.get('nome')
    email = request.args.get('email')
    senha = request.args.get('password')
    cargo = request.args.get('cargo')

    if(cargo == 'Aluno'):
      cadastrar_aluno(matricula,email,senha)

    elif(cargo == 'Funcionário'):
      cadastrar_funcionario(matricula,nome)


    return  render_template("pagina_cadastro.html")

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação