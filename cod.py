# Sistema de Cadastro de Jogos
jogos = []

def cadastrar_jogo():
    print("\n=== Cadastro de Novo Jogo ===")
    titulo = input("Título do jogo: ")
    genero = input("Gênero: ")
    ano = input("Ano de lançamento: ")
    plataforma = input("Plataforma: ")
    
    jogo = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "plataforma": plataforma
    }
    jogos.append(jogo)
    print(f"Jogo '{titulo}' cadastrado com sucesso!")

def listar_jogos():
    if not jogos:
        print("\nNenhum jogo cadastrado ainda.")
        return
    
    print("\n=== Lista de Jogos ===")
    for i, jogo in enumerate(jogos, 1):
        print(f"{i}. Título: {jogo['titulo']}")
        print(f"   Gênero: {jogo['genero']}")
        print(f"   Ano: {jogo['ano']}")
        print(f"   Plataforma: {jogo['plataforma']}")
        print("--------------------")

def buscar_jogo():
    if not jogos:
        print("\nNenhum jogo cadastrado para buscar.")
        return
    
    termo = input("\nDigite o título do jogo para buscar: ").lower()
    encontrados = [jogo for jogo in jogos if termo in jogo['titulo'].lower()]
    
    if not encontrados:
        print("Nenhum jogo encontrado com esse título.")
    else:
        print("\n=== Jogos Encontrados ===")
        for jogo in encontrados:
            print(f"Título: {jogo['titulo']}")
            print(f"Gênero: {jogo['genero']}")
            print(f"Ano: {jogo['ano']}")
            print(f"Plataforma: {jogo['plataforma']}")
            print("--------------------")

def remover_jogo():
    if not jogos:
        print("\nNenhum jogo cadastrado para remover.")
        return
    
    listar_jogos()
    try:
        indice = int(input("Digite o número do jogo a remover: ")) - 1
        if 0 <= indice < len(jogos):
            jogo_removido = jogos.pop(indice)
            print(f"Jogo '{jogo_removido['titulo']}' removido com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Por favor, digite um número válido!")

def menu():
    while True:
        print("\n=== Sistema de Cadastro de Jogos ===")
        print("1. Cadastrar novo jogo")
        print("2. Listar todos os jogos")
        print("3. Buscar jogo por título")
        print("4. Remover jogo")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            cadastrar_jogo()
        elif opcao == "2":
            listar_jogos()
        elif opcao == "3":
            buscar_jogo()
        elif opcao == "4":
            remover_jogo()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    menu()
