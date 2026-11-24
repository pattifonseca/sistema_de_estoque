lista = []

def cadastrar_produtos():
    produtos = {}
    while True:
        produtos["nome"] = input("Nome do produto: ").strip().capitalize()

        duplicado = False

        for produto in lista:
            if produtos["nome"] == produto["nome"]:
                print("Nome de produto já cadastrado!")
                duplicado = True
                break

        if not duplicado:
            break
    while True:
        produtos["valor"] = float(input("Valor: R$ ").replace(",", "."))
        produtos["qtd"] = int(input("Quantidade: "))
    
        if produtos["valor"] <= 0 or produtos["qtd"] < 0:
                print("Dados inválidos!")
                continue
        break
    
    lista.append(produtos)
    print("Produto cadastrado com sucesso!")
    print()

def listar_produtos(lista):
    if lista == []:
            print("Lista sem produtos cadastrados!")
    else:
        print("="*10, "ESTOQUE", 10*"=")
        print("Produto | Valor | Quantidade")
        for produto in lista:
            print(f"{produto["nome"]}|{produto["valor"]:.2f}|{produto["qtd"]}")
    

def atualizar_estoque(lista, nome , quantidade):
    if quantidade == 0:
        print("A quantidade deve ser diferente de zero.")
        return
    for produto in lista:
        if nome == produto["nome"]:
            if quantidade < 0:
                soma = produto["qtd"] + quantidade
                if soma < 0:
                    print("ERRO. Estoque negativo")
                else:
                    produto["qtd"] = soma
                    print(f"Estoque de {nome} foi atualizado com {quantidade} unidades ficando com {produto["qtd"]} no total")
                    print()
            else:
                produto["qtd"] += quantidade
                print(f"Estoque de {nome} foi atualizado com {quantidade} unidades ficando com  {produto["qtd"]} no total")
                print()


def realizar_vendas(lista,nome,quantidade):
    if quantidade <= 0:
        print("Quantidade inválida.")
        return 0
    produto_encontrado = False
    for produto in lista:
        if nome == produto["nome"]:
            produto_encontrado = True
            if produto["qtd"] < quantidade:
                print(f"Produdo sem estoque disponível para a venda de {quantidade}")
                return 0 
            else:
                produto["qtd"] -= quantidade
                valor = produto["valor"] * quantidade
                return valor
    if not produto_encontrado:
        print("Produto não localizado.")

    return 0 


def consultar_produto(lista,nome):
    produto_encontrado = False
    for produto in lista:
        if nome == produto["nome"]:
            produto_encontrado = True
            print(f"Produto: {nome}",
                 f"\nValor: R${produto["valor"]:.2f}",
                 f"\nEstoque: {produto["qtd"]}")
    if not produto_encontrado:
        print("Produto não localizado")

def relatorio_financeiro(lista):
    qtd_cadastrada = len(lista)
    mais_caro = 0
    maior_qtd = 0
    investimneto = 0
    estoque_menos_5 = 0
    for produto in lista:
        if produto["valor"] > mais_caro:
            mais_caro = produto["valor"]
        if produto["qtd"] > maior_qtd:
            maior_qtd = produto["qtd"]
        if produto["qtd"] < 5:
            estoque_menos_5 +=1
        total = produto["valor"] * produto["qtd"]
        investimneto += total
        
    print("====== Relatório =====")
    print(f"Total de produtos cadastrados:{qtd_cadastrada}",
          f"\nValor total do estoque: R${investimneto:.2f}",
          f"\nProduto com maior estoque: {maior_qtd}",
          f"\nProduto mais caro do estoque: R${mais_caro:.2f}",
          f"\nQuantidade de produtos com estoque inferior a 5 unidades {estoque_menos_5}")
    print()

while True:
    print("="*5, "MENU", 5*"=")
    print("1 - Cadastrar produto",
        "\n2 - Listar protudos",
        "\n3 - Atualizar estoque",
        "\n4 - Realizar venda",
        "\n5 - Consultar produto",
        "\n6 - Relatório financeiro",
        "\n7 - Sair")
    print()

    try:
        opc = int(input("Escolha uma opção: "))
        print()
        if opc == 1:
            cadastrar_produtos()

        elif opc == 2:
            listar_produtos(lista)
            print()

        elif opc == 3 :
            nao_ta_lista = True
            while True:
                nome = str(input("Qual o produto a ser atualizado? ")).strip().capitalize()
                if lista == []:
                    print("Lista sem produtos cadastrados.")
                    break
                
                for produto in lista:
                    if nome == produto["nome"]:
                        quantidade = int(input("Qual a quantidade? "))
                        nao_ta_lista = False
                        atualizar_estoque(lista, nome, quantidade)
                        
                if nao_ta_lista:
                    print("Produto não cadastrado na lista")
                else:
                    break

        elif opc == 4:
            nome = input("Produto a ser vendido? ").strip().capitalize()
            quantidade = int(input("Quantas unidades? "))
            valor_total = realizar_vendas(lista,nome,quantidade)
            print(f"Valor total da venda: R${valor_total:.2f}") 

        elif opc == 5:
            print("Ver produto cadastrado")
            nome = input("Solicite um produto: ").strip().capitalize()
            consultar_produto(lista, nome)
        elif opc == 6:
            relatorio_financeiro(lista)   

        elif opc == 7:
            print("Sistema encerrado")
            break
        else:
            print("Opção inválida!")

    except ValueError:
            print("Dados inválidos. Escolha uma das opções")