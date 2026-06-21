# Representa un producto del menú del restaurante

class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria  # plato, bebida, postre, etc.
        self.precio = precio
        self.disponible = True

    def cambiar_disponibilidad(self, estado):
        self.disponible = estado

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - ${self.precio:.2f} | {estado}"
