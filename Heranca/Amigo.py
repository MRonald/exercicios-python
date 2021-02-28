from Heranca.Contato import Contato
from Heranca.Pessoa import Pessoa


class Amigo(Pessoa, Contato):
    todos_amigos = []

    def __init__(self, nome, idade, sexo, email, linkedin, github):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.linkedin = linkedin
        self.github = github
        self.todos_amigos.append(f"Nome: {self.nome} | Idade: {self.idade} | Sexo: {self.sexo} | Email: {self.email}")

    def getAllAmigos(self):
        print("---- LA ----")
        for i in self.todos_amigos:
            print(i)
        print("------------")
