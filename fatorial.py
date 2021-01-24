inp = input()
[N,A,B] = [int(x) for x in inp.split(' ')]

fa = 1
fb = 1
fn = 3628800

def fat (v):
    if (v >0): 
        return v*(fat(v-1))
    return 1

if (A == 1 or B == 1):
    if(A == 1):
        if (B == N):
            print("YES")
        else:
            print("NO")
    else:
        if (A == N):
            print("YES")
        else:
            print("NO")
elif (N != 10):
    print("NO")
else:
    if(A < 11 and B < 11):
            fa = fat(A) 
            fb = fat(B)
            result = fa * fb
            if(result == fn):
                print("YES")
            else:
                print("NO")
    else:
        print("NO");