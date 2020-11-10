inp = input()
[A,B] = [x for x in inp.split(' ')]

estacoes = ['V','O','I','P']

iA = estacoes.index(A)
iB = estacoes.index(B)

q = iB - iA 

if ( q <= 0 ): q += 4

print(q)
