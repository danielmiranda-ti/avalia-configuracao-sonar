def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)

numero = 5
resultado = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')

def verificar_palindromo(palavra):
    return palavra == palavra[::-1]

texto = "radar"
if verificar_palindromo(texto):
    print(f'A palavra "{texto}" é um palíndromo.')
else:
    print(f'A palavra "{texto}" não é um palíndromo.')
