import os
#FUNÇÕES DO MENU
def main():
   menu()

def continuar():
    try:
        denovo = int(input('Deseja continuar? 1-Sim 2-Não \n'))
        while denovo != 2:
            os.system('cls')
            main()
        if denovo == 2:
            encerrar_app()
    except:
        opcao_invalida_denovo()

def encerrar_app():
    os.system('cls')
    print('App Encerrado...')

def opcao_invalida_denovo():
    print('Você digitou uma opção errada!')
    os.system('cls')
    continuar()

def opcao_invalida():
    input('Você digitou uma opção errada! aperte qualquer tecla para continuar!')
    os.system('cls')
    menu()

#FUNÇÕES ARITMÉTICAS
def adicionar():
    os.system('cls')
    print('     SOMA')
    x = int(input('Digite o primeiro valor a ser somado: '))
    y = int(input('Digite o segundo valor: '))
    resultado = x + y
    print(f'{x} + {y} = {resultado}')
    continuar()

def subtrair():
    os.system('cls')
    print('    SUBTRAÇÃO')
    x = int(input('Digite o minuendo: '))
    y = int(input('Digite o subtraendo: '))
    resultado = x - y
    print(f'{x} - {y} = {resultado}')
    continuar()

def multiplicar():
    os.system('cls')
    print('    MULTIPLICAÇÃO')
    x = int(input('Digite o numero a ser multiplicado: '))
    y = int(input('Digite o multiplicador: '))
    resultado = x * y
    print(f'{x} * {y} = {resultado}')
    continuar()

def divisao():
    os.system('cls')
    print('    DIVISÃO')
    x = int(input('Digite o dividendo: '))
    y = int(input('Digite o divisor: '))
    resultado = int(x / y)
    resultado_resto = float(x / y)
    resto = resultado_resto % 2
    if resto % 2 != 0:
        print(f'{x} / {y} = {round(resultado_resto, 2)}')
    else:
        print(f'{x} / {y} = {resultado}')
    continuar()

#MENU
def menu():
    try:
        print('1-SOMA 2-SUBTRAÇÃO 3-MULTIPLICAÇÃO 4-DIVISÃO 5-SAIR')
        funcao = int(input('Escolha uma função:'))
        if funcao == 1:
            adicionar()
        elif funcao == 2:
            subtrair()
        elif funcao == 3:
            multiplicar()
        elif funcao == 4:
            divisao()
        elif funcao == 5:
            encerrar_app()
        else:
            encerrar_app()
    except:
        opcao_invalida()


if __name__ == '__main__' :
       main()