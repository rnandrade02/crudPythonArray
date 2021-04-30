# Iniciando estudos em python. projeto de um crud para cadastrar produtos sem banco de dados só com array/list

from functions.funCadastro import *

saidamenu = False

while saidamenu == False:
    print("------- Cadastro de Produtos -------")
    print("\n       ------- Menu -------")
    print("Informe um número para acessar o menu...")
    menu = int(input(
        "1 ---- NOVO PRODUTO \n2 ---- DELETAR  \n3 ---- EDITAR  \n4 ---- PROCURAR \n5 ---- LISTAR TODOS \n6 ---- SAIR\n"))
    if menu == 1:
        cadastroProdutos()
    elif menu == 2:
        deletarProduto()
    elif menu == 3:
        print("Menu")
    elif menu == 4:
        procurarProduto()
    elif menu == 5:
        listarProdutos()
    elif menu == 6:
        saidamenu = True
