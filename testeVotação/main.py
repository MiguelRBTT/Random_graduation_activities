import datetime

def compara_data(data1, data2):
    diferenca = data1 - data2
    print(diferenca.days)
    if diferenca / 365 == 16.01095890410959:
        print('Sim')


data_menor = datetime.datetime(2008, 4, 18)

data_atual = datetime.datetime(2024, 4, 18)

compara_data(data_atual, data_menor)


