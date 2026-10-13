from src.entities.pedido import Pedido
from src.gateways.pedido_gateway import IPedidoGateway
from src.frameworks.database.memory_database import MemoryDatase

class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatase):
        self.database = database

    def salvar(self, pedido: Pedido):
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        return self.database.pedidos