class CriarPedidoOutputDTO:
    def __init__(
        self,
        cliente,
        valor_original: float,
        valor_desconto: float,
        valor_final: float,
        tipo_desconto: str,
    ):

        self.cliente = cliente
        self.valor_orignal = valor_original
        self.valor_desconto = valor_desconto
        self.valor_final = valor_final
        self.tipo_desconto = tipo_desconto
