from Heranca.Contato import Contato
from Heranca.Pedido import Pedido
from Heranca.Pessoa import Pessoa


class Fornecedor(Pessoa, Contato):
    lista_fornecedores = []

    def __init__(self, nome, idade, sexo, email, github, linkedin):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.github = github
        self.linkedin = linkedin
        self.lista_fornecedores.append(f"Nome: {self.nome} | Idade: {self.idade} | Sexo: {self.sexo} | Email: {self.email}")

    def newPedido(self, titulo, produto, quantidade):
        Pedido(self.nome, titulo, produto, quantidade)

    def getAllPedidos(self):
        print("---- LP ----")
        for i in Pedido.lista_pedidos:
            print(i)
        print("------------")

    def getAllFornecedores(self):
        print("---- LF ----")
        for i in self.lista_fornecedores:
            print(i)
        print("------------")
