nome = input()

def quasePalin(nome):
    nome = nome.replace(' ', '').lower()
    t = len(nome)

    qtDiff = 0
    for i in range(t//2):
        if ( nome[i] != nome[t-i-1] ):
            qtDiff += 1
            if ( qtDiff > 1 ):
                return 'NO'
    return 'YES'


print(quasePalin(nome))