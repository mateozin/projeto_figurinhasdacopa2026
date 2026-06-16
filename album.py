from figurinha import Figurinha, NoLista


class Album:
    def __init__(self, total_figurinhas):
        if not isinstance(total_figurinhas, int) or total_figurinhas <= 0:
            raise ValueError("Total tem que ser um número positivo.")

        self.cabeca = None
        self.repetidas = None
        self.tamanho = 0
        self.qtd_repetidas = 0
        self.total_figurinhas = total_figurinhas

    def _validar_figurinha(self, figurinha):
        if not isinstance(figurinha, Figurinha):
            raise ValueError("Isso não é uma figurinha.")

    def _validar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            raise ValueError("ID deve ser um número inteiro.")
        if id <= 0:
            raise ValueError("ID deve ser positivo.")
        return id

    def _adicionar_na_lista_ordenada(self, inicio, figurinha):
        novo = NoLista(figurinha)

        if inicio is None or figurinha.id < inicio.figurinha.id:
            novo.proximo = inicio
            return novo
        atual = inicio
        while atual.proximo is not None and atual.proximo.figurinha.id < figurinha.id:
            atual = atual.proximo

        novo.proximo = atual.proximo
        atual.proximo = novo
        return inicio

    def _remover_da_lista_por_id(self, inicio, id):
        if inicio is None:
            return inicio, None
        if inicio.figurinha.id == id:
            figurinha_removida = inicio.figurinha
            return inicio.proximo, figurinha_removida

        anterior = inicio
        atual = inicio.proximo

        while atual is not None:
            if atual.figurinha.id == id:
                anterior.proximo = atual.proximo
                return inicio, atual.figurinha

            anterior = atual
            atual = atual.proximo
        return inicio, None

    def adicionar(self, figurinha):
        self._validar_figurinha(figurinha)

        if self.buscar(figurinha.id) is not None:
            self.repetidas = self._adicionar_na_lista_ordenada(self.repetidas, figurinha)
            self.qtd_repetidas += 1
            return "Figurinha repetida adicionada nas repetidas."

        self.cabeca = self._adicionar_na_lista_ordenada(self.cabeca, figurinha)
        self.tamanho += 1
        return "Figurinha adicionada ao álbum."

    def inserir(self, figurinha):
        return self.adicionar(figurinha)

    def remover(self, id):
        id = self._validar_id(id)
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                self.repetidas, repetida = self._remover_da_lista_por_id(self.repetidas, id)

                if repetida is not None:
                    atual.figurinha = repetida
                    self.qtd_repetidas -= 1
                    return "Figurinha removida. Uma repetida ocupou o lugar dela no álbum."

                self.cabeca, removida = self._remover_da_lista_por_id(self.cabeca, id)
                if removida is not None:
                    self.tamanho -= 1
                    return "Figurinha removida do álbum."

            atual = atual.proximo
        return "Figurinha não encontrada no álbum."

    def remover_repetida(self, id):
        id = self._validar_id(id)
        self.repetidas, removida = self._remover_da_lista_por_id(self.repetidas, id)
        if removida is None:
            return "Figurinha repetida não encontrada."
        self.qtd_repetidas -= 1

        return "Figurinha removida das repetidas."

    def buscar(self, id):
        id = self._validar_id(id)
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha

            atual = atual.proximo
        return None

    def consultar(self, id):
        figurinha = self.buscar(id)
        if figurinha is None:
            return "Figurinha não encontrada."
        return str(figurinha)

    def buscar_por_jogador(self, nome):
        if not nome or not nome.strip():
            raise ValueError("Nome do jogador não pode ser vazio.")

        nome = nome.lower().strip()
        atual = self.cabeca
        resultado = ""

        while atual is not None:
            if nome in atual.figurinha.nome.lower():
                resultado += str(atual.figurinha) + "\n"
            atual = atual.proximo
        if resultado == "":
            return "Nenhuma figurinha com esse jogador encontrada!"

        return resultado.rstrip()
    def buscar_por_selecao(self, selecao):
        if not selecao or not selecao.strip():
            raise ValueError("Seleção não pode ser vazia.")

        selecao = selecao.lower().strip()
        atual = self.cabeca
        resultado = ""

        while atual is not None:
            if selecao in atual.figurinha.pais.lower():
                resultado += str(atual.figurinha) + "\n"

            atual = atual.proximo

        if resultado == "":
            return "Nenhuma figurinha encontrada para essa seleção."

        return resultado.rstrip()
    def ver_album_completo(self):
        if self.cabeca is None:
            return "Álbum vazio."

        atual = self.cabeca
        resultado = "ÁLBUM\n"

        while atual is not None:
            resultado += str(atual.figurinha) + "\n"
            atual = atual.proximo

        return resultado.rstrip()

    def listar_repetidas(self):
        if self.repetidas is None:
            return "Nenhuma figurinha repetida."

        atual = self.repetidas
        resultado = "FIGURINHAS REPETIDAS\n"

        while atual is not None:
            resultado += str(atual.figurinha) + "\n"
            atual = atual.proximo

        return resultado.rstrip()

    def contar_repetidas(self):
        return self.qtd_repetidas

    def porcentagem_concluida(self):
        return (self.tamanho / self.total_figurinhas) * 100

    def status(self):
        return (
            f"Figurinhas únicas no álbum: {self.tamanho}/{self.total_figurinhas}\n"
            f"Repetidas: {self.qtd_repetidas}\n"
            f"Conclusão: {self.porcentagem_concluida():.2f}%"
        )
