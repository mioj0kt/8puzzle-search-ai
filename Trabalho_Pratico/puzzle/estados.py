class Estado:
    def __init__(self, tabuleiro):
        self.tabuleiro = tuple(tabuleiro)

    def objetivo(self):
        return self.tabuleiro == (
            1, 2, 3,
            4, 5, 6,
            7, 8, 0
        )

    def posicao_vazia(self):
        return self.tabuleiro.index(0)

    def __eq__(self, outro):
        return self.tabuleiro == outro.tabuleiro

    def __hash__(self):
        return hash(self.tabuleiro)

    def __str__(self):
        resultado = ""

        for i in range(0, 9, 3):
            linha = self.tabuleiro[i:i+3]
            resultado += " ".join(map(str, linha)) + "\n"

        return resultado