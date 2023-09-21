import string
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' '
letras_index = dict(zip(alfabeto,range(len(alfabeto))))
index_letras = dict(zip(range(len(alfabeto)),alfabeto))
def main():

    opcao = int(input('Digite 1 para Criptografrar, 2 para Descriptografar: '))
    if opcao != 1 and opcao != 2:
        print('Digite 1 ou 2.')
    elif opcao == 1:
        chave = ''.join(str(input('Digite a chave: '))).upper()
        mensagem = (str(input('Digite a mensagem para ser criptografada: '))).upper()
        criptografar(mensagem,chave)

    
    elif opcao == 2:
        chave = str(input('Digite a chave: ')).upper()
        cifra = str(input('Digite a mensagem para ser criptografada: ')).upper()
        descriptografar(cifra,chave)
    
def criptografar(mensagem,chave):
    mensagem_criptografada = ''

    index = 0
    for c in mensagem:
        if c in string.ascii_uppercase:
            offset = ord(chave[index]) - ord('a')

            criptografia = chr((ord(c)-ord('a')+offset)%26 + ord('a'))
            mensagem_criptografada = mensagem_criptografada + criptografia
            index = (index+1) % len(chave)
        else:
            mensagem_criptografada = mensagem_criptografada + c
    print(mensagem_criptografada)
    #algoritmo que vi na internet, que da um split na mensagem no tamanho da chave
   # split_message = [mensagem[i:i + len(chave)] for i in range(0, len(''.join(mensagem)), len(chave))]

    #for each_split in split_message:
     #   i = 0
      #  for letra in each_split:
       #    numero = (letras_index[letra] + letras_index[chave[i]]) % len(alfabeto)
        #   mensagem_criptografada += index_letras[numero]
         #  i+=1
    print(mensagem_criptografada)
def descriptografar(cifra,chave):
    pass

if __name__ == '__main__':
    main()
