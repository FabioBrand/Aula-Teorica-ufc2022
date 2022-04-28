Classe Banco: Assinatura

class Banco:
    def __init__(self): (...)
    def cadastrar(self, conta): (...)
    def procurar_conta(self, numero): (...)
    def creditar(self, numero, valor): (...)
    def debitar(self, numero, valor): (...)
    def saldo(self, numero): (...)
    def transferir(self, origem, destino, valor): (...)