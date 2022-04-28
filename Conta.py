class Banco:

    def __init__(self):
    self.contas = [None] * 100
    self.indice = 0

    def cadastrar(self, conta: Conta):
    self.contas[self.indice] = conta
    self.indice += 1