class Figurinha:
    RARIDADES = ["comum", "especial", "lendaria"]

    def __init__(self, id, nome, pais, posicao, raridade):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID deve ser um inteiro positivo.")
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        if not pais or not pais.strip():
            raise ValueError("País não pode ser vazio.")
        if raridade.lower() not in self.RARIDADES:
            raise ValueError(f"Raridade inválida. Use apenas as raridades disponiveis")

        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade.lower()

    def to_save(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "posicao": self.posicao,
            "raridade": self.raridade,
        }

    def __str__(self):
        return (
            f"[{self.pais}{self.id}] {self.nome} - {self.posicao}"
            f"RARIDADE {self.raridade}"
        )

#verificar se tem cópias/repetidas
    def repetida(self, other):
        if not isinstance(other, Figurinha):
            return False
        return self.id == other.id

#nodolista
class NoLista:
    def __init__(self, figurinha):
        self.figurinha: Figurinha = figurinha
        self.proximo: "NoLista | None" = None