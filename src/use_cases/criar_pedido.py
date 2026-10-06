from src.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.entities.pedido import Pedido

class CriarPedido:
    def executar(self, cliente, valor_original, tipo_desconto) -> Pedido:
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo invalido")

        return Pedido(cliente, valor_original, desconto)
