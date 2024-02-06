# Exemplo de código Python com code small e problemas para o SonarQube

def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo.
    
    Argumentos:
    n -- O número inteiro positivo para calcular o fatorial.
    
    Retorna:
    O fatorial de n.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Este é um comentário desnecessário
def verificar_palindromo(palavra):
    """
    Verifica se uma palavra é um palíndromo.
    
    Argumentos:
    palavra -- A palavra para verificar.
    
    Retorna:
    True se a palavra for um palíndromo, False caso contrário.
    """
    unused_variable = 42  # Variável não utilizada
    return palavra == palavra[::-1]

def main():
    numero = 5
    resultado = calcular_fatorial(numero)
    print(f'O fatorial de {numero} é {resultado}')

    texto = "radar"
    if verificar_palindromo(texto):
        print(f'A palavra "{texto}" é um palíndromo.')
    else:
        print(f'A palavra "{texto}" não é um palíndromo.')

    try:
        # Tentar dividir por zero
        resultado = 10 / 0
    except Exception as e:  # Captura de exceção ampla
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
