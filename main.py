from src.frameworks.database.memory_database import MemoryDatase
from src.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.use_cases.criar_pedido import CriarPedido
from src.adapters.controllers.pedido_controller import PedidoController
from src.presenters.pedido_presenter import PedidoPresenter


def main() -> None:
    database = MemoryDatase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)

    controller.criar_pedido("Cliente A", 100, "normal")
    controller.criar_pedido("Cliente B", 100, "vip")
    controller.criar_pedido("Cliente C", 100, "premium")

    print("Pedidos criados:")
    print(controller.listar_pedido())


if __name__ == "__main__":
    main()
