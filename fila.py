class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, valor):
        novo = NoFila(valor)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1
        return "Adicionado na fila com sucesso!"

    def dequeue(self):
        if self.esta_vazia():
            return None

        valor = self.inicio.valor
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return valor

    def primeiro(self):
        if self.esta_vazia():
            return None

        return self.inicio.valor

    def quantidade(self):
        return self.tamanho

    def listar(self):
        if self.esta_vazia():
            return "Fila vazia."

        atual = self.inicio
        resultado = ""

        while atual is not None:
            resultado += str(atual.valor) + "\n"
            atual = atual.proximo

        return resultado.rstrip()
