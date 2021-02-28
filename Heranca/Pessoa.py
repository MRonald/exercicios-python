class Pessoa:
    todas_pessoas = []

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.todas_pessoas.append(self)
