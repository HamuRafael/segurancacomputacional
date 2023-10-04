from collections import Counter
import string
import re

frequencias_ingles = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974,
    'Z': 0.00074
}

frequencias_portugues = {
    'A': 0.1463, 'B': 0.0104, 'C': 0.0388, 'D': 0.0499, 'E': 0.1257,
    'F': 0.0102, 'G': 0.0130, 'H': 0.0078, 'I': 0.0618, 'J': 0.0040,
    'K': 0.0002, 'L': 0.0278, 'M': 0.0474, 'N': 0.0505, 'O': 0.1073,
    'P': 0.0252, 'Q': 0.0120, 'R': 0.0653, 'S': 0.0781, 'T': 0.0434,
    'U': 0.0463, 'V': 0.0167, 'W': 0.0001, 'X': 0.0021, 'Y': 0.0001,
    'Z': 0.0047
}

def ic(texto):
    texto = ''.join(c for c in texto if c not in string.punctuation + ' ')
    n = 0.0
    f = 0.0
    contagem_caracteres = Counter(texto)
    
    for i in contagem_caracteres.values():
        n += i * (i - 1)
        f += i

    if f == 0.0 or f == 1:
        return 0.0
    else:
        return n / (f * (f - 1))

def comprimento_chave(cifra):
    comprimento_chave = 0

    melhores_ic = float('inf')
    
    for tamanho_chave in range(3, 11):
        grupos = [''] * tamanho_chave
        
        for i, caractere in enumerate(cifra):
            grupo_id = i % tamanho_chave
            grupos[grupo_id] += caractere
        
        ic_medio = sum(ic(grupo) for grupo in grupos) / tamanho_chave
        if abs(ic_medio) < abs(melhores_ic):
            melhores_ic = ic_medio
            comprimento_chave = tamanho_chave
    
    return comprimento_chave


def quebrar_vigenere(cifra, comprimento_chave, frequencias):
    cifra = re.sub(r'[^\w\s]', '', cifra)
    cifra = re.sub(r'[áàâã]', 'a', cifra, flags=re.IGNORECASE)
    cifra = re.sub(r'[éèê]', 'e', cifra, flags=re.IGNORECASE)
    cifra = re.sub(r'[íì]', 'i', cifra, flags=re.IGNORECASE)
    cifra = re.sub(r'[óòôõ]', 'o', cifra, flags=re.IGNORECASE)
    cifra = re.sub(r'[úùû]', 'u', cifra, flags=re.IGNORECASE)

    grupos = [''.join(cifra[i::comprimento_chave]) for i in range(comprimento_chave)]
    texto_descriptografado = ''
    chave = []
    
    for grupo in grupos:
        contagem_letras = {letra: grupo.count(letra) for letra in string.ascii_lowercase}
        letra_maior_frequencia = max(contagem_letras, key=lambda k: contagem_letras[k])
        valor_deslocamento = (ord(letra_maior_frequencia) - ord('A')) % 26
        chave.append(chr(((ord(letra_maior_frequencia) - valor_deslocamento) + 26) % 26 + ord('A')))
        
        grupo_descriptografado = ''.join(chr((ord(letra) - valor_deslocamento - ord('A')) % 26 + ord('A')) for letra in grupo)
        texto_descriptografado += grupo_descriptografado
    
    return ''.join(chave), texto_descriptografado



def main():
    cifra = "fzlfmeea é lma wota dv czrcf. frbirnf é o dfmrdoi dr fota. tadr vvz qle vla wita cfm r boca eo nrrzz, frbzanf lye dá lm geioe. r meeieadr vê wilfmvna tod a bflr e pvdv “bij”. eca rvpvte f qle fvz, uá umr rvbocaua e jaz cod ud pezxv na sota tfdr feciq! degozs eca mai uejcaesrr, prrr mazs karue wazvr futio vspvtátulf."

    print("Índice de coincidência ", ic(cifra))
    tamanho = comprimento_chave(cifra)
    print("Estimativa do comprimento da chave:", tamanho)

    chave, texto = quebrar_vigenere(cifra, 5, frequencias_portugues)
    print("Chave estimada ", chave)
    print("Texto descriptografado ", texto)


if __name__ == "__main__":
    main()
