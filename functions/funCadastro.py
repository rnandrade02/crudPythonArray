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
                del codProduto[indice],valorProduto[indice],qtdEstoque[indice],descProduto[indice],nomeProduto[indice]
            print("Produto Deletado")
            break
        else:
            print("produto não encontrado")


def procurarProduto():
    buscar = input("Qual produto deseja buscar: ").upper()
    for indice in range(0, len(codProduto)):
        if buscar == nomeProduto[indice]:
            print("_____________________________")
            print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
                  "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
            print("_____________________________")
            continuar = input()


def listarProdutos():
    for indice in range(0, len(nomeProduto)):
        print("_____________________________")
        print("Código: ", codProduto[indice], "\nNome:", nomeProduto[indice], "\nR$:", valorProduto[indice],
              "\nEstoque:", qtdEstoque[indice], "\nDescrição:", descProduto[indice])
        print("_____________________________")
