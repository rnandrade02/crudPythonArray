codProduto = []
nomeProduto = []
valorProduto = []
qtdEstoque = []
descProduto = []


def cadastroProdutos():
    continuar = "S"
    while continuar == "S":
        cod = len(codProduto) + 1
        codProduto.append(cod)
        print("Código do produto", len(codProduto))
        nomeProduto.append(input("Nome do produto:").upper())
        valorProduto.append(float(input("Valor do produto:")))
        qtdEstoque.append(int(input("Quantidade do produto")))
        descProduto.append(input("Descrição do produto").upper())
        continuar = input("Digite \"S\" para cadastrar um novo produto ou \"N\" para sair: ").upper()
        print("____________________________________________________________")


def deletarProduto():
    buscar = input("Qual produto deseja buscar para deletar?").upper()
    for indice in range(0, len(nomeProduto)):
        if buscar == nomeProduto[indice]:
            print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
                  "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
            deletar = input("Digite \"S\" para deletar ou \"N\" para sair: ").upper()
            if deletar == 'S':
                del codProduto[indice], valorProduto[indice], qtdEstoque[indice], descProduto[indice], nomeProduto[
                    indice]
            print("Produto Deletado")
            break
        else:
            print("produto não encontrado")


def editarProduto():
    buscar = input("Qual produto deseja buscar para editar?").upper()
    for indice in range(0, len(nomeProduto)):
        if buscar == nomeProduto[indice]:
            print("Deseja Editar Esse Item?")
            print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
              "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
            resposta = input("Digite \"S\" para EDITAR ou \"N\" para SAIR: ").upper()

            editar = int(input(
                "---- Edidar ----\n1 ---- Nome \n2 ---- Valor  \n3 ---- Estoque  \n4 ---- Descrição\n5 ---- Sair"))
            if (editar == 1):
                nomeProduto.pop(indice)
                nomeProdutoEdit = input("Nome do produto:").upper()
                nomeProduto.insert(indice, nomeProdutoEdit)

            if (editar == 2):
                valorProduto.pop(indice)
                valorprodutoedit = float(input("Valor do produto:"))
                valorProduto.insert(indice, valorprodutoedit)

            if (editar == 3):
                qtdEstoque.pop(indice)
                qtdEstoqueEdit = int(input("Quantidade do produto"))
                qtdEstoque.insert(indice, qtdEstoqueEdit)

            if (editar == 4):
                descProduto.pop(indice)
                descProdutoEdit = input("Nome do produto:").upper()
                descProduto.insert(indice, descProdutoEdit)

            if (editar == 5):
                loop = False


def procurarProduto():
    buscar = input("Qual produto deseja buscar: ").upper()
    for indice in range(0, len(codProduto)):
        if buscar == nomeProduto[indice]:
            print("_____________________________")
            print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
                  "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
            print("_____________________________")
            break



def listarProdutos():
    for indice in range(0, len(nomeProduto)):
        print("_____________________________")
        print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
              "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
        print("_____________________________")
