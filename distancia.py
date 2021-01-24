inp = input()
[C,L] = [float(x) for x in inp.split(' ')]

S = input()
[D,F] = [float(x) for x in S.split(' ')]

N = int(input())

capLagoa = int(C * L * D)

foraLagoa = N - capLagoa

capMargens = int(2*F*(L+C)) 

if ( capMargens >= foraLagoa ):
    print('YES')
else:
    print('NO')