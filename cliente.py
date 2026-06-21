# Representa a un cliente registrado en el restaurante

class Cliente:
    def __init__(self, cedula, nombre, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []  # lista de pedidos realizados

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def total_pedidos(self):
        return len(self.pedidos)

    def __str__(self):
        return f"Cliente: {self.nombre} | CI: {self.cedula} | Tel: {self.telefono} | Pedidos: {self.total_pedidos()}"
