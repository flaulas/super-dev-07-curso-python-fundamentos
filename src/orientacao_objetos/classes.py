from datetime import date
import os
import platform
from typing import List
import questionary
from rich.table import Table
from rich.console import Console
from rich.align import Align


class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []


# Classe é uma representação de objeto do mundo real
class Jogo:
    def __init__(self):
        # Atributos da classe
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: Desenvolvedora = None


def exemplo_01():
    # titulo = "GTA VI"
    # data_lancamento = date(2077, 2, 28)
    # preco = 650.00
    # genero = "Ação"
    # classificacao = "M"

    # gta_vi_dict = {
    #     "titulo": "GTA VI",
    #     "data_lancamento": date(2077, 2, 28),
    #     "preco": 650.00,
    #     "genero": "Ação",
    #     "classificacao": "M"
    # }

    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New York"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    # Instanciando um objeto chamado gta_vi da classe Jogo
    gta_vi = Jogo() # nome_objeto = NomeClasse()
    # Definindo valor para as atributos do objeto
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 650
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    gta_vi.preco = 669.99

    the_witcher = Jogo()
    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()
    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10, 27)
    league_of_legends.preco = 0
    league_of_legends.genero = "Moba"
    league_of_legends.classificacao = "12"

    # Adicionar os jogos na desenvolvedora
    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)


    colunas = ["Desenvolvedora", "Título", "Data de Lançamento", "Preço", "Gênero", "Classificação"]
    # Instancinado um objeto chamado tabela da classe Table 
    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao
    )
    tabela.add_row(
        "N/A", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao
    )
    tabela.add_row(
        "N/A", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificacao
    )

    # Isntanciando um objeto chamado console da classe Console
    console = Console()
    console.print(tabela)

# Exercício 01 Criar classe chamada Marca com os seguintes atributos
# - Nome
# - Id (1, 2, 3, 4, 5...)
# - Fundador str
# - Data de fundação
# - Faturamento float
# Criar uma função `exercicio_marca`
# Instanciar 2 objetos da classe Marca, atribuindo valor para todos os atributos
# batatinha = Produto()
# batatinha.valor = 1.30
# Apresentar os dados das duas marcas (print ou table)
# Exercício 02 Criar uma classe chamada Usuário com os seguintes atributos
# - Id (1, 2, 3, 4....)
# - Nome Completo 
# - Login
# - Data de nascimento
# Criar uma classe chamada Ticket com os seguintes atributos
# - Número (1000, 1001, 1002)
# - usuario do tipo Usuario
# - data de abertura 
# - status
# - data de fechamento
# - descrição 
# Criar uma função `exercicio_ticket`
# Intanciar dois usuários e preencher os atributos
# Criar um ticket para o primeiro usuário com status de 'Em análise' preenchendo todas as propriedades com exceção da data de fechamento, a data de abertura deve ser hoje
# Criar um ticket para o primeiro usuário com status de 'Finalizado' preenchendo todas as propriedades. A data de abertura deve ser 10 dias atrás, a data de fechamento de ve ser hoje
# Apresentar os dados do ticket e seus usuários



def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
desenvolvedoras: List[Desenvolvedora] = []

def exemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()
        
# from rich.align import Align
 
def adicionar_desenvolvedora():
    # Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietário").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.sede.pais = questionary.text("Digite o país da sede").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    # Listar desenvolvedoras
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    table = Table("Nome", "Proprietário", "Endereço")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )
    
    
    console.print(table)

exemplo_crud_lista_objetos()