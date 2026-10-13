from src.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.entities.pedido import Pedido
from src.gateways.pedido_gateway import IPedidoGateway

class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente, valor_original, tipo_desconto) -> Pedido:
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo invalido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido)

        return Pedido

    def lista_pedido(self) -> list[Pedido]:
        return self.pedido_gateway.listar()
    
