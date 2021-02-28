class Empregado:
    'Classe base para empregados'
    contador = 0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Empregado.contador += 1

    def mostra_contador(self):
        print(f"Número de empregados: {Empregado.contador}")

    def mostra_empregado(self):
        print(f"Nome:  {self.nome} |  Salário:  {self.salario}")
