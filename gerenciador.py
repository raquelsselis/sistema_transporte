import requests

url = "https://jsonplaceholder.typicode.com/posts"

def consultar_post():
    id = int(input("Digite o id:"))
    resposta = requests.get(f"{url}/{id}")

    if resposta.status_code == 200:
        post = resposta.json()

        print("ID:", post["id"])
        print("Usuário:", post["userId"])
        print("Titulo:", post["title"])
        print("Conteúdo:", post["body"])

    else: 
        print("Erro ao acessar a API:", resposta.status_code)


def criar_post():
    usuario = int(input("Digite o id do usuário: "))
    titulo = input("Digite o título: ")
    conteudo = input("Digite o conteúdo: ")

    dados = {
        "userId": usuario,
        "title": titulo,
        "body": conteudo
    }

    resposta = requests.post(url, json=dados)
    
    if resposta.status_code == 201:
        print("Post criado com sucesso!")
    else:
        print("Erro ao criar o post:", resposta.status_code)

def atualizar_post():
    id = int(input("Digite o id do post que deseja atualizar: "))
    titulo = input("Digite o novo título: ")
    conteudo = input("Digite o novo conteúdo: ")

    dados = {
        "id": id,
        "title": titulo,
        "body": conteudo
    }

    resposta = requests.put(f"{url}/{id}", json=dados)
    
    if resposta.status_code == 200:
        print("Post atualizado com sucesso!")
    else:
        print("Erro ao atualizar o post:", resposta.status_code)

def excluir_post():
    id = int(input("Digite o id do post que deseja excluir: "))

    resposta = requests.delete(f"{url}/{id}")
    
    if resposta.status_code == 200:
        print("Post excluído com sucesso!")
    else:
        print("Erro ao excluir o post:", resposta.status_code)


while True:
    print("1. Consultar post")
    print("2. Criar post")
    print("3. Atualizar post")
    print("4. Excluir post")
    print("5. Sair")

    selecao = input("Digite uma opção: ")

    if selecao == "1":
        consultar_post()

    elif selecao == "2":
        criar_post()

    elif selecao == "3":
        atualizar_post()

    elif selecao == "4":
        excluir_post()

    elif selecao == "5":
        print("Encerrando...")
        break
    else:
        print("Opção inválida! Selecione outra do menu")