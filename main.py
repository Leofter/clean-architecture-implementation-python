from src.frameworks.database.memory_database import MemoryDatase
from src.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.use_cases.criar_pedido import CriarPedido
from src.adapters.controllers.pedido_controller import PedidoController


def main() -> None:
    database = MemoryDatase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    controller = PedidoController(criar_pedido_use_case)

    pedido1 = controller.criar_pedido("Cliebte A", 100, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 100, "vip")
    pedido3 = controller.criar_pedido("Cliente C", 100, "premium")

    print("Pedidos criados: ")
    print(pedido1.cliente, pedido1.valor_original, pedido1.valor_final())
    print(pedido2.cliente, pedido2.valor_original, pedido2.valor_final())
    print(pedido3.cliente, pedido3.valor_original, pedido3.valor_final())

    if __name__ == "__main__":
        main()
