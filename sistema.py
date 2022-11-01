import os

import pandas as pd

from functions import *


class Sistema:

    def __init__(self):

        file = "database.xlsx"

        blank = pd.DataFrame(data=[])

        if not os.path.exists(file):
            with pd.ExcelWriter("database.xlsx", mode="w") as writer:
                blank.to_excel(writer, sheet_name="Funcionários")
                blank.to_excel(writer, sheet_name="Livros")
                blank.to_excel(writer, sheet_name="Reservas")
                blank.to_excel(writer, sheet_name="Alunos")

        self.menu()

    @staticmethod
    def menu():

        print("\n(1) Funcionário\n(2) Aluno")

        conta = int(input("Escolha: "))

        match conta:
            case 1:
                print(
                    "\n(1) Cadastrar Funcionário\n(2) Cadastrar Livro\n(3) Registrar Devolução\n(4) Resolver "
                    "Pendências\n")
                opt = int(input("Escolha: "))

                match opt:
                    case 1:
                        cadastrar_funcionario()
                    case 2:
                        cadastrar_livro()
                    case 3:
                        registrar_devolucao()
                    case 4:
                        resolver_pendencias()
                    case _:
                        print("Entrada inválida\n")
            case 2:
                print("(1) Registrar Reserva")
                opt = int(input("Escolha: "))

                match opt:
                    case 1:

                        login = input("Insira seu endereço de email institucional: ")
                        check = checar_dados("Alunos", login)

                        if check:
                            registrar_reserva(login)
                        else:
                            cadastrar_aluno()

                    case _:
                        print("Entrada inválida\n")

        while True:
            Sistema.menu()


sys = Sistema()

Sistema.menu()
