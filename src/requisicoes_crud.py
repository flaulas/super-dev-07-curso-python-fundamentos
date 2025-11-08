from typing import Dict, List
import questionary
import requests
from rich.console import Console
from rich.table import Table
import os
import platform

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def crud():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu principal", choices=[
            "Clientes", "Vendas", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Clientes":
            menu_cliente()


def menu_cliente():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu", choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Listar":
            listar_clientes()
        elif opcao == "Cadastrar":
            cadastrar_cliente()
        elif opcao == "Excluir":
            exluir_cliente()
        elif opcao == "Editar":
            editar_cliente()


def listar_clientes():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/clientes"
    response = requests.get(url)
    if response.status_code == 200:
        clientes: List[Dict[str, str | float | int]] = response.json()
        quantidade_clientes = len(clientes)

        tabela = Table()
        tabela.add_column("Código")
        tabela.add_column("Nome")
        tabela.add_column("Telefone")
        tabela.add_column("Crédito")

        
        for i in range(0, quantidade_clientes):
            cliente = clientes[i] # pegar da lista o cliente por uma posição
            nome = cliente.get("nome")
            id = cliente.get("id")
            telefone = cliente.get("telefone")
            credito = cliente.get("credito")

            tabela.add_row(str(id), nome, telefone, f"R$ {credito}")
            
        console = Console()
        console.print(tabela)


def cadastrar_cliente():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/clientes"
    nome = questionary.text("Digite o nome do cliente").ask().strip()
    telefone = questionary.text("Digite o telefone").ask()
    valor_credito = float(questionary.text("Digite o crédito").ask().replace(",", "."))
    payload = {
        "nome": nome,
        "telefone": telefone,
        "credito": valor_credito
    }
    headers = {
        "Content-Type": "application/json-patch+json"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Cliente cadastrado com sucesso")
    else:
        print("Ocorreu uma falha ao cadastrar o cliente\nErro:", response.text)


def exluir_cliente():
    listar_clientes()
    id = questionary.text("Digite o id para apagar o cliente").ask()

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/clientes/{id}"

    response = requests.delete(url)

    if response.status_code == 204:
        print("Cliente excluído com sucesso")
    elif response.status_code == 404:
        print("Cliente não encontrado")
    else:
        print(f"Não foi possível apagar o cliente. Erro:{response.text}")


def editar_cliente():
    listar_clientes()

    id_para_editar = questionary.text("Digite o id para editar o cliente").ask()
    nome = questionary.text("Digite o nome do cliente").ask().strip()
    telefone = questionary.text("Digite o telefone").ask()
    valor_credito = float(questionary.text("Digite o crédito").ask().replace(",", "."))

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/clientes/{id_para_editar}"

    payload = {
        "nome": nome,
        "telefone": telefone,
        "credito": valor_credito
    }
    
    headers = {
        "Content-Type": "application/json-patch+json"
    }
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Cliente alterado com sucesso")
    else:
        print("Ocorreu uma falha ao alterar o cliente\nErro:", response.text)


if __name__ == "__main__":
    crud()