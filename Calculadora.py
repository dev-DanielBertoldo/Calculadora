#Calculadora#
#Author: github.com/dev-DanielBertoldo

aux = 0
#----------FUNÇÕES------------#
def Selecao ():
    divisor(10)
    print("1)Somar\n2)Subtrair\n3)Multiplicar\n4)Dividir\n0)Sair")
    divisor(10)
    return


def divisor(x):
    aux = 0
    while aux < x:
        print('*', end='')
        aux += 1
    print('')
#-----------------------------#
nome = input("Olá, eu sou T-Bot, como devo chama-lo(a)?\n ")
print(f'Saudações {nome}, porfavor selecione uma das opções a seguir:')
#-----------------------------#
while aux == 0:

    Selecao()
    slc = int(input("Seleção: "))

    #Operação de SOMA
    if slc == 1:
        auxsoma = input('-Operação de soma foi selecionada-\nDeseja prosseguir? (Y: sim, N: Não)\n')
        if auxsoma == 'y' or auxsoma == 'Y':
            n1 = int(input('Digite o primeiro valor da operação: '))
            n2 = int(input('Digite o segundo valor da operação: '))
            resultado = n1+n2
            print(f"O resultado da soma dos valores informados é: {resultado}")
            while t == 0:
                y = input("Deseja voltar para o menu de seleção? (Y: sim, N: não)\n")
                if y == 'y' or y =='Y':
                    t += 1
                    print('Reiniciando!')
                elif y == 'n' or y== 'N':
                    print('Desligando...')
                    aux -=1
                    break
                else:
                    print('(Valor Inválido! Selecione uma opção válida) \n')               
        elif auxsoma == "n" or auxsoma == "N":
            print('Reiniciando!')
        else:
            print('Valor inválido!')

    #Operação de SUBTRAÇÃO
    elif slc == 2:
        auxsub = input('-Operação de subtração foi selecionada-\nDeseja prosseguir? (Y: sim, N: Não)\n')
        if auxsub == 'y' or auxsub == 'Y':
            n1 = int(input('Digite o primeiro valor da operação: '))
            n2 = int(input('Digite o segundo valor da operação: '))
            resultado = n1-n2
            print(f"O resultado da subtração dos valores informados é: {resultado}")
            while t == 0:
                y = input("Deseja voltar para o menu de seleção? (Y: sim, N: não)\n")
                if y == 'y' or y =='Y':
                    t += 1
                    print('Reiniciando!')
                elif y == 'n' or y== 'N':
                    print('Desligando...')
                    aux -=1
                    break
                else:
                    print('(Valor Inválido! Selecione uma opção válida) \n')               
        elif auxsub == "n" or auxsub == "N":
            print('Reiniciando!')
        else:
            print('Valor inválido!')

    #Operação de MUKTIPLICAÇÃO
    elif slc == 3:
        t = 0
        auxmult = input('-Operação de MULTIPLICAÇÃO foi selecionada-\nDeseja prosseguir? (Y: sim, N: Não)\n')
        if auxmult == 'y' or auxmult == 'Y':
            n1 = int(input('Digite o primeiro valor da operação: '))
            n2 = int(input('Digite o segundo valor da operação: '))
            resultado = n1*n2
            print(f"O resultado da multiplicação dos valores informados é: {resultado}")
            while t == 0:
                y = input("Deseja voltar para o menu de seleção? (Y: sim, N: não)\n")
                if y == 'y' or y =='Y':
                    t += 1
                    print('Reiniciando!')
                elif y == 'n' or y== 'N':
                    print('Desligando...')
                    aux -=1
                    break
                else:
                    print('(Valor Inválido! Selecione uma opção válida) \n')               
        elif auxmult == "n" or auxmult == "N":
            print('Reiniciando!')
        else:
            print('Valor inválido!')
            
    #Operação de DIVISÃO
    elif slc == 4:
        auxdiv = input('-Operação de DIVISÃO foi selecionada-\nDeseja prosseguir? (Y: sim, N: Não)\n')
        if auxdiv == 'y' or auxdiv == 'Y':
            n1 = int(input('Digite o primeiro valor da operação: '))
            n2 = int(input('Digite o segundo valor da operação: '))
            resultado = n1/n2
            print(f"O resultado da subtração dos valores informados é: {resultado}")
            while t == 0:
                y = input("Deseja voltar para o menu de seleção? (Y: sim, N: não)\n")
                if y == 'y' or y =='Y':
                    t += 1
                    print('Reiniciando!')
                elif y == 'n' or y== 'N':
                    print('Desligando...')
                    aux -=1
                    break
                else:
                    print('(Valor Inválido! Selecione uma opção válida) \n')
        elif auxdiv == "n" or auxdiv == "N":
            print('Reiniciando!')
        else:
            print('Valor inválido!')

    elif slc == 0:
        print('Desligando...')
        break
    else:
        print('Valor inválido! Selecione outra opção.')