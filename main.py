# Punto de arranque del sistema de gestión de restaurante

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear instancia del restaurante
restaurante = Restaurante("El Sabor Manabita")

# Registrar productos en el menú
restaurante.registrar_producto(Producto("P001", "Seco de pollo", "Plato fuerte", 5.50))
restaurante.registrar_producto(Producto("P002", "Encebollado", "Plato fuerte", 4.00))
restaurante.registrar_producto(Producto("P003", "Jugo de naranja", "Bebida", 1.50))
restaurante.registrar_producto(Producto("P004", "Arroz con leche", "Postre", 2.00))
restaurante.registrar_producto(Producto("P005", "Ceviche mixto", "Entrada", 6.00))

# Marcar un producto como no disponible
producto_temp = restaurante.buscar_producto("P004")
if producto_temp:
    producto_temp.cambiar_disponibilidad(False)

# Registrar clientes
restaurante.registrar_cliente(Cliente("1308456789", "Luis Moreira", "0991234567"))
restaurante.registrar_cliente(Cliente("1305678901", "Ana Cedeño", "0987654321"))

# Mostrar menú y clientes
restaurante.listar_productos()
restaurante.listar_clientes()

# Registrar pedidos
print("\n--- Procesando pedidos ---")
restaurante.realizar_pedido("1308456789", ["P001", "P003"])
restaurante.realizar_pedido("1305678901", ["P002", "P004", "P005"])  # P004 no disponible

# Mostrar resumen final de clientes con sus pedidos
print("\n=== Resumen de pedidos por cliente ===")
for cliente in restaurante.clientes:
    print(f"\n{cliente}")
    for i, pedido in enumerate(cliente.pedidos, 1):
        print(f"  Pedido #{i}:")
        for p in pedido["productos"]:
            print(f"    - {p.nombre}")
        print(f"    Total: ${pedido['total']:.2f}")
