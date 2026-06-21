# Gestiona las operaciones principales del restaurante

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # --- Gestión de productos ---

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def listar_productos(self):
        print(f"\n=== Menú de {self.nombre} ===")
        if not self.productos:
            print("  Sin productos registrados.")
        for p in self.productos:
            print(f"  {p}")

    # --- Gestión de clientes ---

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente(self, cedula):
        for c in self.clientes:
            if c.cedula == cedula:
                return c
        return None

    def listar_clientes(self):
        print(f"\n=== Clientes registrados en {self.nombre} ===")
        if not self.clientes:
            print("  Sin clientes registrados.")
        for c in self.clientes:
            print(f"  {c}")

    # --- Realizar pedido ---

    def realizar_pedido(self, cedula_cliente, codigos_productos):
        cliente = self.buscar_cliente(cedula_cliente)
        if not cliente:
            print(f"Cliente con CI {cedula_cliente} no encontrado.")
            return

        pedido = []
        total = 0.0

        for codigo in codigos_productos:
            producto = self.buscar_producto(codigo)
            if producto and producto.disponible:
                pedido.append(producto)
                total += producto.precio
            else:
                print(f"  Producto '{codigo}' no disponible o no existe.")

        if pedido:
            detalle = {
                "productos": pedido,
                "total": total
            }
            cliente.agregar_pedido(detalle)
            print(f"\nPedido registrado para {cliente.nombre}:")
            for p in pedido:
                print(f"  - {p.nombre} ............. ${p.precio:.2f}")
            print(f"  Total: ${total:.2f}")
