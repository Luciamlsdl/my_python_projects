# Este código é um estudo é somente um teste

def somar(n1, n2):
	soma = n1 + n2
	return soma


def mostrar_soma(soma):
	print(f"A soma dos valores é = {soma}.")


# Programa principal
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

soma = somar(n1, n2)
mostrar_soma(soma)

