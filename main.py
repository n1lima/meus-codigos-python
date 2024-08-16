def menu():
    print("1-soma")
    print("2-subtrair")
    print("3-multiplicacao")
    print("4-divisao")
    print("5-sair")
    return input("escolha de 1 a 5:  ") #esse input vai ler, e o return vai rertonar o valor em string

def calculadora(num1, num2, op):

    if op == '1':
         calculo = num1 + num2
         return calculo
    elif op == '2':
        calculo = num1 - num2
        return calculo
    elif op == '3':
        calculo = num1 * num2
        return calculo
    elif op == '4':
        calculo = num1 / num2   
        return calculo         


op = menu() #op vai receber o valor que a funçao menu esta retornando 
while op != '5':
   
    num1 = float(input('entre com numero:'))#se n deixar claro que o valor num1 e num2 eh float ele vai ler como str
    num2 = float(input('entre com numero:'))

    resultado = calculadora(num1, num2, op) #a funcao vai receber os parametros, e resultado vai receber o valor da funçao esta retonando, 

    if resultado is not None: #se resultado nao for igual a NONE entao executa esse bloco de comandos
        print(f"Resultado: {float(resultado):.2f}")#o .2f nao estava funcionando pq o resultado tava vindo como string
    else:
        print("deu erro no código")
    
    op = menu()#vai executar novamente a menu novamente

    
    
