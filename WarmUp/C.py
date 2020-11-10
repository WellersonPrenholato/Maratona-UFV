frase = input()

frase = frase.replace(' ','').lower()
vogais = [ c for c in frase if c in ['a','e','i','o','u'] ]

if ( len(vogais) >= len(frase)*0.5 ):
    print('facil')
else:
    print('dificil')



