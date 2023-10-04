import string
lista = []
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def main():

    opcao = int(input('Digite 1 para Criptografrar, 2 para Descriptografar: '))
    chave = ''.join(str(input('Digite a chave: '))).lower()
    texto = (str(input('Digite a mensagem para ser criptografada: '))).lower()        # RETIRA SIMBOLOS E NUMEROS DA MENSAGEM 
    
    
    if opcao != 1 and opcao != 2:
        print('Digite 1 ou 2.')
        #ENTRA NA FUNCAO DE CRIPTOGRAFIA
    elif opcao == 1:
        criptografar(texto,chave)
    #ENTRA NA FUNCAO DE DESCRIPTOGRAFAR
    elif opcao == 2:
        descriptografar(texto,chave)

def criptografar(texto,chave):
    mensagem_criptografada = ''
    keyFinal = ""
    
    i = 0
    if len(texto) < len(chave):
        print('A mensagem é menor que a chave.')
        return
    while(len(keyFinal) < len(texto)):
        keyFinal += chave[i]
        i+=1
        if i == len(chave):
            i = 0
            
    for i in range(len(texto)):
        if texto[i] in alfabeto:
            posicao_letra = int(alfabeto.index(texto[i]))
            posicao_letra_chave = int(alfabeto.index(keyFinal[i]))
            mensagem_criptografada += str(alfabeto[(posicao_letra+posicao_letra_chave) %26])
        else:
            mensagem_criptografada += texto[i]
        
    print(mensagem_criptografada)
    
def descriptografar(texto,chave):
    mensagem_criptografada = ''
    keyFinal = ""
    i = 0
    if len(texto) < len(chave):
        print('A mensagem é menor que a chave.')
        return
    while(len(keyFinal) < len(texto)):
        keyFinal += chave[i]
        i+=1
        if i == len(chave):
            i = 0
            
    for i in range(len(texto)):
        if texto[i] in alfabeto:
            
            posicao_letra = int(alfabeto.index(texto[i]))
            posicao_letra_chave = int(alfabeto.index(keyFinal[i]))
            mensagem_criptografada += str(alfabeto[(posicao_letra-posicao_letra_chave) %26])
    
        else:
            mensagem_criptografada += texto[i]
    print(mensagem_criptografada)
if __name__ == '__main__':
    main()
