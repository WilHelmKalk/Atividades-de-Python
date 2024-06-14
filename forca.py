import random


palavras = ["python", "programacao", "computador", "inteligencia", "openai", "desenvolvimento", "aprendizado"]

def escolher_palavra(palavras):
    return random.choice(palavras)


palavra_escolhida = escolher_palavra(palavras)
print("Palavra escolhida:", palavra_escolhida)

def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta


letras_corretas = ['p', 'r', 'g', 'm', 'c']
print("Palavra oculta:", exibir_palavra_oculta(palavra_escolhida, letras_corretas))

def fazer_tentativa():
    letra = input("Digite uma letra: ")
    return letra.lower() 


tentativa = fazer_tentativa()
print("Tentativa do jogador:", tentativa)

def verificar_tentativa(letra, palavra, letras_corretas, erros):
    if letra in palavra:
        letras_corretas.append(letra)
    else:
        erros += 1
    return letras_corretas, erros


letras_corretas, erros = verificar_tentativa('a', palavra_escolhida, letras_corretas, 1)
print("Letras corretas:", letras_corretas)
print("Erros:", erros)

def verificar_fim_do_jogo(palavra, letras_corretas, erros):
    if all(letra in letras_corretas for letra in palavra):
        return True, "Você venceu! A palavra era: " + palavra
    elif erros >= 6:
        return True, "Você perdeu! A palavra era: " + palavra
    else:
        return False, ""


fim_do_jogo, mensagem = verificar_fim_do_jogo(palavra_escolhida, letras_corretas, erros)
if fim_do_jogo:
    print(mensagem)
else:
    print("O jogo ainda não acabou.")


while True:
    
    tentativa = fazer_tentativa()

    
    letras_corretas, erros = verificar_tentativa(tentativa, palavra_escolhida, letras_corretas, erros)

    
    print("Palavra:", exibir_palavra_oculta(palavra_escolhida, letras_corretas))

    
    fim_do_jogo, mensagem = verificar_fim_do_jogo(palavra_escolhida, letras_corretas, erros)
    if fim_do_jogo:
        print(mensagem)
        break

    