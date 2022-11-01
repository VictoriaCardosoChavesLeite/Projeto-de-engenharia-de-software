from contextlib import redirect_stderr
from flask import Flask, request, render_template # Importa a biblioteca
from functions import *

app = Flask(__name__) # Inicializa a aplicação

@app.route('/')
def login():
  email = request.args.get('email')
  senha = request.args.get('password')
  checa_aluno = checar_login('Alunos',email,senha)
  checa_func = checar_login('Funcionários',email,senha)

  if checa_aluno == True or checa_func == True:
    return app.redirect("/pagina_inicial.html")

  

  return render_template("pagina_login.html")

@app.route('/pagina_inicial.html')
def inicial():
  return render_template("pagina_inicial.html")

@app.route('/pagina_reserva_livro.html')
def reservar():

  codigo = request.args.get('codigo')
  email = request.args.get('email')

  registrar_reserva(email,codigo)

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

  cadastrar_livro(codigo,titulo, ano, assunto, autor, editora, estoque)
  return render_template("pagina_cadastro_livro.html")

@app.route('/pagina_cadastro.html') # Nova rota
def cadastro():
    database = list()

    matricula = request.args.get('matricula')
    nome = request.args.get('nome')
    email = request.args.get('email')
    senha = request.args.get('password')
    cargo = request.args.get('cargo')

    database.append(nome)
    database.append(email)
    database.append(senha)
    database.append(cargo)

    if(cargo == 'Aluno'):
      cadastrar_aluno(database,matricula)

    elif(cargo == 'Funcionário'):
      cadastrar_funcionario(database,matricula)


    return  render_template("pagina_cadastro.html")

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação