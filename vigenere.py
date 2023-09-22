import string
import re
lista = []
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' '
letras_index = dict(zip(alfabeto,range(len(alfabeto))))
index_letras = dict(zip(range(len(alfabeto)),alfabeto))
def main():

    opcao = int(input('Digite 1 para Criptografrar, 2 para Descriptografar: '))
    
    if opcao != 1 and opcao != 2:
        print('Digite 1 ou 2.')
        #ENTRA NA FUNCAO DE CRIPTOGRAFIA
    elif opcao == 1:
        chave = ''.join(str(input('Digite a chave: '))).upper() 
        mensagem = (str(input('Digite a mensagem para ser criptografada: '))).upper()
        # RETIRA SIMBOLOS E NUMEROS DA MENSAGEM 
        for i in mensagem:
            if i not in alfabeto:
                lista.append(i)
                mensagem = mensagem.replace(i,"")
        print(f'Os caracteres {lista} foram removidos.')
        criptografar(mensagem,chave)

    #ENTRA NA FUNCAO DE DESCRIPTOGRAFAR
    elif opcao == 2:
        chave = str(input('Digite a chave: ')).upper()
        cifra = str(input('Digite a mensagem para ser descriptografada: ')).upper()
        descriptografar(cifra,chave)
    
def criptografar(mensagem,chave):
    mensagem_criptografada = ''
    j = 0
    for i in range(len(mensagem)):
        if ord(mensagem[i]) == 32:
            mensagem_criptografada += " "
        else:
            if j < len(chave):
                mensagem_criptografada += chave[j]
                j += 1
            else:
                j = 0
                mensagem_criptografada += chave[j]
                j += 1
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
