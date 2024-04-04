#parametros para passar dentro da chama de função cesar
MODE_ENCRYPT = 1
MODE_DECRYPT = 0


#func para realizar a criptografia e descriptografia, sendo passado o mode como 1(MODE_ENCRYPT)
# ou como 0(MODE_DECRYPT)
def cesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data


#func igual a de cima; apenas para puxar no pytest
def cesar2(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key #
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data


diferenca_carac = 3 #diferença no espaçamento para o proximo caractere que será embaralhado
original = 'Martim é fã do grupo de K-POP chamado BTS' #aqui vai a frase que quer criptografar
print('Original:', original)
criptografada = cesar(original, diferenca_carac, MODE_ENCRYPT) #joga para a func cesar como 1
print('Encriptada:', criptografada)
descriptografada = cesar2(criptografada, diferenca_carac, MODE_DECRYPT) #joga para a func cesar como 0
print('Decriptada:', descriptografada)