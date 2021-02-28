from Heranca.Amigo import Amigo
from Heranca.Fornecedor import Fornecedor

a1 = Amigo("João", 38, "M", "joao.1020@gmail.com", "in/joao", "hub/joao")
a1.getAllAmigos()

f1 = Fornecedor("Michael", 20, "M", "ronaldmichael918@gmail.com", "in/mr-dev", "hub/MRonald")
f1.getAllFornecedores()

f1.newPedido("Abastecimento 1", "Catchup", 500)
f1.getAllPedidos()
