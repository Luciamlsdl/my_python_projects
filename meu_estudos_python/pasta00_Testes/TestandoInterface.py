import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import * # Importa todas as constantes do ttkbootstrap, como SUCCESS, DANGER, INFO

# --- Funções de Lógica de Negócio (Adaptadas para a GUI) ---

def calcula_valores(valor_casa: float, salario_comprador: float, anos_pagamento: int) -> tuple[float, float]:
    """
    Calcula a prestação mensal e o valor mínimo permitido (30% do salário).

    Args:
        valor_casa (float): O valor total da casa.
        salario_comprador (float): O salário mensal do comprador.
        anos_pagamento (int): A quantidade de anos para pagamento.

    Returns:
        tuple[float, float]: Uma tupla contendo (prestacao_mensal, limite_salario_30_porcento).
    """
    if anos_pagamento <= 0: # Evita divisão por zero
        return 0.0, 0.0
    meses_pagamento = anos_pagamento * 12
    prestacao_mensal = valor_casa / meses_pagamento
    limite_salario_30_porcento = salario_comprador * 0.30
    return prestacao_mensal, limite_salario_30_porcento

# --- Funções da Interface Gráfica ---

def limpar_campos(entry_casa, entry_salario, entry_anos, label_resultado):
    """Limpa os campos de entrada e o rótulo de resultado."""
    entry_casa.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_anos.delete(0, tk.END)
    label_resultado.config(text="") # Limpa o texto do rótulo

def calcular_emprestimo(entry_casa, entry_salario, entry_anos, label_resultado):
    """
    Função chamada quando o botão 'Calcular Empréstimo' é clicado.
    Valida as entradas, calcula e exibe o resultado.
    """
    try:
        valor_casa = float(entry_casa.get())
        salario_comprador = float(entry_salario.get())
        anos_pagamento = int(entry_anos.get())

        # Validação de valores positivos
        if valor_casa <= 0 or salario_comprador <= 0 or anos_pagamento <= 0:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores positivos para todos os campos.")
            return

        prestacao, valor_minimo = calcula_valores(valor_casa, salario_comprador, anos_pagamento)

        # Atualiza o label de resultado com a informação formatada
        resultado_texto = f"Para uma casa de R$: {valor_casa:.2f} em {anos_pagamento} anos:\n" \
                          f"A prestação mensal será de R$: {prestacao:.2f}\n" \
                          f"Seu limite de 30% do salário é de R$: {valor_minimo:.2f}\n\n"

        if prestacao <= valor_minimo:
            label_resultado.config(text=resultado_texto + "🎉 Empréstimo APROVADO!", foreground="green", bootstyle=SUCCESS)
        else:
            label_resultado.config(text=resultado_texto + "😔 Empréstimo NEGADO! (Prestação excede 30% do salário)", foreground="red", bootstyle=DANGER)

    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos para todos os campos.")
    except Exception as e:
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

# --- Configuração da Interface Tkinter com TTKBootstrap ---

def criar_interface():
    """Cria e executa a janela principal da aplicação."""
    root = ttk.Window(themename="flatly") # Cria a janela principal com o tema 'flatly' do ttkbootstrap
    root.title("Simulador de Empréstimo Bancário")
    root.geometry("500x450") # Define o tamanho inicial da janela
    root.resizable(False, False) # Impede que a janela seja redimensionada

    # Frame principal para organizar os widgets
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Título da aplicação
    title_label = ttk.Label(main_frame, text="Simulador de Empréstimo Imobiliário",
                            font=("Helvetica", 16, "bold"), bootstyle=PRIMARY)
    title_label.pack(pady=10)

    # --- Entrada de Valor da Casa ---
    label_casa = ttk.Label(main_frame, text="Valor da Casa (R$):", font=("Helvetica", 10))
    label_casa.pack(anchor=tk.W, pady=(10, 0))
    entry_casa = ttk.Entry(main_frame, width=40, bootstyle="info")
    entry_casa.pack(pady=5)
    entry_casa.focus_set() # Coloca o cursor neste campo ao iniciar

    # --- Entrada de Salário ---
    label_salario = ttk.Label(main_frame, text="Seu Salário Mensal (R$):", font=("Helvetica", 10))
    label_salario.pack(anchor=tk.W, pady=(10, 0))
    entry_salario = ttk.Entry(main_frame, width=40, bootstyle="info")
    entry_salario.pack(pady=5)

    # --- Entrada de Anos para Pagar ---
    label_anos = ttk.Label(main_frame, text="Anos para Pagar:", font=("Helvetica", 10))
    label_anos.pack(anchor=tk.W, pady=(10, 0))
    entry_anos = ttk.Entry(main_frame, width=40, bootstyle="info")
    entry_anos.pack(pady=5)

    # --- Botões de Ação ---
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=15)

    btn_calcular = ttk.Button(button_frame, text="Calcular Empréstimo", bootstyle=SUCCESS,
                              command=lambda: calcular_emprestimo(entry_casa, entry_salario, entry_anos, label_resultado))
    btn_calcular.pack(side=tk.LEFT, padx=10)

    btn_limpar = ttk.Button(button_frame, text="Limpar", bootstyle=WARNING,
                            command=lambda: limpar_campos(entry_casa, entry_salario, entry_anos, label_resultado))
    btn_limpar.pack(side=tk.LEFT, padx=10)

    # --- Rótulo para Exibir o Resultado ---
    label_resultado = ttk.Label(main_frame, text="", font=("Helvetica", 11), wraplength=400)
    label_resultado.pack(pady=15)

    root.mainloop() # Inicia o loop principal da aplicação Tkinter

# --- Execução Principal ---
if __name__ == "__main__":
    criar_interface()