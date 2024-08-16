''''' 
Entre com dois valores inteiros.
1)Verifique o tipo de dado para entrar
somente com inteiros
2)Um será a base e outro a potência.
3)Exiba o resultado
'''
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Por favor, entre com um valor inteiro.")

base = get_integer_input("Entre com a base (inteiro): ")
expoente = get_integer_input("Entre com o expoente (inteiro): ")

resultado = base ** expoente

print(f"O resultado de {base} elevado a {expoente} é {resultado}.")