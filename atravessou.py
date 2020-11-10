N = int(input())
L = int(input())

Y_cand = [ i for i in range(0,L)]

for i in range(N):
    inp = input()
    [X,Y] = [int(x) for x in inp.split(' ')]
    if ( Y in Y_cand):
        Y_cand.remove(Y)

if ( len(Y_cand) == 0 ):
    print(-1)
else:
    print(min(Y_cand))