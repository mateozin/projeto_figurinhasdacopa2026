from figurinha import *
from album import *
from historico import *
from persistencia import *
import os
import random


TOTAL_FIGURINHAS = 670
album_usuario = Album(TOTAL_FIGURINHAS)
album_amigo = Album(TOTAL_FIGURINHAS)
historico = Historico()


def pausa():
    escolha = input("Pressione Enter para continuar ou digite L para limpar o console: ")

    if escolha.lower() == "l":
        os.system("cls" if os.name == "nt" else "clear")


def ver_id(texto="ID da figurinha: "):
    while True:
        try:
            id = int(input(texto))
        except ValueError:
            print("Isso não é um ID válido.")
            continue

        if id <= 0:
            print("ID deve ser maior que zero.")
            continue

        return id


def ver_quantidade():
    while True:
        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Isso não é uma quantidade válida.")
            continue

        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            continue

        return quantidade


def escolher_album():
    print("1- Seu álbum")
    print("2- Álbum do amigo")

    try:
        escolha = int(input("Escolha o álbum: "))
    except ValueError:
        print("Isso não é uma opção válida.")
        return None, None

    if escolha == 1:
        return album_usuario, "seu álbum"
    if escolha == 2:
        return album_amigo, "álbum do amigo"

    print("Álbum inválido.")
    return None, None


def criar_figurinha():
    id = ver_id()
    nome = input("Nome do jogador: ")
    pais = input("Seleção/País: ")
    posicao = input("Posição: ")
    raridade = input("Raridade comum/especial/lendaria: ")

    return Figurinha(id, nome, pais, posicao, raridade)


def adicionar_aleatorias(album, quantidade):
    nomes = ["Neymar", "Messi", "Cristiano Ronaldo", "Mbappe", "Vini Jr", "Haaland", "Modric", "Salah"]
    paises = ["Brasil", "Argentina", "Portugal", "França", "Noruega", "Croácia", "Egito", "Espanha"]
    posicoes = ["Goleiro", "Zagueiro", "Lateral", "Meio-campo", "Atacante"]
    raridades = ["comum", "especial", "lendaria"]

    for _ in range(quantidade):
        id = random.randint(1, TOTAL_FIGURINHAS)
        nome = random.choice(nomes)
        pais = random.choice(paises)
        posicao = random.choice(posicoes)
        raridade = random.choice(raridades)
        album.adicionar(Figurinha(id, nome, pais, posicao, raridade))


menu = """
MENU PRINCIPAL
1- Adicionar figurinha ao álbum
2- Remover figurinha do álbum
3- Consultar figurinha por número
4- Buscar figurinha por jogador
5- Buscar figurinha por seleção
6- Ver álbum completo
7- Ver figurinhas repetidas
8- Ver porcentagem concluída e status
9- Registrar proposta de troca
10- Exibir propostas de troca
11- Efetuar próxima troca automática
12- Exibir histórico de trocas
13- Gerar figurinhas aleatórias
14- Salvar álbum em JSON
15- Carregar álbum em JSON
0- Sair
"""

while True:
    print(menu)

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Isso não é um número válido.")
        escolha = -1

    if escolha == 1:
        print("OK! Escolha o álbum e depois digite os dados da figurinha.")
        album, nome_album = escolher_album()

        if album is not None:
            try:
                figurinha = criar_figurinha()
                print(album.adicionar(figurinha))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 2:
        print("OK! Escolha o álbum e digite o ID da figurinha que deseja remover.")
        album, nome_album = escolher_album()

        if album is not None:
            try:
                id = ver_id()
                print(album.remover(id))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 3:
        print("OK! Escolha o álbum e digite o ID da figurinha.")
        album, nome_album = escolher_album()

        if album is not None:
            try:
                id = ver_id()
                print(album.consultar(id))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 4:
        print("OK! Escolha o álbum e digite o nome do jogador.")
        album, nome_album = escolher_album()

        if album is not None:
            try:
                nome = input("Nome do jogador: ")
                print(album.buscar_por_jogador(nome))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 5:
        print("OK! Escolha o álbum e digite a seleção.")
        album, nome_album = escolher_album()

        if album is not None:
            try:
                selecao = input("Seleção: ")
                print(album.buscar_por_selecao(selecao))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 6:
        print("OK! Escolha qual álbum deseja ver.")
        album, nome_album = escolher_album()

        if album is not None:
            print(album.ver_album_completo())

        pausa()

    elif escolha == 7:
        print("OK! Escolha qual álbum deseja ver.")
        album, nome_album = escolher_album()

        if album is not None:
            print(album.listar_repetidas())

        pausa()

    elif escolha == 8:
        print("OK! Escolha qual álbum deseja ver.")
        album, nome_album = escolher_album()

        if album is not None:
            print(album.status())

        pausa()

    elif escolha == 9:
        print("OK! Registrando proposta de troca entre seu álbum e o álbum do amigo.")
        try:
            id_usuario = ver_id("ID repetido que você oferece: ")
            id_amigo = ver_id("ID repetido que o amigo oferece: ")
            print(historico.registrar_proposta_troca("Você", album_usuario, id_usuario, "Amigo", album_amigo, id_amigo))
        except ValueError as erro:
            print(erro)

        pausa()

    elif escolha == 10:
        print("OK! Mostrando propostas de troca.")
        print(historico.mostrar_propostas())
        pausa()

    elif escolha == 11:
        print("OK! Tentando fazer a próxima troca da fila.")
        print(historico.efetuar_troca_automatica())
        pausa()

    elif escolha == 12:
        print("OK! Mostrando histórico de trocas.")
        print(historico.mostrar_historico())
        pausa()

    elif escolha == 13:
        print("OK! Escolha o álbum e a quantidade de figurinhas aleatórias.")
        album, nome_album = escolher_album()

        if album is not None:
            quantidade = ver_quantidade()
            adicionar_aleatorias(album, quantidade)
            print(f"{quantidade} figurinhas criadas em {nome_album}.")

        pausa()

    elif escolha == 14:
        print("OK! Escolha qual álbum deseja salvar.")
        album, nome_album = escolher_album()

        if album is not None:
            nome_arquivo = input("Nome do arquivo para salvar: ")
            if not nome_arquivo.strip():
                nome_arquivo = "album.json"

            try:
                print(salvar_album(album, nome_arquivo))
            except ValueError as erro:
                print(erro)

        pausa()

    elif escolha == 15:
        print("OK! Escolha onde carregar o álbum.")
        print("1- Carregar no seu álbum")
        print("2- Carregar no álbum do amigo")

        try:
            opcao_album = int(input("Escolha: "))
        except ValueError:
            print("Isso não é uma opção válida.")
            opcao_album = -1

        if opcao_album == 1 or opcao_album == 2:
            nome_arquivo = input("Nome do arquivo para carregar: ")
            if not nome_arquivo.strip():
                nome_arquivo = "album.json"

            try:
                album_carregado = carregar_album(nome_arquivo)

                if opcao_album == 1:
                    album_usuario = album_carregado
                    print("Seu álbum foi carregado.")
                else:
                    album_amigo = album_carregado
                    print("Álbum do amigo foi carregado.")
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            except ValueError as erro:
                print(erro)
        else:
            print("Álbum inválido.")

        pausa()

    elif escolha == 0:
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
        pausa()
