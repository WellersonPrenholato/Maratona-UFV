inp = input()
[C,A,P] = [int(x) for x in inp.split(' ')]

qtd = 0
qtdPrev = {
    '0': 1,
}
for i in range(1,P+1):
    
    qtdPrev[str(i)] = qtdPrev[str(i-1)] * C * A * 4
    qtd += qtdPrev[str(i)]

print(qtd % 1000000007)