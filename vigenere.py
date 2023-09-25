import string
import re
lista = []
alfabeto = 'abcdefghijklmnopqrstuvwxyz '
letras_index = dict(zip(alfabeto,range(len(alfabeto))))
index_letras = dict(zip(range(len(alfabeto)),alfabeto))

def main():

    opcao = int(input('Digite 1 para Criptografrar, 2 para Descriptografar: '))
    
    if opcao != 1 and opcao != 2:
        print('Digite 1 ou 2.')
        #ENTRA NA FUNCAO DE CRIPTOGRAFIA
    elif opcao == 1:
        chave = ''.join(str(input('Digite a chave: '))).lower()
        mensagem = (str(input('Digite a mensagem para ser criptografada: '))).lower()        # RETIRA SIMBOLOS E NUMEROS DA MENSAGEM 
        for i in mensagem:
            if i not in alfabeto:
                lista.append(i)
                mensagem = mensagem.replace(i,"")
        
        if len(lista) != 0:
            print(f'Os caracteres {lista} foram removidos.')
        criptografar(mensagem,chave)

    #ENTRA NA FUNCAO DE DESCRIPTOGRAFAR
    elif opcao == 2:
        chave = str(input('Digite a chave: ')).upper()
        cifra = str(input('Digite a mensagem para ser descriptografada: ')).upper()
        


def criptografar(mensagem,chave):
    mensagem_criptografada = ''
    keyFinal = ""
    textofinal = ''
    i = 0
    if len(mensagem) < len(chave):
        print('A mensagem é menor que a chave.')
        return
    while(len(keyFinal) < len(mensagem)):
        keyFinal += chave[i]
        i+=1
        if i == len(chave):
            i = 0
            
    for i in range(len(mensagem)):
        if mensagem[i] != ' ':
            posicao_letra = int(alfabeto.index(mensagem[i]))
            print(keyFinal)
            posicao_letra_chave = int(alfabeto.index(keyFinal[i]))
            textofinal += str(alfabeto[(posicao_letra+posicao_letra_chave) %26])
        else:
            textofinal += ' '
        

    print(textofinal)



    
    print(mensagem_criptografada)

    

    
def descriptografar(cifra,chave):
    pass

if __name__ == '__main__':
    main()

