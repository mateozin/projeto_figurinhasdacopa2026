from album import Album
from fila import Fila


class PropostaTroca:
    def __init__(self, usuario_1, album_1, id_fig_1, usuario_2, album_2, id_fig_2):
        self.usuario_1 = usuario_1
        self.album_1 = album_1
        self.id_fig_1 = id_fig_1
        self.usuario_2 = usuario_2
        self.album_2 = album_2
        self.id_fig_2 = id_fig_2

    def __str__(self):
        return (
            f"{self.usuario_1} oferece a figurinha {self.id_fig_1} "
            f"para {self.usuario_2} pela figurinha {self.id_fig_2}"
        )


class NoHistorico:
    def __init__(self, texto):
        self.texto = texto
        self.proximo = None


class Historico:
    def __init__(self):
        self.propostas = Fila()
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def _validar_nome(self, nome):
        if not nome or not nome.strip():
            raise ValueError("Não pode ser vazio.")

        return nome.strip()

    def _validar_album(self, album):
        if not isinstance(album, Album):
            raise ValueError("Isso não é um álbum.")

    def _validar_id(self, id):
        try:
            id = int(id)
        except (ValueError, TypeError):
            raise ValueError("ID deve ser um número inteiro.")

        if id <= 0:
            raise ValueError("ID deve ser positivo.")

        return id

    def _buscar_repetida(self, album, id):
        atual = album.repetidas

        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha

            atual = atual.proximo

        return None

    def _adicionar_registro(self, texto):
        novo = NoHistorico(texto)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def registrar_proposta_troca(self, usuario_1, album_1, id_fig_1, usuario_2, album_2, id_fig_2):
        usuario_1 = self._validar_nome(usuario_1)
        usuario_2 = self._validar_nome(usuario_2)
        self._validar_album(album_1)
        self._validar_album(album_2)

        id_fig_1 = self._validar_id(id_fig_1)
        id_fig_2 = self._validar_id(id_fig_2)

        proposta = PropostaTroca(usuario_1, album_1, id_fig_1, usuario_2, album_2, id_fig_2)
        self.propostas.enqueue(proposta)

        return "Proposta de troca adicionada."

    def ver_proxima_proposta(self):
        proposta = self.propostas.primeiro()

        if proposta is None:
            return "Nenhuma proposta na fila."

        return str(proposta)

    def verificar_repetidas(self, proposta=None):
        if proposta is None:
            proposta = self.propostas.primeiro()

        if proposta is None:
            return False

        figurinha_1 = self._buscar_repetida(proposta.album_1, proposta.id_fig_1)
        figurinha_2 = self._buscar_repetida(proposta.album_2, proposta.id_fig_2)

        return figurinha_1 is not None and figurinha_2 is not None

    def efetuar_troca_automatica(self):
        proposta = self.propostas.dequeue()

        if proposta is None:
            return "Nenhuma proposta na fila."

        figurinha_1 = self._buscar_repetida(proposta.album_1, proposta.id_fig_1)
        figurinha_2 = self._buscar_repetida(proposta.album_2, proposta.id_fig_2)

        if figurinha_1 is None or figurinha_2 is None:
            texto = "Troca não realizada. Um dos usuários não tem figurinha repetida."
            self._adicionar_registro(texto)
            return texto

        proposta.album_1.remover_repetida(proposta.id_fig_1)
        proposta.album_2.remover_repetida(proposta.id_fig_2)

        proposta.album_1.adicionar(figurinha_2)
        proposta.album_2.adicionar(figurinha_1)

        texto = (
            f"Troca feita: {proposta.usuario_1} recebeu a figurinha {proposta.id_fig_2} "
            f"e {proposta.usuario_2} recebeu a figurinha {proposta.id_fig_1}."
        )

        self._adicionar_registro(texto)
        return texto

    def efetuar_troca(self):
        return self.efetuar_troca_automatica()

    def mostrar_propostas(self):
        return self.propostas.listar()

    def mostrar_historico(self):
        if self.inicio is None:
            return "Histórico vazio."

        atual = self.inicio
        resultado = "HISTÓRICO\n"

        while atual is not None:
            resultado += atual.texto + "\n"
            atual = atual.proximo

        return resultado.rstrip()

    def quantidade_propostas(self):
        return self.propostas.quantidade()

    def quantidade_registros(self):
        return self.tamanho
