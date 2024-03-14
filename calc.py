def soma(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print('Escolha uma operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

while True:
    
    opera = input('Escolha a sua operação 1/2/3/4: ')

    if opera in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Escreva seu primeiro número: '))
            num2 = float(input('Escreva seu segundo número: '))
        except ValueError:
            print('Valor inválido. Tente outro valor.')
            continue
        if opera == '1':
            print(num1, '+', num2, '=', soma(num1, num2))
        elif opera == '2':
            print(num1, '-', num2, '=', subt(num1, num2))
        elif opera == '3':
            print(num1, '*', num2, '=', mult(num1, num2))
        elif opera == '1':
            print(num1, '/', num2, '=', div(num1, num2))
        
        prox_conta = input('Gostaria de fazer outro cálculo | S - (Sim) | N - (Não):')

        if prox_conta == 'Não' or prox_conta == 'não':
            break
    else:
        print('Valor inválido')