import json
from album import Album
from figurinha import Figurinha


def _nome_json(nome_arquivo):
    if not nome_arquivo.strip():
        nome_arquivo = "album.json"

    if not nome_arquivo.endswith(".json"):
        nome_arquivo += ".json"

    return nome_arquivo


def figurinha_para_dict(figurinha):
    return {
        "id": figurinha.id,
        "nome": figurinha.nome,
        "pais": figurinha.pais,
        "posicao": figurinha.posicao,
        "raridade": figurinha.raridade
    }


def dict_para_figurinha(dados):
    return Figurinha(
        int(dados["id"]),
        dados["nome"],
        dados["pais"],
        dados["posicao"],
        dados["raridade"]
    )


def lista_encadeada_para_lista(inicio):
    dados = []
    atual = inicio

    while atual is not None:
        dados.append(figurinha_para_dict(atual.figurinha))
        atual = atual.proximo

    return dados


def salvar_album(album, nome_arquivo="album.json"):
    if not isinstance(album, Album):
        raise ValueError("Isso não é um álbum.")

    nome_arquivo = _nome_json(nome_arquivo)

    dados = {
        "total_figurinhas": album.total_figurinhas,
        "figurinhas": lista_encadeada_para_lista(album.cabeca),
        "repetidas": lista_encadeada_para_lista(album.repetidas)
    }

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return "Álbum salvo com sucesso."


def carregar_album(nome_arquivo="album.json"):
    nome_arquivo = _nome_json(nome_arquivo)

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    if "total_figurinhas" not in dados:
        raise ValueError("Arquivo inválido.")

    album = Album(int(dados["total_figurinhas"]))

    for item in dados.get("figurinhas", []):
        figurinha = dict_para_figurinha(item)
        album.adicionar(figurinha)

    for item in dados.get("repetidas", []):
        figurinha = dict_para_figurinha(item)
        album.repetidas = album._adicionar_na_lista_ordenada(album.repetidas, figurinha)
        album.qtd_repetidas += 1

    return album


def salvar(album, nome_arquivo="album.json"):
    return salvar_album(album, nome_arquivo)


def carregar(nome_arquivo="album.json"):
    return carregar_album(nome_arquivo)
