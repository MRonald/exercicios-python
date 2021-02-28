class Pedido:
    lista_pedidos = []

    def __init__(self, fornecedor, titulo, produto, quantidade):
        self.fornecedor = fornecedor
        self.titulo = titulo
        self.produto = produto
        self.quantidade = quantidade
        self.lista_pedidos.append(f"Fornecedor: {self.fornecedor} | Título: {self.titulo} | Produto: {self.produto} | Quantidade: {self.quantidade}")
