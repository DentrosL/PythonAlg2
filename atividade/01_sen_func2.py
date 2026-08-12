# Base de dados (Escopo global do script)
estoque = [
    {"id": 1, "nome": "Notebook", "preco": 3500.0, "qtd": 5},
    {"id": 2, "nome": "Mouse", "preco": 80.0, "qtd": 15},
    {"id": 3, "nome": "Teclado", "preco": 150.0, "qtd": 10}
]
carrinho = []
taxa_imposto_padrao = 0.05  # 5% de taxa padrão

# def exibir_menu():                                # Exibe o menu de opções para o usuário
def exibir_menu():                                  # Entrada: nenhuma
    print("\n" + "=" * 30)                          # Saída: opção escolhida pelo usuário
    print("      SISTEMA DE ESTOQUE      ")
    print("=" * 30)
    print("1. Listar Produtos")
    print("2. Adicionar ao Carrinho")
    print("3. Exibir Carrinho e Total")
    print("4. Cadastrar Novo Produto")
    print("0. Sair")

    opcao = input("\nEscolha uma opção: ")

    return opcao                                    

# def listar_produtos()                             # Listagem de produtos já cadastrados no sistema
def listar_produtos(estoque):                       # Entrada: variável global estoque
    print("\n--- PRODUTOS DISPONÍVEIS ---")         # Saída: nenhuma, apenas exibe os produtos 
    if not estoque:
        print("Estoque vazio.")
    else:
        for item in estoque:
            print(f"ID: {item['id']} | "f"Nome: {item['nome']} | "f"Preço: R$ {item['preco']:.2f} | "f"Estq: {item['qtd']}")

# def add_carrinho()                                # Adicionar item ao carrinho
def add_carrinho(estoque, carrinho):                # Entrada: estoque e carrinho
    print("\n--- ADICIONAR AO CARRINHO ---")        # Saída: nenhuma (altera estoque e carrinho)
    id_busca = input("Digite o ID do produto: ")
    
    # Validação simples se é número
    if id_busca.isdigit():
        id_busca = int(id_busca)
        produto_encontrado = None
        
        # Busca manual no estoque
        for item in estoque:
            if item["id"] == id_busca:
                produto_encontrado = item
                break
        
        if produto_encontrado:
            qtd_desejada = input(f"Quantidade desejada de '{produto_encontrado['nome']}': ")
            if qtd_desejada.isdigit():
                qtd_desejada = int(qtd_desejada)
                
                if qtd_desejada > 0 and qtd_desejada <= produto_encontrado["qtd"]:
                    # Atualiza estoque e adiciona ao carrinho
                    produto_encontrado["qtd"] -= qtd_desejada
                    
                    # Verifica se já está no carrinho para somar a quantidade
                    no_carrinho = False
                    for item_c in carrinho:
                        if item_c["id"] == produto_encontrado["id"]:
                            item_c["qtd"] += qtd_desejada
                            no_carrinho = True
                            break
                    
                    if not no_carrinho:
                        carrinho.append({
                            "id": produto_encontrado["id"],
                            "nome": produto_encontrado["nome"],
                            "preco": produto_encontrado["preco"],
                            "qtd": qtd_desejada
                        })
                    
                    print(f"Sucesso: {qtd_desejada}x '{produto_encontrado['nome']}' adicionado(s) ao carrinho!")
                else:
                    print("Erro: Quantidade indisponível no estoque.")
            else:
                print("Erro: Quantidade inválida.")
        else:
            print("Erro: Produto não encontrado.")
    else:
        print("Erro: ID deve ser um número inteiro.")

# def mostrar_carrinho()                            # Visualizar itens do carrinho
def mostrar_carrinho(carrinho, taxa_imposto_padrao):# Entrada: carrinho e taxa
    print("\n--- SEU CARRINHO ---")                 # Saída: retorna o total final

    if not carrinho:
        print("O carrinho está vazio.")
        return 0

    subtotal = 0.0

    for item in carrinho:
        total_item = item["preco"] * item["qtd"]
        subtotal += total_item

        print(
            f"- {item['nome']} "
            f"(x{item['qtd']}): "
            f"R$ {total_item:.2f}"
        )

    aplicar_taxa = input("\nDeseja aplicar taxa de entrega/serviço customizada? (s/N): ").strip().lower()
    taxa_aplicada = taxa_padrao

    if aplicar_taxa == "s":
        val_taxa = input("Digite a taxa decimal (ex: 0.10 para 10%): ")
        try:
            taxa_aplicada = float(val_taxa)
        except ValueError:
            print("Valor inválido. Mantendo taxa padrão de 5%.")

    valor_imposto = subtotal * taxa_aplicada
    total_final = subtotal + valor_imposto

    print("-" * 30)
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Taxa ({taxa_aplicada * 100:.1f}%): R$ {valor_imposto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

    return total_final

# def add_produto()                                 # Adicionar novo item ao estoque
def add_produto(estoque):                           # Entrada: estoque
    print("\n--- CADASTRO DE PRODUTO ---")          # Saída: retorna o novo produto cadastrado

    nome_novo = input("Nome do produto: ").strip()
    preco_novo = input("Preço do produto: ")
    qtd_nova = input("Quantidade inicial em estoque: ")

    try:
        preco_novo = float(preco_novo)
        qtd_nova = int(qtd_nova)

        if not nome_novo or preco_novo <= 0 or qtd_nova < 0:
            print("Erro: Dados inválidos para o produto.")
            return None

        novo_id = 1

        if estoque:
            novo_id = max(item["id"] for item in estoque) + 1

        novo_produto = {"id": novo_id,"nome": nome_novo,"preco": preco_novo,"qtd": qtd_nova}
        estoque.append(novo_produto)

        print(f"Produto '{nome_novo}' cadastrado " f"com sucesso! ID: {novo_id}")

        return novo_produto

    except ValueError:
        print("Erro: Preço e Quantidade devem ser numéricos.")
        return None

executando = True

while executando:
    exibir_menu()

    if opcao == "1":
        listar_produtos(estoque)
    elif opcao == "2":
        add_carrinho(estoque, carrinho)
    elif opcao == "3":
        mostrar_carrinho(carrinho, taxa_imposto_padrao)
    elif opcao == "4":
        add_produto(estoque)
    elif opcao == "0":
        print("\nEncerrando o sistema. Até logo!")
        executando = False
    else:
        print("\nOpção inválida! Tente novamente.")