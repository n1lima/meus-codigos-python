def menu():
    print("1-soma")
    print("2-subtrair")
    print("3-multiplicacao")
    print("4-divisao")
    print("5-sair")
    return input("ecolha um valor de 1 a 5: ")

def operacoesBasica(num1, num2, option):
    if option == '1':
         calculo = num1 + num2
         return calculo
    elif option == '2':
        calculo = num1 - num2
        return calculo
def operadoresAvancados(num1, num2, option):
    if option == '3':
        calculo = num1 * num2
        return calculo
    elif option == '4':
        calculo = num1 / num2   
        return calculo         
                

option = menu()
while option != '5':
    num1 = float(input("entre com num1:"))
    num2 = float(input("entre com num2:"))
 
    if option in ['1', '2']:#A expressão if op in ['1', '2']: 
    # verifica se o valor da variável op está presente na lista ['1', '2']. Vamos analisar isso mais detalhadamente
        resultado = operacoesBasica(num1, num2, option)
    elif option in ['3','4']: 
        resultado = operadoresAvancados(num1, num2, option)

    print(f'Resultado: {float(resultado):.2f}')

    option = menu()

