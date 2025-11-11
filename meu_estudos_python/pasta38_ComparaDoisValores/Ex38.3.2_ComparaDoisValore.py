"""
Programa: Comparação entre dois valores inteiros
Autor: Luciano Soares
Descrição:
    Lê dois números inteiros e mostra qual é o maior,
    ou se ambos são iguais.
    Esta versão usa a biblioteca RICH para deixar a saída colorida e mais amigável.
"""

# ========================================
# Importações
# ========================================

import os
from rich.console import Console        # Para imprimir texto colorido e formatado
from rich.panel import Panel            # Para criar caixas (painéis) de texto
from rich.text import Text              # Para estilizar texto dentro dos painéis
from rich.prompt import IntPrompt       # Para ler números com validação automática
from rich.rule import Rule              # Para criar uma linha divisória bonita


# ========================================
# Classe principal
# ========================================

class CompararDoisValores:
    def __init__(self):
        # Cria um console Rich (objeto que "fala" com o terminal)
        self.console = Console()
        self.primeiro_valor = 0
        self.segundo_valor = 0

    # ------------------------------------
    # Limpa a tela (Windows e Linux)
    # ------------------------------------
    def limpa_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    # ------------------------------------
    # Mostra a apresentação do programa
    # ------------------------------------
    def apresentacao(self):
        # Cria uma linha decorada com título centralizado
        self.console.print(Rule("[bold yellow]Programa de Comparação entre Dois Valores", style="bright_yellow"))
        self.console.print(
            Panel(
                Text("Bem-vindo! Este programa lê dois números inteiros e mostra qual é o maior.", justify="center", style="green"),
                border_style="bright_blue",
                title="[bold cyan]Apresentação[/bold cyan]",
                subtitle="Feito por Luciano Soares"
            )
        )

    # ------------------------------------
    # Lê valores com validação automática
    # ------------------------------------
    def ler_valores(self):
        # O Rich tem um prompt interativo que valida inteiros automaticamente
        self.primeiro_valor = IntPrompt.ask("[bold white]Digite o primeiro valor[/bold white]")
        self.segundo_valor = IntPrompt.ask("[bold white]Digite o segundo valor[/bold white]")

    # ------------------------------------
    # Compara os valores
    # ------------------------------------
    def comparar_valores(self):
        if self.primeiro_valor > self.segundo_valor:
            return f"O primeiro valor ({self.primeiro_valor}) é o maior."
        elif self.segundo_valor > self.primeiro_valor:
            return f"O segundo valor ({self.segundo_valor}) é o maior."
        else:
            return f"Os dois valores são iguais ({self.primeiro_valor})."

    # ------------------------------------
    # Executa o fluxo completo do programa
    # ------------------------------------
    def executor(self):
        self.limpa_tela()
        self.apresentacao()
        self.ler_valores()
        resultado = self.comparar_valores()

        # Mostra o resultado dentro de um painel colorido
        self.console.print(
            Panel(
                Text(resultado, style="bold magenta", justify="center"),
                border_style="bright_yellow",
                title="[bold green]Resultado[/bold green]",
                subtitle="Comparação final"
            )
        )

        # Linha de encerramento
        self.console.print(Rule("[bold cyan]Fim do Programa", style="cyan"))


# ========================================
# Execução principal
# ========================================
if __name__ == "__main__":
    app = CompararDoisValores()
    app.executor()
