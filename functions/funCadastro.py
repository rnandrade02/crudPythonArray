codProduto = []
nomeProduto = []
valorProduto = []
qtdEstoque = []
descProduto = []

def cadastroProdutos():
    continuar = "S"
    while continuar == "S":
        cod = len(codProduto) +1
        codProduto.append(cod)
        print("Código do produto", len(codProduto))
        nomeProduto.append(input("Nome do produto:").upper())
        valorProduto.append(float(input("Valor do produto:")))
        qtdEstoque.append(int(input("Quantidade do produto")))
        descProduto.append(input("Descrição do produto").upper())
        continuar = input("Digite \"S\" para cadastrar um novo produto ou \"N\" para sair: ").upper()


def deletarProduto():
    buscar = input("Qual produto deseja buscar para deletar?").upper()
    for indice in range(0,len(nomeProduto)):
        if buscar == nomeProduto[indice]:
            print("entrou na condicao")
        else:
            print("produto não encontrado")