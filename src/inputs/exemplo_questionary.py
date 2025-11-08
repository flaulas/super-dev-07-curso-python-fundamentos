from questionary import text, password, select, checkbox, confirm

from src.envios.envio_email import enviar_email_pedido

sabores_pizza = [
    "Calabresa",
    "Mussarela",
    "Frango com Catupiry",
    "Portuguesa",
    "Quatro Queijos",
    "Marguerita",
    "Pepperoni",
    "Bacon",
    "Napolitana",
    "Vegetariana"
]


def __solicitar_text() -> str:
    cliente = text("Digite o e-mail do cliente").ask()
    return cliente


def __solicitar_senha() -> str:
    senha = password("Digite a senha do cliente").ask()
    return senha


# Questionar o tamanho Pequena, Média, Grande
def __escolher_opcao() -> str:
    opcoes = ["Pequena", "Média", "Grande"]
    opcao_escolhida = select("Escolha o tamanho da pizza", choices=opcoes).ask()
    return opcao_escolhida


def __escolher_sabores(tamanho: str) -> list:
    quantidade_maxima_sabores = 1
    if tamanho == "Média":
        quantidade_maxima_sabores = 2
    elif tamanho == "Grande":
        quantidade_maxima_sabores = 4
    
    sabores = checkbox(
        "Escolha o(s) sabor(es) desejado(s)", 
        choices=sabores_pizza,
        validate=lambda elementos: __validar_quantidade_sabores(elementos, quantidade_maxima_sabores)
    ).ask()

    return sabores


def __validar_quantidade_sabores(elementos: list[str], quantidade_maxima: int) -> bool | str:
    if len(elementos) == 0:
        return "No mínimo deve conter 1 sabor"
    if len(elementos) > quantidade_maxima:
        return f"A pizza deve conter no máximo {quantidade_maxima} sabor(es)"
    return True


def __solicitar_confirmacao() -> bool:
    confirmado = confirm("Você confirma o pedido?").ask()
    return confirmado


def exemplos():
    cliente = __solicitar_text()
    senha = __solicitar_senha()

    if cliente.endswith("@gmail.com") and senha == "Batatinha":
        tamanho = __escolher_opcao()
        sabores = __escolher_sabores(tamanho)
        pedido_confirmado = __solicitar_confirmacao()

        if pedido_confirmado == True:
            enviar_email_pedido(cliente, tamanho, sabores)
            print("Pedido confirmado")
        else:
            print("Pedido cancelado")

# Tamanho permite ele escolher uma quantidade diferente de sabores
#   - Pequena 1 sabor
#   - Média 1, 2 sabores
#   - Grande 1, 2, 3, 4 sabores
# Perguntar se ele quer efetivar a compra
# Gerar um arquivo json com os dados do peiddo