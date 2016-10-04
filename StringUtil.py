def output(texto):
    print(texto)
def tamanho(texto):
    TamanhoTexto = len(texto)
    return TamanhoTexto
def maiusculo(texto):
    MaiusculaT = texto.upper()
    return MaiusculaT
def minusculo(texto):
    minusculaT = texto.lower()
    return minusculaT
def contador(texto):
    letraBusca = input("Qual a letra a ser encontrada? ")
    a = 0
    for letrabusca1 in texto:
        if(letraBusca == letrabusca1):
            a = a + 1
    if(a == 0):
        print ("Letra não encontrada")
    elif(a > 0):
        print("A letra", letraBusca, "aparece", a, "vezes no texto:", texto)
